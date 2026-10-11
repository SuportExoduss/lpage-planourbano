# Aplica trocas exatas num arquivo: python testes/edita.py arquivo trocas.py  (trocas = lista de (antes, depois))
import sys, pathlib, runpy
arq = pathlib.Path(sys.argv[1]); s = arq.read_text(encoding="utf-8")
for antes, depois in runpy.run_path(sys.argv[2])["TROCAS"]:
    n = s.count(antes)
    assert n == 1, f"esperava 1 ocorrência, achei {n}: {antes[:70]!r}"
    s = s.replace(antes, depois)
arq.write_bytes(s.encode("utf-8"))
print("ok", arq.name)
