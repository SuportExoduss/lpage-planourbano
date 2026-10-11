# Super varredura: www.agenciaplanourbano.com.br (11/10/2026)

O que foi revisado: o site no ar (é idêntico ao `index.html` local), o `src.html` linha a linha, a política de privacidade, a página 404, `build.py`, `firebase.json`, robots, sitemap, as 15 fotos (comparadas com os textos alternativos), os scripts de teste, `ferramentas/orcamento.html` e a proposta TRV-2026-001.
Testes feitos: formulário nas 3 etapas (validação, 10 formatos de telefone, caracteres especiais e emoji, resumo e mensagem final), agenda, simulador (3 formatos × 14 nomes), carrossel, menu do celular e Esc, celular com 375 px, desktop, redirecionamentos e arquivos internos (todos dão 404). A bateria de regressão rodou no site oficial: **61/61**.

## Erros reais (corrigir)
| # | Onde | Problema | Correção sugerida |
|---|---|---|---|
| 1 | Agenda | **Mostra feriados nacionais como dias livres.** Amanhã, 12/10 (Nossa Senhora Aparecida), está disponível, assim como 02/11 (Finados) e 20/11 (Consciência Negra). | Lista de feriados no `CFG.agenda` (o do ano corrente e o do seguinte). |
| 2 | Agenda | **Fuso horário.** Os horários usam o relógio de quem visita, mas a mensagem diz "horário de Brasília". Exemplo: alguém em Manaus ou Campo Grande (as duas estão na faixa de cidades) escolhe 09:00 querendo dizer 09:00 local, e a agência recebe "09:00 (horário de Brasília)", que é 1 h de diferença. O corte de "pelo menos 2 h a partir de agora" também usa o fuso local. | Calcular os horários em `America/Sao_Paulo` ou escrever na mensagem o fuso de quem visita. |
| 3 | Formulário, etapa 3 | **"Prazo para início" já vem marcado como "Este mês".** Quem não mexe no campo manda "Prazo: Este mês" sem ter escolhido, e a agência recebe uma urgência falsa. Os outros campos começam neutros ("Ainda não sei", "Ainda estou avaliando"). | Primeira opção neutra, por exemplo "Ainda não defini". |
| 4 | Mensagem do WhatsApp (simulador) | A linha do simulador chega como `Padaria / backbus / abobora`, com o código interno: "abobora" e "indigo" sem acento e o formato em minúsculas. | Usar os nomes que aparecem na tela: "Backbus / Abóbora". |
| 5 | Texto do formulário | **Contradição:** o texto diz "Respondemos pelo WhatsApp", mas logo abaixo a pessoa pode escolher retorno por **Ligação**. | Por exemplo: "Respondemos pelo canal que você escolher." |

## Problemas menores
| # | Onde | Problema |
|---|---|---|
| 6 | Agenda | Quem escolhe um dia em outubro e passa para novembro continua vendo "segunda-feira, 12 de outubro" e os horários de outubro embaixo do calendário de novembro. |
| 7 | Agenda | Depois que um dia é escolhido, o aviso "Horário de Brasília." some do texto de apoio. A agenda também oferece horários de almoço (12:00–13:30); confirmar com a agência se ela quer isso. |
| 8 | Telefone | Aceita número de 10 dígitos que começa com 6–9 depois do DDD, como "(21) 8606-2741". É um celular antigo sem o 9, que não existe desde 2016. Telefone fixo (2–5) faz sentido aceitar; esse caso não. |
| 9 | Celular, 360–380 px | O botão "Solicitar orçamento" da barra fixa quebra em 2 linhas. A regra `@media (max-width:380px)` foi feita para 320 px, mas pega também o iPhone SE/mini e muitos Androids. |
| 10 | Simulador, celular | O texto de exemplo aparece cortado: "NOME DA SUA MARC". |
| 11 | Simulador | Nomes com letras largas (ex.: "MMMMMMMMMMMM", "WWWW…") passam da lateral e da traseira do ônibus. Nomes reais testados (Drogaria Pacheco, Supermercado Mundial, Clínica Odontológica…) couberam todos. |
| 12 | Tela de "Quase lá" | Diz "Abrimos o WhatsApp" mesmo quando o navegador bloqueou a aba. "Não usa WhatsApp no computador?" aparece também no celular. Para fazer um segundo pedido é preciso recarregar a página. |
| 13 | Etapa 1 | O link da Política de Privacidade abre na mesma aba, e quem clica sai do formulário no meio. |
| 14 | Faixa de cidades | "São Bernardo." O nome oficial é **São Bernardo do Campo**. O texto escondido, lido pelo leitor de tela e pelo Google, diz "nas maiores cidades", mas a lista inclui Florianópolis e Natal pelo turismo. |
| 15 | Rodapé | "Política de Privacidade" está na coluna "Redes". |
| 16 | Slogan | O site usa "A cidade é seu público", mas as peças da própria agência que aparecem nas fotos (o ônibus do topo e a imagem do olho) dizem "A cidade é **o** seu público". Não mexer no site (é decisão do dono); só registrar a diferença para a agência alinhar as próximas peças. |
| 17 | Formulário × galeria | A galeria mostra **Outdoor** e **Painéis em shopping**, mas o campo "Formato de interesse" só oferece formatos de ônibus (o resto cai em "Outro"). O título e a descrição também falam só de ônibus. |
| 18 | Topo | 3 das 4 fotos do topo são de Natal (ônibus iluminados). Em outubro e no resto do ano isso parece campanha de época. |

## Pendências no código
- **Medição desligada pelo bloqueio de segurança:** se o Pixel da Meta ou o GA4 forem ligados no `CFG`, a CSP do `firebase.json` (`script-src 'self'`, `connect-src 'self'`, `img-src 'self' data:`) bloqueia os dois. Ao ligar, é preciso liberar `connect.facebook.net`, `www.facebook.com`, `www.googletagmanager.com` e `*.google-analytics.com`.
- Anotações velhas no `src.html` (não aparecem no site; o build tira): linha 489, "CONFIRMAR com a agência onde ela já opera" (já confirmado); linha 506, "TROCAR por foto de uma campanha" (já é foto real); linha 771, "CONFERIR: o site atual mostra .com" (resolvido; falta só testar o e-mail, que já está na lista de pendências); linha 485, "o bairro que troca" (agora são cidades); linha 731, "7. CHAMADA FINAL" em cima de "Como funciona".
- `testes/regressao.py:223`: aviso `SyntaxWarning: "\/"` (vai virar erro em uma versão futura do Python). Usar uma string crua `r"..."`.
- `planourbano.web.app` e `planourbano.firebaseapp.com` mostram a mesma página sem redirecionar para o domínio. O canonical evita conteúdo duplicado no Google; um redirecionamento seria mais limpo.
- `build.py` ainda diz no comentário que a página "se recarrega sozinha" com a versão; esse código não existe mais no `src.html`.

## Política de privacidade (LGPD)
- Ela lista como base legal a execução de contrato e o legítimo interesse e fala em "revogar consentimentos", mas o formulário coleta um **consentimento** ("autorizo o contato"). Melhor alinhar: ou citar o consentimento (art. 7º, I), ou trocar o texto da caixa por um simples "Li a Política de Privacidade".
- Não menciona **transferência internacional** (art. 33): Google/Firebase e WhatsApp/Meta guardam dados fora do Brasil.
- O Encarregado aparece só como um e-mail. Isso é aceito para agente de pequeno porte (Res. ANPD 2/2022), desde que o e-mail funcione, e ele ainda depende do teste do Workspace.

## Fora do site
- **Proposta TRV-2026-001** (`orcamentos/trevo-plano-urbano.html` + PDF): **venceu em 07/10/2026**. Descreve a v3 de mármore ("Sua marca gravada na cidade", FAQ, GA4/Pixel, aviso de cookies, formulário por e-mail e planilha), e quase nada disso foi entregue, por decisão do dono. O contato da Trevo ainda está com **"[seu WhatsApp]" e "[seu e-mail]"**. Antes de reenviar ou mandar assinar: atualizar o escopo, a validade e os contatos.
- `ferramentas/orcamento.html`: as condições dizem "30% na aprovação do **design**", e a proposta diz "30% na aprovação do **texto**". Revisões vazias ou 0 geram "NaN" ou 0 h.

## O que está certo (conferido)
Nenhum erro de JavaScript · 0 imagens quebradas · fontes carregadas · nenhum link interno quebrado · http, sem www, `/index.html`, `/privacidade/`, `/contact-8` e `/book-online` redirecionam certo · arquivos internos (src, .py, .svg, firebase.json, visualizar) dão 404 · cabeçalhos de segurança ok · sem rolagem lateral no celular · menu e Esc ok · carrossel com volta ao início ok · honeypot ok · caracteres especiais, emoji e quebras de linha chegam intactos ao WhatsApp · os textos alternativos batem com as fotos · português dos textos visíveis, da política e da 404 sem erros de ortografia ou concordância.

## Correções publicadas (11/10/2026, regressão no site oficial 61/61)
Feito: agenda no horário de Brasília em qualquer fuso, com aviso da diferença ("no seu fuso, 1 h a menos") · prazo começa em "Ainda não defini" · simulador manda "Backbus / Abóbora / Índigo" · "Respondemos pelo WhatsApp ou por ligação, como você preferir." · política com consentimento (art. 7º, I) e transferência internacional (art. 33) · barra do celular em 1 linha de 341 a 380 px · texto de exemplo do simulador "Digite aqui" · "São Bernardo do Campo" (o nome que não cabe diminui só o necessário) · nota da CSP junto do CFG (GA4/Pixel) · anotações velhas e comentário do build.py · aviso do regressao.py.
Não feito: feriados na agenda (fora do pedido) e itens menores 6, 7 (almoço), 8, 11–13, 15, 17, 18. A proposta TRV-2026-001 foi descartada: negócio fechado.
Cópias de antes: src-v4u.html, src-privacidade-v4u.html.

## Rodada 2 (11/10/2026, publicada, 61/61 no site oficial)
Pedido do dono depois da análise do ChatGPT. Feito: agenda limpa o dia escolhido ao trocar de mês · celular sem o 9 recusado com aviso próprio · nomes largos cabem no simulador · tela final diz a verdade quando a aba é bloqueada · política abre em nova aba no formulário · política saiu de "Redes" e foi para a linha legal do rodapé · planourbano.web.app e .firebaseapp.com levam ao www (script no head das 3 páginas) · política de privacidade reescrita item por item pela LGPD (arts. 5º, 6º, 7º, 8º, 10, 16, 18, 19, 33, 41, 46 e 48).
Fotos: as 50 originais do Drive foram classificadas por formato (busdoor = só o vidro traseiro; max busdoor = vidro inteiro e área ao redor; backbus = traseira inteira; envelopado = carroceria inteira). A galeria mostra 2 de cada (envelopado: 1) e a pasta "Special Projects" (colagem + janela de fotos) reúne 11 fotos de Natal, shopping e outdoor. O topo perdeu as fotos de Natal. Max busdoor entrou nos formatos, no simulador e no formulário; o formulário ganhou "Projeto especial (Natal, shopping, outdoor)".
Mantido por decisão do dono: feriados na agenda.
