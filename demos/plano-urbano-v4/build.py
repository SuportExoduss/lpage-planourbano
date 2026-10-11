# Monta index.html a partir de src.html, embutindo o logo e o símbolo extraídos do brandbook.
# Cada build ganha um número de versão: as imagens vão com ?v=versão (o navegador baixa de novo).
# Também gera plano-urbano-visualizar.html (arquivo único, imagens embutidas) para mandar ao cliente.
import re, urllib.parse, pathlib, time, base64
d = pathlib.Path(__file__).parent
versao = time.strftime('%Y%m%d%H%M%S')
logo = (d/'logo.svg').read_text(encoding='utf-8').replace('<svg ', '<svg role="img" aria-hidden="true" ', 1)
simb = (d/'simbolo.svg').read_text(encoding='utf-8')
paths = ''.join(re.findall(r'<path[^>]*/>', simb))
q = lambda s: urllib.parse.quote(s, safe=' =:/"-.,')
seta = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 11L11 3M5 3h6v6"/></svg>'
fontes = (d/'src-fontes.html').read_text(encoding='utf-8').strip()   # mesmo bloco de fontes nas 3 páginas
html = (d/'src.html').read_text(encoding='utf-8')
html = html.replace('%FONTES%', fontes)
# link do WhatsApp já no HTML (funciona sem JavaScript); número e mensagem vêm do CFG do próprio site
_num = re.search(r'whatsapp: "(\d+)"', html).group(1); _msg = re.search(r'msg: "([^"]+)"', html).group(1)
html = html.replace('%WA%', f'https://wa.me/{_num}?text=' + urllib.parse.quote(_msg))
html = (html.replace('%LOGO%', logo).replace('%SETA%', seta)
  .replace('%SIMBOLO_MASK%', q(simb.replace('currentColor', '#000')).replace('"', "'"))
  .replace('%SIMBOLO_PATHS%', paths)
  .replace('%VERSAO%', versao))
html = re.sub(r'<!--.*?-->\n?', '', html, flags=re.S)   # anotações internas não vão para o site
IMG = r'(img/[\w.-]+\.(?:webp|jpg))'

site = re.sub(IMG, r'\1?v=' + versao, html)
(d/'index.html').write_text(site, encoding='utf-8')

def embute(m):
    f = m.group(1)
    tipo = 'image/webp' if f.endswith('.webp') else 'image/jpeg'
    return f'data:{tipo};base64,' + base64.b64encode((d/f).read_bytes()).decode()
visual = re.sub(IMG, embute, html).replace('href="/privacidade"', 'href="#"')
(d/'plano-urbano-visualizar.html').write_text(visual, encoding='utf-8')
print('ok', versao, len(site))

# política de privacidade: mesma marca, sem anotações internas
priv = (d/'src-privacidade.html').read_text(encoding='utf-8').replace('%LOGO%', logo).replace('%FONTES%', fontes)
(d/'privacidade.html').write_text(re.sub(r'<!--.*?-->\n?', '', priv, flags=re.S), encoding='utf-8')

# página 404 com a marca (o Firebase usa o 404.html sozinho)
(d/'404.html').write_text((d/'src-404.html').read_text(encoding='utf-8').replace('%LOGO%', logo).replace('%FONTES%', fontes), encoding='utf-8')
