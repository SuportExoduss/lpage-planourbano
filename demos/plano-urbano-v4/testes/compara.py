# Compara duas rodadas: python testes/compara.py antes depois
import json, sys, pathlib
d = pathlib.Path(__file__).parent / "resultados"
a, b = (json.loads((d / f"{n}.json").read_text(encoding="utf-8")) for n in sys.argv[1:3])
ck = lambda r: {k: v["ok"] for k, v in r.items() if isinstance(v, dict) and "ok" in v}
ca, cb = ck(a), ck(b)
print(f"{sys.argv[1]} {sum(ca.values())}/{len(ca)}  ->  {sys.argv[2]} {sum(cb.values())}/{len(cb)}")
for k in cb:
    if ca.get(k) != cb[k]: print(("  + corrigiu " if cb[k] else "  - REGREDIU ") + k)
if a["contraste"]["info"] != b["contraste"]["info"]: print("  contraste:", a["contraste"]["info"], "->", b["contraste"]["info"])
print("  métricas:", a["metricas"], "->", b["metricas"])
if not any(ca.get(k) and not cb[k] for k in cb): print("  sem regressão")
