# Desempenho em celular de entrada (4G lenta 1,6 Mbps / 150 ms, CPU 4x), cache vazio. Mediana de N rodadas.
# python testes/desempenho.py <url> [rodadas]
import asyncio, sys, statistics
from playwright.async_api import async_playwright
U = sys.argv[1]; N = int(sys.argv[2]) if len(sys.argv) > 2 else 3
OBS = """window.__m={tbt:0};new PerformanceObserver(l=>{for(const e of l.getEntries()) __m.lcp=Math.round(e.startTime)}).observe({type:'largest-contentful-paint',buffered:true});
new PerformanceObserver(l=>{for(const e of l.getEntries()) if(e.name==='first-contentful-paint') __m.fcp=Math.round(e.startTime)}).observe({type:'paint',buffered:true});
new PerformanceObserver(l=>{for(const e of l.getEntries()) __m.tbt+=Math.max(0,e.duration-50)}).observe({type:'longtask',buffered:true});"""
async def uma(b, i):
    c = await b.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True); pg = await c.new_page(); s = await c.new_cdp_session(pg)
    await s.send("Network.enable"); await s.send("Network.setCacheDisabled", {"cacheDisabled": True})
    await s.send("Network.emulateNetworkConditions", {"offline": False, "latency": 150, "downloadThroughput": 1.6e6/8, "uploadThroughput": 750e3/8})
    await s.send("Emulation.setCPUThrottlingRate", {"rate": 4}); await pg.add_init_script(OBS)
    await pg.goto(f"{U}?perf={i}", wait_until="load"); await pg.wait_for_timeout(3500)
    m = await pg.evaluate("__m"); m["tbt"] = round(m["tbt"])
    m["kb"] = round(await pg.evaluate("performance.getEntriesByType('resource').reduce((a,r)=>a+r.transferSize,0)+performance.getEntriesByType('navigation')[0].transferSize") / 1024)
    m["layouts_fontes"] = await pg.evaluate("document.fonts.size")
    await c.close(); return m
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="msedge"); rs = [await uma(b, i) for i in range(N)]; await b.close()
    med = {k: statistics.median([r[k] for r in rs if k in r]) for k in ("fcp", "lcp", "tbt", "kb")}
    print("rodadas:", rs); print("MEDIANA:", med)
asyncio.run(main())
