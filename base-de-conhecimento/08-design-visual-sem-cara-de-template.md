# 08. Design visual sem cara de template

Estudo feito em 22/09/2026 a partir de 5 skills públicas de design para agentes de IA. As skills foram copiadas para `C:\Users\andre\.claude\skills\` e ficam disponíveis nas próximas sessões do Claude Code.

| Skill | Origem | Serve para LP? | Resumo |
|---|---|---|---|
| `frontend-design` | anthropics/skills | **Sim, é a base** | Método: entender o assunto, planejar tokens, revisar o plano contra o "padrão de IA", construir e depois criticar. |
| `design-taste-frontend` | leonxlnx/taste-skill | **Sim, é o checklist** | Regras "anti-slop" para landing pages: leitura do briefing, 3 "dials", disciplina do hero, proibições e um checklist final. |
| `high-end-visual-design` | leonxlnx/taste-skill | Em parte | Acabamento "de agência cara": moldura dupla nos cartões, botão com ícone encaixado, espaços enormes, movimento com mola. É dogmática demais para usar ao pé da letra. |
| `codebase-design` | mattpocock/skills | Não (é para código) | Vocabulário de módulos "profundos": interface pequena com muito comportamento por trás. Serve para organizar o gerador de orçamento e o modelo, não para o visual. |
| `design-mobile-apps` | designed-by-ai/skills | Não | É um cliente da API paga do Sleek (sleek.design) para telas de app. Precisa de `SLEEK_API_KEY` e plano Pro (US$ 49,99/mês). Não usar em LP. |

---

## O método (juntando as três que valem)

### 1. Ler o briefing antes de desenhar
Escreva uma linha: **"Estou lendo isto como: \<tipo de página> para \<público>, com linguagem \<clima>, puxando para \<família estética>."**
- Quem escolhe a estética é o **público**, não o gosto do designer.
- O que torna o visual único vem do **mundo do cliente**: materiais, vocabulário, objetos e lugares do ramo. Uma LP de mídia em ônibus não pode parecer com a de um SaaS.
- Se o briefing for ambíguo, faça **uma** pergunta só.

### 2. Ajustar os três "dials" (1 a 10)
| Tipo de página | Variação do layout | Movimento | Densidade |
|---|---|---|---|
| LP de serviço local / conversão | 6-7 | 4-5 | 4-5 |
| LP de agência / criativa | 8-9 | 6-8 | 3 |
| Consumo premium | 7 | 6 | 3 |
| Confiança primeiro (saúde, jurídico, governo) | 3-4 | 2-3 | 4-5 |

Movimento acima de 3 obriga a respeitar `prefers-reduced-motion`. Se não der para fazer o movimento bem feito, baixe para 3 e entregue uma página estática limpa.

### 3. Plano de tokens antes do código
- **Cor:** de 4 a 6 hex com nome. **Um único acento**, usado igual na página inteira.
- **Tipo:** uma ou duas famílias. Se forem duas, que sejam bem diferentes.
- **Layout:** uma frase por seção e um rascunho em ASCII. Definir o alinhamento.
- **Princípios:** o que faz esta página ser desta marca.

Depois **revise o plano**: se alguma parte sairia igual para qualquer cliente parecido, troque essa parte e anote o motivo.

### 4. Gastar a ousadia em um lugar só
Escolha **um** elemento memorável e deixe o resto quieto e disciplinado. Antes de sair de casa, tire um acessório (conselho da Chanel citado na skill).

### 5. Construir, tirar print e criticar
Veja em celular e desktop, no modo claro e no escuro, e passe o checklist do fim deste arquivo.

---

## Os "padrões de IA" que denunciam página gerada
Nenhum deles é proibido de verdade. São **escolhas padrão**, e só valem se o briefing pedir.

**Paletas**
- Fundo creme (#F4F1EA) + serifa grande + acento terracota (#D97757).
- Fundo quase preto + um acento verde-limão ou vermelhão.
- Bege, latão, vinho e marrom-café para produto "premium".
- Gradiente roxo/azul "de IA" e brilho neon.

**Tipografia**
- Inter como padrão (também Roboto, Arial, Open Sans). As alternativas citadas são Geist, Outfit, Satoshi, Cabinet Grotesk e Plus Jakarta Sans.
- Serifa só porque parece "criativo". Fraunces e Instrument Serif são as favoritas da IA.
- Uma palavra do título destacada em outra cor ou em itálico.
- Rótulo pequeno em CAIXA ALTA espaçada (o "eyebrow") em cima de toda seção. O limite é **1 a cada 3 seções**.
- Travessão (—) em todo lugar. Uma das skills proíbe por completo. Para nós: usar vírgula, ponto, dois-pontos ou parênteses.
- Separar tudo com ponto médio ("A · B · C") e colocar "→" no fim de todo botão.

**Layout**
- Três cartões iguais lado a lado.
- Todo o conteúdo picado em cartões arredondados iguais, com a mesma sombra cinza.
- Numeração 01 / 02 / 03 quando o conteúdo não é uma sequência de verdade.
- Hero centralizado sobre um fundo escuro com mancha de gradiente e sem imagem real.
- Mais de 2 seções seguidas no esquema "imagem de um lado, texto do outro" em zigue-zague.
- Título grande à esquerda com um parágrafo pequeno flutuando à direita.
- "Painel de produto" falso desenhado com divs.

**Texto**
- Verbos de enchimento como "eleve", "revolucione", "potencialize", "sem esforço".
- Números inventados com cara de precisos. (Isso já é regra nossa: nunca inventar número nem depoimento.)
- "Role para explorar", faixas de cidade, hora e clima, e selos "BETA".

## Regras de disciplina que adotamos
- **O hero cabe na primeira tela:** título de até 2 linhas, subtítulo de até 20 palavras, botão visível sem rolar e no máximo 4 elementos de texto. Logos de clientes e prova social ficam **abaixo** do hero.
- **Uma intenção por botão:** se o botão de contato se chama "Pedir proposta", ele tem esse mesmo nome no menu, no hero e no rodapé. Nada de "Fale conosco" em um lugar e "Vamos conversar" em outro.
- O texto do botão não quebra linha no desktop e tem no máximo 3 palavras.
- **Uma família de cantos:** tudo reto, tudo 12-16px ou botão em pílula com cartões de 16px. A regra vale para a página toda.
- **Um tema por página:** nenhuma seção muda de claro para escuro no meio. Oferecer modo escuro pelo `prefers-color-scheme`.
- Nenhum layout de seção se repete. Uma LP de 8 seções usa pelo menos 4 formatos diferentes.
- Mais de 5 itens pedem outro componente: abas, acordeão, carrossel ou grade com imagem. Nada de lista longa com linha embaixo de cada item.
- **Imagens reais são obrigatórias.** Página só com texto está incompleta. Quando o cliente ainda não mandou fotos, deixar espaços marcados (`<!-- FOTO: campanha busdoor, 1600x1000 -->`) e pedir as fotos.
- Formulário: rótulo em cima do campo e erro embaixo. O placeholder nunca faz o papel de rótulo. Contraste AA em tudo.
- Movimento: um único momento orquestrado (a entrada do hero, por exemplo) funciona melhor que animação em toda seção. Animar só `transform` e `opacity`. Usar IntersectionObserver e nunca um listener de `scroll`. Usar `min-height: 100dvh` e nunca `100vh`.

## O que aproveitar da `high-end-visual-design` (com moderação)
- **Moldura dupla:** cartão importante dentro de uma "bandeja" com 6-8px de respiro e cantos concêntricos (raio interno = raio externo - respiro). Usar só nos 1 ou 2 blocos de destaque, não em todos.
- **Botão com o ícone dentro de um círculo próprio**, que se desloca levemente no hover.
- Curvas de movimento personalizadas, como `cubic-bezier(0.16, 1, 0.3, 1)` ou `(0.32, 0.72, 0, 1)`.
- `backdrop-filter` só em elemento fixo (menu). Textura de ruído só em pseudo-elemento fixo com `pointer-events: none`.
- **Não seguir:** "eyebrow em cima de todo título" (contradiz as outras duas), "toda seção com 96-160px de respiro" (ruim no celular e em LP de conversão) e "nada aparece sem animação" (prejudica o LCP e a acessibilidade).

## Onde as skills discordam (e o que decidimos)
| Tema | Conflito | Decisão |
|---|---|---|
| Eyebrow | high-end manda usar em todos, as outras limitam | No máximo 1 a cada 3 seções |
| Stack | taste-skill manda React/Next + Tailwind + Motion | Para LP de cliente pequeno: HTML/CSS/JS puro como o `modelo/`, que é mais leve, mais barato de hospedar e bom de LCP. React só em projeto maior |
| Fontes | taste-skill não quer `<link>` do Google Fonts | Hospedar a fonte junto (`@font-face` + `font-display: swap`) quando der |
| Ícones | taste-skill proíbe SVG feito à mão | Usar Phosphor ou Tabler (um só conjunto, espessura de traço fixa) |
| Movimento | high-end quer tudo animado | Dial de movimento 4-5 para LP de conversão |

## Checklist visual rápido (antes de mostrar ao cliente)
- [ ] A frase de leitura do briefing e os dials foram escritos
- [ ] Paleta de 4 a 6 cores com um único acento, sem nenhuma das paletas padrão de IA
- [ ] Fonte escolhida por um motivo (não é Inter por padrão) e sem destacar uma palavra só do título
- [ ] O hero cabe na tela (2 linhas + 20 palavras + botão) no celular e no desktop
- [ ] Um nome por intenção de botão e nenhum botão quebrando linha
- [ ] No máximo 1 eyebrow a cada 3 seções, sem numeração falsa e sem travessão
- [ ] Nenhum layout de seção repetido e no máximo 2 zigue-zagues seguidos
- [ ] Imagens reais ou espaços marcados, sem painel falso
- [ ] Uma família de cantos e um tema, testado no claro e no escuro
- [ ] Contraste AA em botões, campos e textos de ajuda
- [ ] Movimento com motivo, respeitando reduced-motion, animando só transform e opacity
- [ ] Todo texto relido em voz alta: nada com cara de IA e nenhum número inventado
