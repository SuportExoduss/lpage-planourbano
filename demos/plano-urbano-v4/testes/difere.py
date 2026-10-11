# Diferença visual entre duas rodadas: python testes/difere.py antes depois [desk|mob]
# Congela animações e compara as capturas; grava resultados/dif_<depois>_<tela>.png com as mudanças em vermelho.
import sys, pathlib
from PIL import Image, ImageChops
d = pathlib.Path(__file__).parent / "resultados"
a, b, tela = sys.argv[1], sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "desk")
A = Image.open(d / f"{a}_{tela}.png").convert("RGB"); B = Image.open(d / f"{b}_{tela}.png").convert("RGB")
if A.size != B.size:
    print(f"{tela}: tamanho mudou {A.size} -> {B.size}"); h = min(A.height, B.height); A = A.crop((0, 0, A.width, h)); B = B.crop((0, 0, B.width, h))
diff = ImageChops.difference(A, B).convert("L").point(lambda v: 255 if v > 40 else 0)
n = diff.histogram()[255]; tot = A.width * A.height
caixa = diff.getbbox()
print(f"{tela}: {100*n/tot:.2f}% dos pixels mudaram; região: {caixa}")
if n:
    over = B.copy(); over.paste((255, 0, 0), mask=diff); over.save(d / f"dif_{b}_{tela}.png")
