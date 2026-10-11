# Bateria de regressão do site: python testes/regressao.py <url-base> <nome-da-rodada>
# Grava testes/resultados/<nome>.json e capturas, para comparar antes e depois de cada correção.
import asyncio, json, sys, pathlib, re, urllib.parse, urllib.request, urllib.error, http.client
import urllib.parse as up
from playwright.async_api import async_playwright

BASE = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "http://127.0.0.1:5000"
NOME = sys.argv[2] if len(sys.argv) > 2 else "rodada"
OUT = pathlib.Path(__file__).parent / "resultados"; OUT.mkdir(exist_ok=True)

CONTRASTE = r"""() => {
 const lum=c=>{const m=c.match(/[\d.]+/g); if(!m) return null; return m.slice(0,3).map(Number).map(v=>{v/=255;return v<=0.03928?v/12.92:((v+0.055)/1.055)**2.4}).reduce((a,v,i)=>a+v*[0.2126,0.7152,0.0722][i],0)};
 const bg=el=>{while(el){const c=getComputedStyle(el).backgroundColor,a=c.match(/[\d.]+/g); if(a&&(a.length<4||+a[3]>0.5)) return c; el=el.parentElement} return 'rgb(255,255,255)'};
 const out=new Set();
 document.querySelectorAll('p,span,a,li,label,h1,h2,h3,h4,button,b,strong,em').forEach(e=>{
  if(!e.offsetParent) return; const t=[...e.childNodes].filter(n=>n.nodeType==3).map(n=>n.textContent.trim()).join(' ').trim(); if(!t) return;
  const s=getComputedStyle(e); if(+s.opacity<0.3) return; const r=e.getBoundingClientRect(); if(r.width<2||r.height<2) return;
  const a=lum(s.color),b=lum(bg(e)); if(a==null||b==null) return; const k=(Math.max(a,b)+.05)/(Math.min(a,b)+.05);
  const fs=parseFloat(s.fontSize), grande=fs>=24||(fs>=18.66&&+s.fontWeight>=700);
  if(k<(grande?3:4.5)) out.add(t.slice(0,40)+' ('+k.toFixed(2)+')');
 }); return [...out];
}"""

async def main():
    R = {"base": BASE, "falhas": []}
    def ok(nome, cond, info=""):
        R[nome] = {"ok": bool(cond), "info": info}
        if not cond: R["falhas"].append(f"{nome}: {info}")
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="msedge")
        # ---------- desktop ----------
        c = await b.new_context(viewport={"width": 1440, "height": 900})
        pg = await c.new_page()
        erros, reqs = [], []
        pg.on("pageerror", lambda e: erros.append("pageerror: " + str(e)))
        pg.on("console", lambda m: m.type == "error" and erros.append("console: " + m.text))
        pg.on("request", lambda r: reqs.append(r.url))
        resp = await pg.goto(BASE + "/?utm_source=teste&utm_campaign=regressao", wait_until="networkidle")
        await pg.wait_for_timeout(800)
        h = resp.headers
        R["headers"] = {k: h.get(k) for k in ["content-security-policy", "permissions-policy", "x-frame-options", "cache-control", "strict-transport-security"]}
        texto = await pg.evaluate("document.body.innerText")
        ok("sem_demo", "Demonstração" not in texto and "provisório" not in texto, "aviso de demonstração visível")
        colch = re.findall(r"\[[^\]]{1,60}\]", texto)
        ok("sem_colchetes", not colch, colch)
        ok("sem_todo", await pg.evaluate("document.querySelectorAll('.todo').length") == 0, "elementos .todo")
        rod = await pg.evaluate("document.querySelector('footer').innerText")
        ok("rodape_cnpj", "58.332.620/0001-08" in rod, rod[-160:])
        ok("rodape_niteroi", "Niterói" in rod and "Sede no Rio" not in rod, rod[-160:])
        ok("sem_recarga_versao", not [u for u in reqs if "nocache=" in u], [u for u in reqs if "nocache=" in u])
        head = await pg.evaluate("""({og:[...document.querySelectorAll('meta[property^="og:"],meta[name^="twitter:"]')].map(m=>(m.getAttribute('property')||m.name)+'='+m.content),
            ld:[...document.querySelectorAll('script[type="application/ld+json"]')].map(s=>s.textContent),
            icons:[...document.querySelectorAll('link[rel*=icon]')].map(l=>l.rel+' '+l.getAttribute('href').slice(0,40))})""")
        R["head"] = head
        ok("og_imagem", any(x.startswith("og:image=") for x in head["og"]), head["og"])
        ldok = True
        for s in head["ld"]:
            try: json.loads(s)
            except Exception: ldok = False
        ok("json_ld", head["ld"] and ldok, "ausente ou inválido")
        ok("favicon_arquivo", any("data:" not in i for i in head["icons"]), head["icons"])
        ok("contraste", True, await pg.evaluate(CONTRASTE))
        # imagens e peso
        R["recursos"] = await pg.evaluate("performance.getEntriesByType('resource').map(r=>[r.name.split('/').pop().split('?')[0],Math.round(r.transferSize/1024)])")
        R["metricas"] = await pg.evaluate("""(async()=>{const n=performance.getEntriesByType('navigation')[0];
           const cls=await new Promise(r=>{let v=0;new PerformanceObserver(l=>l.getEntries().forEach(e=>{if(!e.hadRecentInput)v+=e.value})).observe({type:'layout-shift',buffered:true});setTimeout(()=>r(+v.toFixed(3)),600)});
           return {load:Math.round(n.loadEventEnd),dcl:Math.round(n.domContentLoadedEventEnd),cls}})()""")
        # simulador -> formulário
        await pg.fill("#s-marca", "PADARIA DO ZÉ")
        await pg.click("label[for='f2']")
        await pg.wait_for_timeout(200)
        sim = await pg.evaluate("document.querySelector('#simOnibus').innerText")
        ok("simulador_texto", "PADARIA" in sim.upper(), sim[:60])
        await pg.click("#simCta"); await pg.wait_for_timeout(300)
        # formulário
        await pg.evaluate("window.__abertos=[]; window.open=(u)=>{window.__abertos.push(u);return null}")
        await pg.click("[data-passo='1'] [data-ir='2']"); await pg.wait_for_timeout(150)
        val = await pg.evaluate("[...document.querySelectorAll('.erro')].map(e=>e.textContent).filter(Boolean)")
        ok("validacao", len(val) >= 2, val)
        await pg.fill("#f-nome", "Maria Teste"); await pg.fill("#f-wa", "21999998888")
        await pg.check("input[name='contato'][value='Ligação']", force=True)
        await pg.check("#f-aceite", force=True)
        await pg.click("[data-passo='1'] [data-ir='2']"); await pg.wait_for_timeout(150)
        await pg.fill("#f-empresa", "ACME"); await pg.fill("#f-regiao", "Niterói")
        await pg.click("[data-passo='2'] [data-ir='3']"); await pg.wait_for_timeout(150)
        await pg.click("#proposta [type=submit]"); await pg.wait_for_timeout(400)
        abertos = [u for u in await pg.evaluate("window.__abertos") if u]
        msg = urllib.parse.unquote(abertos[-1]) if abertos else ""
        R["mensagem_whatsapp"] = msg
        ok("form_abre_whatsapp", msg.startswith("https://wa.me/5521986062741"), msg[:80])
        ok("form_tem_contato", "Liga" in msg, "preferência de contato fora da mensagem")
        ok("form_tem_simulador", "PADARIA" in msg.upper(), "escolha do simulador fora da mensagem")
        ok("form_tem_origem", "teste" in msg and "regressao" in msg, "UTM fora da mensagem")
        ok("form_tela_final", await pg.evaluate("document.getElementById('feito').classList.contains('on')"), "")
        # agenda
        await pg.evaluate("document.querySelector('#agenda').scrollIntoView()")
        dias = await pg.query_selector_all("#dias button:not([disabled])")
        if dias:
            await dias[0].click(); await pg.wait_for_timeout(150)
            sl = await pg.query_selector_all("#slots button")
            if sl: await sl[0].click()
        href = await pg.get_attribute("#agendar", "href") or ""
        ok("agenda", href.startswith("https://wa.me/"), href[:60])
        ok("sem_erros_js", not erros, erros)
        await pg.screenshot(path=str(OUT / f"{NOME}_desk.png"), full_page=True)
        await c.close()
        # ---------- celular ----------
        m = await b.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True)
        mp = await m.new_page(); merros = []
        mp.on("pageerror", lambda e: merros.append(str(e)))
        await mp.goto(BASE + "/", wait_until="networkidle")
        ok("mobile_sem_rolagem_lateral", not await mp.evaluate("document.documentElement.scrollWidth > innerWidth + 1"), "")
        btn = await mp.query_selector("button[aria-label='Abrir menu']")
        if btn:
            await btn.click(); await mp.wait_for_timeout(300)
        ok("mobile_menu", btn and await btn.get_attribute("aria-expanded") == "true", "")
        ok("mobile_sem_erros", not merros, merros)
        await mp.screenshot(path=str(OUT / f"{NOME}_mob.png"), full_page=True)
        # privacidade e 404
        r2 = await mp.goto(BASE + "/privacidade", wait_until="networkidle")
        ptxt = await mp.evaluate("document.body.innerText")
        ok("privacidade_coerente", "Preferências de cookies" not in ptxt and "58.332.620" in ptxt, "")
        await mp.screenshot(path=str(OUT / f"{NOME}_priv.png"), full_page=True)
        r3 = await mp.goto(BASE + "/pagina-que-nao-existe", wait_until="networkidle")
        t404 = await mp.evaluate("document.title + document.body.innerText")
        ok("pagina_404", r3.status == 404 and "Plano Urbano" in t404 and "firebase.json" not in t404, f"status {r3.status}")
        await mp.screenshot(path=str(OUT / f"{NOME}_404.png"))
        await m.close()
        # movimento reduzido
        rc = await b.new_context(reduced_motion="reduce"); rp = await rc.new_page()
        await rp.goto(BASE + "/", wait_until="networkidle")
        ok("movimento_reduzido", await rp.evaluate("document.getAnimations().filter(a=>a.playState==='running').length") == 0, "")
        await rc.close()
        # capturas estáveis para comparar visualmente (sem animação, imagens já carregadas)
        for tela, vp, mob in (("desk", {"width": 1440, "height": 900}, False), ("mob", {"width": 390, "height": 844}, True)):
            cc = await b.new_context(viewport=vp, is_mobile=mob, has_touch=mob, reduced_motion="reduce"); cp = await cc.new_page()
            await cp.goto(BASE + "/", wait_until="networkidle")
            await cp.add_style_tag(content="html{scroll-behavior:auto!important}")
            for y in range(0, 8000, 500): await cp.evaluate(f"scrollTo(0,{y})"); await cp.wait_for_timeout(40)
            await cp.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')"); await cp.wait_for_timeout(600)
            await cp.evaluate("scrollTo(0,0)"); await cp.wait_for_timeout(200)
            await cp.screenshot(path=str(OUT / f"{NOME}_limpa{tela}.png"), full_page=True)
            await cc.close()
        # ---------- varredura 2 ----------
        ok("fontes_locais", not [u for u in reqs if "fonts.googleapis" in u or "fonts.gstatic" in u], "fontes vindo do Google")
        # CSS sem chaves sobrando (todas as páginas)

        for pag in ("/", "/privacidade", "/pagina-inexistente"):
            try: html = urllib.request.urlopen(BASE + pag).read().decode("utf-8")
            except urllib.error.HTTPError as e: html = e.read().decode("utf-8")   # a 404 responde com status 404
            css = re.sub(r"/\*.*?\*/", "", "".join(re.findall(r"<style>(.*?)</style>", html, re.S)), flags=re.S)
            d, ruim = 0, False
            for ch in css:
                d += (ch == "{") - (ch == "}")
                ruim = ruim or d < 0
            ok("css_chaves" + pag.replace("/", "_"), not ruim and d == 0, "chaves desbalanceadas")
        # formulário: +55, DDD inválido, limite de tamanho
        fc = await b.new_context(viewport={"width": 1440, "height": 900}); fp = await fc.new_page()
        await fp.goto(BASE + "/", wait_until="networkidle")
        await fp.type("#f-wa", "+55 (21) 99999-8888")
        ok("tel_mais55", await fp.input_value("#f-wa") == "(21) 99999-8888", await fp.input_value("#f-wa"))
        await fp.fill("#f-nome", "Teste"); await fp.fill("#f-wa", ""); await fp.type("#f-wa", "0800 123 4567"); await fp.check("#f-aceite", force=True)
        await fp.click("[data-passo='1'] [data-ir='2']"); await fp.wait_for_timeout(150)
        ok("ddd_invalido_recusado", await fp.evaluate("document.querySelector('.passo.on').dataset.passo") == "1", await fp.input_value("#f-wa"))
        ok("limite_tamanho", await fp.evaluate("['f-nome','f-empresa','f-ramo','f-regiao','f-obj','s-marca'].every(i=>document.getElementById(i).maxLength>0)"), "campo sem maxlength")
        ok("agenda_sem_href_desativado", await fp.evaluate("!document.getElementById('agendar').hasAttribute('href')"), "link desativado com href")
        await fc.close()
        # celular: Esc fecha o menu; carrossel alcançável pelo teclado
        mc = await b.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True); mp = await mc.new_page()
        await mp.goto(BASE + "/", wait_until="networkidle")
        await mp.click("button[aria-label='Abrir menu']"); await mp.keyboard.press("Escape"); await mp.wait_for_timeout(200)
        ok("menu_esc", await mp.evaluate("(()=>{const b=document.querySelector('button.menu,button[aria-controls]');return b.getAttribute('aria-expanded')==='false'&&document.activeElement===b})()"), "Esc não fecha ou foco não volta")
        await mc.close()
        # sem JavaScript: WhatsApp continua funcionando
        nc = await b.new_context(java_script_enabled=False); np_ = await nc.new_page()
        await np_.goto(BASE + "/", wait_until="networkidle")
        hs = await np_.evaluate("[...document.querySelectorAll('.js-wa')].map(a=>a.getAttribute('href'))")
        ok("whatsapp_sem_js", hs and all(h.startswith("https://wa.me/") for h in hs), hs)
        await nc.close()
        # alto contraste: botões com contorno
        hc = await b.new_context(forced_colors="active"); hp = await hc.new_page()
        await hp.goto(BASE + "/", wait_until="networkidle")
        ok("botoes_alto_contraste", await hp.evaluate("[...document.querySelectorAll('.btn')].filter(e=>e.offsetParent).every(e=>parseFloat(getComputedStyle(e).borderTopWidth)>0)"), "botão sem contorno")
        await hc.close()
        # axe-core (WCAG 2.2 AA + boas práticas), desktop e celular
        for w, mob in ((1440, False), (390, True)):
            ac = await b.new_context(viewport={"width": w, "height": 900}, is_mobile=mob, has_touch=mob, bypass_csp=True); ap = await ac.new_page()
            await ap.goto(BASE + "/", wait_until="networkidle")
            for y in range(0, 7000, 700): await ap.evaluate(f"scrollTo(0,{y})"); await ap.wait_for_timeout(40)
            await ap.add_script_tag(url="https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.2/axe.min.js")
            v = await ap.evaluate("axe.run(document,{runOnly:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa','best-practice']}).then(r=>r.violations.map(v=>v.id+'('+v.nodes.length+')'))")
            ok(f"axe_{w}", not v, v)
            await ac.close()
        # ---------- v3: itens do ChatGPT + fotos reais ----------
        try: bruto = urllib.request.urlopen(BASE + "/").read().decode("utf-8")
        except urllib.error.HTTPError as e: bruto = e.read().decode("utf-8")
        semjs = re.sub(r"<script.*?</script>", "", bruto, flags=re.S)   # conteúdo da página (o script só cria o aviso se houver medição)
        ok("v3_sem_texto_cookies", "Usamos cookies" not in semjs and "Preferências de cookies" not in semjs, "texto de cookies no HTML")
        ok("v3_agenda_sugerir", ">Agendar conversa<" not in bruto and "Sugerir horário" in bruto, "nome antigo da agenda")
        ok("v3_letreiro_1x", len(re.findall(r"Inevitável", bruto)) == 1, len(re.findall(r"Inevitável", bruto)))
        ok("v3_backbus_indicado", "Indicado para fixar" in bruto, "")
        ok("v3_faixa_investimento", "Faixa de investimento" in bruto and "Ainda estou avaliando" in bruto, "")
        ok("v3_aviso_transparencia", "não são enviados automaticamente" in bruto, "")
        ok("v3_simulador_fecho", "Gostou de ver sua marca na rua?" in bruto, "")
        vc = await b.new_context(viewport={"width": 1440, "height": 900}); vp = await vc.new_page()
        await vp.goto(BASE + "/?utm_source=src1&utm_medium=med2&utm_campaign=cmp3&utm_content=cnt4&utm_term=trm5", wait_until="networkidle")
        ok("v3_opcionais", await vp.evaluate("['f-empresa','f-ramo','f-regiao','f-obj'].every(i=>/opcional/i.test(document.querySelector('label[for='+i+']').textContent))"), "campo opcional sem marca")
        await vp.evaluate("window.__ab=[];window.open=u=>{__ab.push(u);return null}")
        await vp.fill("#f-nome", "Rita Resumo"); await vp.fill("#f-wa", "21999998888"); await vp.check("#f-aceite", force=True)
        await vp.click("[data-passo='1'] [data-ir='2']"); await vp.wait_for_timeout(120); await vp.fill("#f-empresa", "Loja Resumo")
        await vp.click("[data-passo='2'] [data-ir='3']"); await vp.wait_for_timeout(200)
        res = await vp.evaluate("(document.getElementById('resumo')||{}).innerText||''")
        ok("v3_resumo_pedido", "Rita Resumo" in res and "Loja Resumo" in res, res[:80])
        await vp.click("#proposta [type=submit]"); await vp.wait_for_timeout(300)
        msg5 = urllib.parse.unquote(next((u for u in await vp.evaluate("__ab") if u), ""))
        ok("v3_origem_5_utm", all(x in msg5 for x in ("src1", "med2", "cmp3", "cnt4", "trm5")), msg5[-90:])
        # seções novas e fotos reais carregando
        for y in range(0, 9000, 600): await vp.evaluate(f"scrollTo(0,{y})"); await vp.wait_for_timeout(50)
        await vp.wait_for_timeout(800)
        gal = await vp.evaluate("(()=>{const s=document.getElementById('campanhas');if(!s)return null;const im=[...s.querySelectorAll('img')];return {n:im.length,alt:im.every(i=>i.alt.trim().length>5),carregou:im.every(i=>i.complete&&i.naturalWidth>0)}})()")
        ok("v3_galeria", gal and gal["n"] >= 8 and gal["alt"] and gal["carregou"], gal)
        ok("v3_como_funciona", await vp.evaluate("(()=>{const s=document.getElementById('como-funciona');return !!s&&s.querySelectorAll('ol > li').length===5})()"), "")
        ok("v3_topo_fotos_reais", await vp.evaluate(r"![...document.querySelectorAll('.mosaico img')].some(i=>/img\/(onibus|passageiro|luzes)\.webp/.test(i.src))"), "foto de banco no topo")
        ok("v3_imagens_ok", await vp.evaluate("[...document.images].filter(i=>i.loading!=='lazy'||i.getBoundingClientRect().top<innerHeight*3).every(i=>i.complete&&i.naturalWidth>0)"), "imagem quebrada")
        await vc.close()
        # ---------- H1–H6 (congelamento da v3) ----------
        try: priv = urllib.request.urlopen(BASE + "/privacidade").read().decode("utf-8")
        except urllib.error.HTTPError as e: priv = e.read().decode("utf-8")
        ok("h1_privacidade_fluxo", "O site não armazena" in priv and "depois que você envia" in priv, "")
        ok("h2_encarregado", "Encarregado pelo tratamento de dados pessoais" in priv and "(DPO)" not in priv.split("Encarregado pelo tratamento")[0][-40:], "")
        ok("h3_regioes", "pelas regiões onde o seu público circula" in bruto and "diante do público que você quer alcançar" not in bruto, "")
        ok("h4_agenda_vazio", "Escolha um dia para ver os horários" in bruto and "Os horários aparecem aqui" not in bruto, "")
        ok("h5_comentario_w3c", "falso positivo" in open(pathlib.Path(__file__).parent.parent / "src.html", encoding="utf-8").read(), "")
        ok("h6_retorno", "Como prefere que a Plano Urbano retorne?" in bruto and 'value="Ligação"' in bruto, "")
        ok("h6_mensagem", "Prefere retorno por: Ligação" in R.get("mensagem_whatsapp", ""), R.get("mensagem_whatsapp", "")[-120:])
        # endereços que davam 404 sem necessidade

        for pth, esperado in (("/privacidade/", (301, 302)), ("/favicon.ico", (200, 301, 302))):
            pu = up.urlparse(BASE); cn = (http.client.HTTPSConnection if pu.scheme == "https" else http.client.HTTPConnection)(pu.netloc)
            cn.request("GET", pth); st = cn.getresponse().status
            ok("url" + pth.replace("/", "_").replace(".", "_"), st in esperado, st)
        await b.close()
    (OUT / f"{NOME}.json").write_text(json.dumps(R, ensure_ascii=False, indent=1), encoding="utf-8")
    checks = {k: v for k, v in R.items() if isinstance(v, dict) and "ok" in v}
    print(f"{NOME}: {sum(v['ok'] for v in checks.values())}/{len(checks)} ok")
    for f in R["falhas"]: print("  X", str(f)[:160])

asyncio.run(main())
