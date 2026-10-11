# Análise da varredura do ChatGPT (feita só de fora)

**Observação:** os dois arquivos enviados (`analise v1 chat gpt.txt` e `analise codigo v1 chat gpt.txt`) são **idênticos**. Não veio um roadmap separado. Analisei o texto único e **conferi cada afirmação no código e no site atual**.

Legenda: ✅ concordo e dá para fazer já · 🟡 concordo, mas depende do dono (dados reais) · ☑️ já foi feito · ❌ discordo / não se aplica

---

## 1. O que ele elogia (manter): concordo com tudo
✅ "A cidade é seu público" como assinatura · ✅ a pergunta "E a sua marca, está em cartaz?" · ✅ formulário em 3 etapas como qualificador · ✅ simulador como diferencial · ✅ WhatsApp no centro · ✅ **não refazer o site; acrescentar uma camada de autoridade**. Bate com a nossa leitura.

## 2. Ponto a ponto

| § | O que ele diz | Marca | Por quê (conferido) |
|---|---|---|---|
| 5–6 | "Maiores cidades do Brasil" promete mais do que prova. E o **LinkedIn do Fábio fala em concessão em garagens de ônibus no estado do RJ**, com plano de expansão | 🟡 **concordo, é o achado mais valioso dele** | Já estava na nossa lista ("confirmar as 25 cidades"), mas o LinkedIn reforça: o inventário próprio pode ser só do RJ. O texto precisa dizer a verdade (próprio no RJ + parceiros nas outras praças?). **Decisão do dono** |
| 7–9 | Falta prova: cases, fotos reais, clientes, números | 🟡 concordo | Também era nosso item nº 1 de conversão. Só sai com material real da agência |
| 10 | Transformar CNPJ e endereço num bloco de confiança | ✅ concordo (leve) | Dá para fazer com os dados que já temos |
| 11 | Placeholders `[Razão social]` e "Demonstração da Trevo" | ☑️ já feito | Ele viu uma cópia antiga do Google. Hoje a bateria bloqueia isso em todas as publicações |
| 12 | **Contradição dos cookies**: a página diz "Usamos cookies para medir…" e a política diz que não usa | ✅ **concordo, é real** | O aviso fica **escondido** (só aparece se houver medição), mas **o texto está no HTML**, e o Google e o ChatGPT o leem. Conferido no site oficial |
| 13 | Avisar perto do botão que os dados **não são enviados automaticamente** | ✅ concordo | Barato e aumenta a confiança |
| 15 | "Investimento previsto" assusta; usar "Faixa de investimento" + "Ainda estou avaliando" | ✅ rótulo / 🟡 faixas | A troca de texto é simples; as faixas em si seguem pendentes com o dono |
| 17 | Simulador com fechamento "Gostou de ver sua marca na rua?" | ✅ concordo (leve) | Ajuste de texto em volta do botão |
| 18 | Simulador perguntando a cidade | 🟡 depois | Depende da lista real de cidades |
| 19 | Formatos com "quando usar" | ✅ parcial | Envelopado e Busdoor já dizem "indicado para"; **Backbus não**. Completo |
| 20 | Mini consultor "qual formato escolher" | 🟡 futuro | Funcionalidade nova; vale depois da prova social |
| 21 | Frase do letreiro repetida | ✅ concordo (técnico) | A repetição é visual (a faixa rola em loop), mas o texto está **2× no HTML**. Deixo 1× e duplico só na tela |
| 22–23 | Mais "mundo real": fotos reais da operação | 🟡 concordo | Material da agência |
| 24–25 | Posição: OOH próximo e consultivo, sem competir em escala com a Eletromidia | ✅ concordo | Combina com o que o dono contou (estuda o nicho e cria junto) |
| 26–27 | Agenda: chamar de "sugerir horário" | ✅ parcial | O conteúdo já foi corrigido (F7), mas o **menu, o rodapé e o título** ainda dizem "Agendar conversa". "15 minutos" depende do dono |
| 28 | Mostrar como o pedido vai ficar antes de abrir o WhatsApp | ✅ concordo | Resumo do pedido na etapa 3 |
| 29 | UTM completo (content e term) na mensagem | ✅ **concordo, é real** | O site **captura** os 5, mas a mensagem só leva 3 (source, medium e campaign). Conferido no código |
| 30–32 | Páginas de SEO por formato e cidade | 🟡 concordo, depois | Ele mesmo diz: "só onde existe operação". Depende das cidades e de conteúdo real |
| 33 | SEO local: Perfil da Empresa no Google, nome igual em tudo | 🟡 concordo | Ação do dono/sua, fora do código |
| 34 | "Por trás da Plano Urbano" (foto e nome do Fábio) | 🟡 concordo | Precisa da foto e da autorização dele |
| 35–37 | "Por que Plano Urbano" / "Planejamos onde sua marca encontra a cidade" | 🟡 texto para o dono aprovar | A ideia é boa. A frase "encontra **ele**" está errada (o certo é "o encontra") |
| 38 | Auditoria de acessibilidade | ☑️ já feito | axe-core zerado, teclado, contraste, alto contraste |
| 39 | Mensagens de erro específicas e obrigatórios claros | ☑️ erros / ✅ obrigatórios | Os erros já são específicos ("Informe um WhatsApp válido, com DDD."). Mas **nada indica quais campos são opcionais**. Isso eu faço |
| 40–41 | CTA fixo no celular | ☑️ **já existe** | A barra "Solicitar orçamento \| WhatsApp" aparece ao rolar. Ele não viu porque não navega |
| 42 | Desempenho: imagens, fontes, CLS | ☑️ já feito | WebP, fontes locais, CLS 0,006 |
| 43 | Banner de cookies gerando CLS | ❌ não se aplica | O banner nem aparece (sem medição) |
| 44 | Cabeçalhos de segurança e regras do Firebase | ☑️ / ❌ | Os cabeçalhos estão feitos. **Não há Firestore, Storage nem chaves de API** no site |
| 45 | Checagens do WhatsApp | ☑️ já feito | Bateria de 40 testes, 24 casos de telefone |
| 46 | Rodapé com "Operação", "Empresa", "Termos" | 🟡 / ❌ | "Operação" e "Cases" dependem do conteúdo. **"Termos" não faz sentido** (não há contrato nem conta no site) |
| 48 / 59 | Funil ideal com "Como funciona" em 5 passos | ✅ **concordo** | Dá para escrever com o que o dono já contou, sem inventar nada |
| 49 | Mapa do Brasil com as cidades | 🟡 depois | Só faz sentido com a cobertura real confirmada |
| 52–54 | Conteúdo educativo (blog), plataforma de planejamento | 🟡 futuro | Fora do escopo agora |

## 3. Resumo
- **Real e confirmado no código:** a contradição dos cookies (texto escondido no HTML), as UTMs incompletas na mensagem, os nomes antigos da agenda, os campos sem "opcional", a frase do letreiro duplicada no HTML e o Backbus sem "indicado para".
- **Já resolvido antes dele olhar** (ele viu cópias antigas ou não testou): placeholders, Trevo, acessibilidade, desempenho, segurança, CTA fixo no celular e WhatsApp.
- **O grande recado dele é o mesmo nosso:** falta **prova**, e a **promessa nacional** precisa bater com a realidade. O LinkedIn (concessão no RJ) torna isso mais urgente. Isso é com o dono.

---

# Roadmap proposto (o que eu faço no código)
Mesmo fluxo das rodadas anteriores: um por vez → comparar → bateria → próximo → varreduras 1 e 2 → publicar se tudo estiver ok.

| # | Item | Origem | Esforço |
|---|---|---|---|
| G1 | **Tirar do HTML o aviso de cookies e o link "Preferências de cookies"**. O aviso passa a ser criado pelo script só se um dia houver medição (Pixel/GA4); assim não existe texto contraditório para o Google ler | §12 | Pequeno |
| G2 | **Origem completa na mensagem**: `utm_source / medium / campaign / content / term` | §29 | Pequeno |
| G3 | **Aviso de transparência** acima do botão final: "Seus dados não são enviados automaticamente. Vamos abrir o WhatsApp com o pedido preenchido para você revisar e enviar." | §13 | Pequeno |
| G4 | **Resumo do pedido** na etapa 3: prévia de como a mensagem vai chegar, atualizada enquanto a pessoa preenche | §28 | Médio |
| G5 | **Campos opcionais marcados** ("opcional" em empresa, segmento, região e objetivo) | §39 | Pequeno |
| G6 | "Investimento previsto" → **"Faixa de investimento"**, com "Ainda estou avaliando" (as faixas continuam as mesmas até o dono decidir) | §15 | Pequeno |
| G7 | Agenda coerente: menu e rodapé **"Sugerir horário"**; título **"Prefere conversar? Sugira um horário."** | §26 | Pequeno |
| G8 | Letreiro: frase **1× no HTML**, duplicada só na tela pelo script (o loop visual continua igual) | §21 | Pequeno |
| G9 | Backbus com **"Indicado para…"**, como os outros dois formatos | §19 | Pequeno |
| G10 | Nova seção **"Como funciona"** em 5 passos, antes da chamada final (texto abaixo) | §48/59 | Médio |
| G11 | Fechamento do simulador: **"Gostou de ver sua marca na rua?"** acima do botão "Quero esta campanha" | §17 | Pequeno |
| G12 | **Bloco de confiança** no rodapé: "Agência de mídia em ônibus · CNPJ … · Niterói, RJ · Atendimento nacional", mais organizado que a linha atual | §10 | Pequeno |

**Texto proposto para G10, "Como funciona"** (baseado no que o dono contou: a agência estuda o nicho e o resultado esperado, cria a ideia junto com o cliente e depois executa):
1. **Você conta o objetivo.** O que quer vender, para quem e onde.
2. **Estudamos o seu público.** As regiões e os trajetos por onde ele circula.
3. **Criamos a campanha com você.** A mensagem e a arte, junto com a sua equipe.
4. **Cuidamos da execução.** Do planejamento à instalação nos ônibus.
5. **Sua marca na rua.** Onde o seu cliente passa todos os dias.

**Texto proposto para o Backbus (G9):** "Indicado para fixar a marca em quem faz o mesmo trajeto todos os dias."

## Fica com o dono (não entra no código agora)
1. **Cobertura real:** inventário próprio no RJ? parceiros em outras praças? A partir disso: o texto do topo, as 25 cidades e, depois, o mapa e as páginas por cidade.
2. **Prova:** fotos de campanhas reais, logos de clientes (com autorização), números (ônibus, campanhas, anos).
3. **"Por trás da Plano Urbano":** foto e frase do Fábio.
4. Duração da conversa, faixas de investimento, opção "Ligação".
5. Perfil da Empresa no Google com nome, endereço e telefone iguais aos do site.
