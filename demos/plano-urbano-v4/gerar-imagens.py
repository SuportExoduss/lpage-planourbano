# Gera a imagem de compartilhamento (Open Graph) e os ícones a partir da marca. Rodar só quando a marca mudar.
import asyncio, pathlib, base64
from playwright.async_api import async_playwright
d = pathlib.Path(__file__).parent
logo = (d/'logo.svg').read_text(encoding='utf-8')
simb = (d/'simbolo.svg').read_text(encoding='utf-8')
foto = 'data:image/webp;base64,' + base64.b64encode((d/'img/topo-plano-urbano.webp').read_bytes()).decode()   # ônibus real da Plano Urbano
FONTES = '<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@800;900&family=Rubik:wght@500&display=swap" rel="stylesheet">'
OG = f'''<html><head>{FONTES}<style>
body{{margin:0;width:1200px;height:630px;background:#2F2E2E;color:#fff;font-family:Rubik;display:grid;grid-template-columns:640px 1fr;overflow:hidden}}
.txt{{padding:64px 0 56px 64px;display:flex;flex-direction:column}}
.logo{{width:230px;color:#fff}} .logo svg{{width:100%;height:auto;display:block}}
h1{{font:900 58px/1.02 Unbounded;text-transform:uppercase;margin:auto 0 0;letter-spacing:-.01em}}
h1 span{{display:inline-block;white-space:nowrap;background:#E9AC00;color:#2F2E2E;padding:4px 14px 8px;margin-top:10px;transform:rotate(-2deg)}}
p{{font-size:26px;margin:30px 0 0;color:#ACABAB}}
.foto{{background:url({foto}) 50% 40%/cover;border-radius:40px 0 0 40px;margin:40px 0}}
</style></head><body><div class="txt"><div class="logo">{logo}</div>
<h1>A cidade é<br><span>seu público.</span></h1><p>Busdoor, backbus e ônibus envelopado em todo o Brasil.</p></div><div class="foto"></div></body></html>'''
def icone(tam, fundo, pad):
    s = simb.replace('currentColor', '#E9AC00')
    return f'<html><body style="margin:0;width:{tam}px;height:{tam}px;background:{fundo};display:grid;place-items:center"><div style="width:{tam-2*pad}px">{s}</div></body></html>'.replace('<svg ', '<svg style="width:100%;height:auto;display:block" ', 1)
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="msedge")
        for nome, html, w, h, tipo in [('img/compartilhar.jpg', OG, 1200, 630, 'jpeg'),
                                       ('apple-touch-icon.png', icone(180, '#2F2E2E', 30), 180, 180, 'png'),
                                       ('favicon.png', icone(96, 'transparent', 4), 96, 96, 'png')]:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            await pg.set_content(html, wait_until='networkidle'); await pg.wait_for_timeout(300)
            opts = {'path': str(d/nome), 'type': tipo, 'omit_background': tipo == 'png'}
            if tipo == 'jpeg': opts['quality'] = 82
            await pg.screenshot(**opts); await pg.close()
            print(nome, (d/nome).stat().st_size, 'bytes')
        await b.close()
asyncio.run(main())
