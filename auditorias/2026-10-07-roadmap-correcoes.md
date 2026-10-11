# Roadmap de correções: www.agenciaplanourbano.com.br

Baseado na auditoria de 07/10/2026.
**Método por item:** pesquisar → listar as necessidades (cruzando com os outros itens) → corrigir → comparar com a versão anterior → testar o impacto → bateria de regressão → próximo item.
**Bateria:** `testes/regressao.py`, com 25 verificações em desktop, celular, 404, privacidade e movimento reduzido. **Base antes das correções: 11/25.**

## Ordem e dependências

| # | Correção | Item da auditoria | Depende de / afeta |
|---|---|---|---|
| F1 | Tirar a faixa e a nota de "Demonstração" | 2.1 | — |
| F2 | Tirar os marcadores `[ ]` (rodapé com os dados reais; duração e "Também atuamos" saem até o dono confirmar) | 2.2 | Nada pode ser inventado: o que não foi confirmado sai |
| F3 | Sede em Niterói | 2.3 | F11 (endereço no JSON-LD) |
| F4 | Mensagem do WhatsApp completa (preferência de contato, simulador, origem) | 2.4 | F8 (a privacidade cita a origem/UTM) |
| F5 | Remover a recarga automática por versão | 3.8 | build.py continua com `?v=` nas imagens, necessário para F15 |
| F6 | No computador: botão "Copiar pedido" e número da agência na tela final | 2.5 | F4 (usa o mesmo texto) |
| F7 | Agenda com texto honesto ("sugira um horário") | 3.4 | — |
| F8 | Privacidade igual ao que o site faz + cabeçalho com logo | 3.7, 4.13 | F4 |
| F9 | Prévia de compartilhamento (Open Graph + imagem 1200×630) | 3.1 | F10/F11 (mesma identidade), F15 (cache) |
| F10 | Favicon em arquivo + ícone do iPhone | 4.2 | firebase.json ignora `*.svg` → usar PNG |
| F11 | Dados estruturados (Organization, JSON-LD) | 4.3 | F3, F9, F10 |
| F12 | Página 404 com a marca | 3.6 | F20 (CSP) |
| F13 | Botão flutuante reconhecível como WhatsApp | 4.1 | Paleta só do brandbook |
| F14 | Imagem do topo em WebP | 4.4 | preload, F15 |
| F15 | Cache longo para imagens versionadas | 4.5 | F5, F9, F10, F14 |
| F16 | Imagem escura de "A rua é sua vitrine" | 4.6 | — |
| F17 | E-mail quebrando no rodapé | 4.7 | — |
| F18 | Contraste do rótulo "Sua marca" | 4.8 | Paleta só do brandbook |
| F19 | Tirar pesos de fonte não usados | 4.10 | — |
| F20 | Cabeçalhos de segurança (CSP, Permissions-Policy, frame-ancestors) | 4.11 | **Por último:** precisa liberar tudo o que F1–F19 usam |
| F21 | Títulos do rodapé (h4 → h2) | baixo | — |

## Fora do código: dependem do dono ou de você
| Item | O que falta |
|---|---|
| 3.2 Prova social | Clientes, fotos de campanhas reais, números |
| 3.3 Cidades do topo | Confirmar a lista das 25 |
| 2.2 Duração da conversa / outros serviços | Confirmar para voltar ao site |
| Opção "Ligação" | Manter (agora vai na mensagem) ou tirar |
| 3.5 DKIM + 4.12 DMARC | Depois que o Workspace passar para o Google |
| 4.9 Search Console | Você, com o acesso |

## Registro de execução
(preenchido a cada item: antes → depois, teste, regressão)

| Rodada | Correção | Testes | O que mudou | Regressão |
|---|---|---|---|---|
| 00 | Base (antes) | 11/25 | — | — |
| 01 | F1 Faixa "Demonstração" | 12/25 | Saíram a faixa do topo, a nota do rodapé e o CSS | Nenhuma |
| 02 | F2 Marcadores `[ ]` | 15/25 | Rodapé com razão social e CNPJ; duração e "Também atuamos" removidos. **A bateria achou um 7º marcador escondido na etapa 3** ("Faixas de exemplo"), também removido. O build passou a apagar as anotações internas (`<!-- CONFIRMAR… -->`) do código publicado | Nenhuma |
| 03 | F3 Sede em Niterói | 16/25 | Rodapé corrigido | Nenhuma |
| 04 | F4 Mensagem do WhatsApp | 19/25 | Agora leva a preferência de contato, o simulador e a origem (UTM), com rótulos iguais aos do formulário | Nenhuma |
| 05 | F5 Recarga por versão | 20/25 | O código e a meta "versao" saíram; a página não se baixa mais de novo | Nenhuma |
| 06 | F6 Envio pelo computador | 20/25 | "Copie o pedido" + número na tela final (testado: copia o texto completo) | Nenhuma |
| 07 | F7 Agenda honesta | 20/25 | "Sugira um horário", "Enviar sugestão pelo WhatsApp" e a mensagem pergunta se o horário funciona | Nenhuma |
| 08 | F8 Privacidade | 21/25 | Reescrita conforme o que o site faz (WhatsApp, sem cookies), logo no topo e gerada pelo build; links sem o redirecionamento `.html` | Nenhuma |
| 09 | F9–F11 Compartilhamento, ícones, JSON-LD | 24/25 | Imagem 1200×630 (80 KB) gerada com a marca; favicon.png e apple-touch-icon; AdvertisingAgency com CNPJ e endereço | Nenhuma |
| 10 | F12 Página 404 | 25/25 | 404 com a marca, botão de início e WhatsApp, noindex ("fale conosco", sem "a gente") | Nenhuma |
| 11 | F13 Botão flutuante | 25/25 | Ícone de balão de conversa com telefone, nas cores da marca | Nenhuma |
| 12 | F14 Imagem do topo | 25/25 | onibus.jpg 151 KB → onibus.webp 39 KB (720 px, o bastante para 2× no maior tamanho exibido, 348 px). Página: 275 → 163 KB. Comparação visual 2× idêntica | Nenhuma |
| 13 | F15 Cache | 25/25 | Imagens com 1 ano + immutable, ícones com 1 semana (conferido no canal de pré-visualização) | Nenhuma |
| 14 | F16 Imagem escura | 25/25 | Níveis ajustados preservando o tom (brilho 49 → 108); a primeira tentativa (autocontraste) gerou tom azul e foi descartada | Nenhuma |
| 15 | F17 E-mail no rodapé | 25/25 | `<wbr>` depois do @ | Nenhuma |
| 16 | F18 Contraste | 25/25 | Rótulos do simulador em Mostarda 40% (3,0 → 4,58:1). Lista de contraste baixo: vazia | Nenhuma |
| 17 | F19 Fontes | 25/25 | Unbounded só com os pesos 800/900 (os únicos usados, conferido) | Nenhuma |
| 18 | F21 Títulos do rodapé | 25/25 | h4 → h2, visual idêntico | Nenhuma |
| 19 | F20 Cabeçalhos de segurança | 25/25 | CSP + Permissions-Policy + frame-ancestors; zero violações nas 3 páginas (pré-visualização) | Nenhuma |
| 21 | **F22 (achado na varredura final)** | 25/25 | No desktop a página rolava de 16 a 52 px para o lado (faixa inclinada) → `main{overflow-x:clip}`. Isso revelou outro defeito antigo: em 320 px o botão principal vazava, e o celular ampliava a página para 348 px → texto do botão quebra abaixo de 380 px | Nenhuma |
| 22 | **Produção, varredura final** | **25/25** | 11 larguras de tela (320 a 2560) sem rolagem lateral e sem nada cortado; links ok; nenhum texto proibido; redirecionamentos, sitemap, robots, OG, JSON-LD e DNS ok | — |
