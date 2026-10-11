# Roadmap: correções da varredura 2

Mesmo método da rodada 1: um item por vez → corrigir → comparar com a versão anterior → testar o impacto → bateria → próximo.
**Bateria ampliada:** `testes/regressao.py`, de 25 para **40 verificações** (axe-core em desktop e celular, CSS das 3 páginas, +55, DDD, limites, Esc, sem JS, alto contraste, fontes locais, URLs). **Base no site oficial: 27/40.**

## Ordem (com dependências)

| # | Item | Achado | Por que nesta ordem |
|---|---|---|---|
| C1 | Chaves sobrando + CSS sem uso | V3 | Limpa a base: os itens seguintes mexem no CSS |
| C2 | WhatsApp com +55 | V1 | Mesma função de formatação que C3 |
| C3 | DDD inválido | V6 | Depende de C2 |
| C4 | Limite de tamanho dos campos | V15 | Formulário, independente |
| C5 | Esc fecha o menu | V9 | Independente |
| C6 | WhatsApp sem JavaScript | V7 | O build grava o link; o JS continua acrescentando a origem (UTM) |
| C7 | Link da agenda sem `href` desativado | V12 | Mesmo padrão de link que C6 |
| C8 | Carrossel de formatos pelo teclado | V4 | Mesmo elemento (`.grade`) que C9 |
| C9 | Papéis ARIA nos `div` com `aria-label` | V10 | Depois de C8 |
| C10 | Botão flutuante e barra em `<aside>` | V11 | Mexe no fim da página; C11 é vizinho |
| C11 | Seção sem título → `div` | V13 | Conferir se o CSS dependia de `section` |
| C12 | Contraste dos dias da semana | V5 | CSS do calendário |
| C13 | Contorno dos botões no alto contraste | V8 | CSS dos botões |
| C14 | `-webkit-mask` | V14 | CSS do simulador |
| C15 | `/privacidade/` e `/favicon.ico` | V16 | `firebase.json` |
| C16 | Fontes no próprio site + pré-carga | V2 | **Por último:** muda a CSP (`font-src`/`style-src`) das 3 páginas; medir antes/depois em 4G lenta |

## Depois
1. Varredura 1 completa (regressão, 11 larguras, links, textos proibidos, imagens, botões, interação).
2. Varredura 2 completa (W3C, axe, desempenho em 4G lenta, sem JS, alto contraste, teclado, formulário, URLs/DNS), feita no **canal de pré-visualização**, porque o W3C precisa de um endereço público.
3. Se tudo estiver ok, publicar no site oficial e repetir a bateria lá.

## Registro de execução
| Rodada | Item | Bateria | O que mudou | Regressão |
|---|---|---|---|---|
| 40 | Base (site oficial) | 27/40 | — | — |
| 41 | Base local | 27/40 | (mesma do site oficial) | — |
| 42 | C1 Chaves sobrando + CSS sem uso | 28/40 | 2 `}` removidas; `.pista`, `@keyframes corre`, `.revela`, `.ajuda` apagados. **Diferença visual 0,00%** | Nenhuma |
| 43 | C2+C3 Telefone (+55 e DDD) | 30/40 | Tira +55 e 0 de discagem; valida contra os 67 DDDs reais; celular de 11 dígitos precisa começar com 9. **Matriz de 24 casos (digitados e colados): 24/24** | Nenhuma |
| 44 | C4 Limites de tamanho | 31/40 | maxlength em 6 campos (o simulador já tinha). Matriz de telefones continua 24/24 | Nenhuma |
| 45 | C5 Esc fecha o menu | 32/40 | Esc fecha e devolve o foco ao botão | Nenhuma |
| 46 | C6 WhatsApp sem JS | 33/40 | O build grava o link real (número e mensagem lidos do CFG); o JS continua acrescentando a origem. Diferença visual: só o dia 7 (hoje) desativado porque o horário passou, o que é correto | Nenhuma |
| 47 | C7 Agenda | 34/40 | Sem `href` enquanto desativado (`role="link"`); escolher dia e horário continua gerando o link | Nenhuma |
| 48 | C8+C9 Carrossel + papéis ARIA | 34/40 | `.grade` com `role="region"` e `tabindex="0"`; mosaico com `role="group"`. Sumiu o "scrollable-region-focusable" do axe | Nenhuma |
| 49 | C10 `<aside>` | 34/40 | Botão flutuante e barra numa região "Contato rápido"; sumiu o "region" do axe | Nenhuma |
| 50 | C11 Seção → div | 34/40 | As regras de `section` foram estendidas à `.faixa-cta`; alturas idênticas medidas (uma diferença inicial veio da fonte do Google não carregar com a internet instável; a nova captura deu 0,00%) | Nenhuma |
| 51 | C12 Contraste dos dias | 36/40 | Opacidade 0,75 → 0,85 (4,0 → 4,97:1). **axe: zero violações** no desktop e no celular | Nenhuma |
| 52 | C13 Alto contraste | 37/40 | Contorno nos botões só em `forced-colors` (conferido na captura); modo normal 0,00% | Nenhuma |
| — | C14 `-webkit-mask` | — | **Falso positivo**: as 5 máscaras já têm o prefixo; o validador do W3C é que não reconhece a sintaxe sem prefixo. Sem mudança | — |
| 53 | C15 URLs | 39/40 | `trailingSlash:false` + `/favicon.ico` → `/favicon.png` (conferido na pré-visualização; o emulador local não aplica redirecionamentos) | Nenhuma |
| 54 | C16 Fontes no próprio site | **40/40** | As fontes do Google eram variáveis: 6 arquivos → **3** (`/fonts/`, cache de 1 ano), pré-carga das 2 principais, CSP sem domínios externos. **4G lenta (mediana): primeira pintura 4,2 → 3,4 s, conteúdo principal 5,2 → 3,8 s.** Diferença visual 0,11–0,34% (só suavização das letras) | Nenhuma |

## Varreduras finais e publicação
| Etapa | Onde | Resultado |
|---|---|---|
| Varredura 1 completa | Pré-visualização | 11 larguras sem rolagem lateral e sem nada cortado · botões cabendo de 320 a 1440 · links 200 · todas as imagens carregam (a do carrossel do celular, quando a pessoa desliza) · interação completa ok · zero erros de JS · nenhum texto proibido (a verificação passou a usar palavra inteira; o "a gente" achado estava dentro de "muit**a gente**", num comentário de código) |
| Varredura 2 completa | Pré-visualização | W3C: privacidade **0**, 404 **0**, página inicial só o falso positivo do `mask` · axe **0** violações (desktop e celular) · teclado ok, Esc fecha o menu · telefones 24/24 · sem JS: WhatsApp funciona · alto contraste: botões com contorno · 4G lenta: 3,4 s / 3,8 s |
| **Publicado** | Site oficial | **40/40** (antes 27/40), 11 larguras ok, W3C igual à pré-visualização, CSP sem domínios externos, arquivos internos dão 404 |
