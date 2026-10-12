# Plano Urbano OOH: landing page

Site no ar: https://www.agenciaplanourbano.com.br

**O site atual é a pasta `demos/plano-urbano-v4/`. Não há outra versão neste repositório.**

## Arquivos
| Arquivo | O que é |
|---|---|
| `src.html` | **Fonte da página inicial** (HTML, CSS e JS num arquivo só). Edite aqui. |
| `src-privacidade.html` | Fonte da Política de Privacidade |
| `src-404.html` | Fonte da página de erro 404 |
| `src-fontes.html` | Trecho comum do `<head>` das 3 páginas (fontes locais e redirecionamento dos endereços do Firebase) |
| `build.py` | Monta as páginas finais a partir dos `src-*` (embute o logo, versiona as imagens) |
| `index.html`, `privacidade.html`, `404.html` | **Gerados pelo `build.py`.** Não edite à mão: o próximo build apaga a mudança |
| `logo.svg`, `simbolo.svg` | Logo e símbolo oficiais (do brandbook) |
| `img/`, `fonts/` | Imagens (WebP) e fontes Unbounded + Rubik hospedadas no próprio site |
| `firebase.json` | Hospedagem (Firebase Hosting): cabeçalhos de segurança, cache e redirecionamentos |
| `gerar-imagens.py` | Gera a imagem de compartilhamento e os ícones |
| `testes/regressao.py` | Bateria de testes (Playwright): `python testes/regressao.py <url> <rodada>` |

## Publicar
```bash
cd demos/plano-urbano-v4
python build.py
firebase deploy --only hosting --project planourbano
```

## Regras da marca
Cores do brandbook (Mostarda #E9AC00, Abóbora #F06101, Índigo #5757C1, Asfalto #2F2E2E, branco), fontes Unbounded (títulos, caixa alta) + Rubik (texto), assinatura "A cidade é seu público.", tom profissional e nacional.
Conversão só pelo WhatsApp (sem banco de dados); sem medição de visitas por enquanto.
