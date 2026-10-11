# Auditoria completa: www.agenciaplanourbano.com.br

**Data:** 07/10/2026 · **Visão:** primeira visita, sem usar o que eu já sabia do projeto
**Como foi feita:** acesso real ao site no Edge (desktop 1440 px e celular 390 px), navegador do app, `curl`, consultas de DNS e testes automáticos de interação (formulário, agenda, simulador, menu, teclado, contraste, movimento reduzido).

---

## 1. Resumo

O site é **rápido, bonito, acessível e tecnicamente bem montado**. O problema não é técnico, é de **acabamento**: o site oficial ainda está com **cara de demonstração**. Tem uma faixa dizendo "Demonstração da Trevo", textos provisórios entre `[ ]` à vista do público e dados da empresa trocados por marcadores. Também faltam **elementos de confiança** (clientes, campanhas reais, números), e alguns dados do formulário **se perdem** no caminho para o WhatsApp.

| Área | Nota | Comentário |
|---|---|---|
| Velocidade | 9/10 | Resposta em 0,29 s, carga em 0,7 s, zero saltos de layout |
| Visual / marca | 8/10 | Fiel ao brandbook, com personalidade. Uma imagem escura e um ícone confuso |
| Celular | 8/10 | Sem rolagem lateral, menu ok, barra fixa de ação |
| Acessibilidade | 8/10 | Foco visível, rótulos, `lang`, movimento reduzido respeitado. Um contraste baixo |
| SEO técnico | 6/10 | Canonical, sitemap e robots ok. Falta prévia de compartilhamento, dados estruturados, favicon em arquivo e página 404 |
| Conteúdo / confiança | 4/10 | Marcadores provisórios à vista, sem prova social, endereço divergente |
| Conversão | 5/10 | Bom caminho até o WhatsApp, mas o formulário perde dados e o computador sem WhatsApp trava o envio |
| E-mail (DNS) | 6/10 | MX, SPF e DMARC ok. **Falta o DKIM** do Google Workspace |

---

## 2. 🔴 Crítico: corrigir antes de divulgar o site

### 2.1 Faixa "Demonstração" no topo do site oficial
A primeira coisa que qualquer visitante lê, no topo da página:
> "**Demonstração** da Trevo para a Plano Urbano. O que tem borda tracejada ou está entre [ ] é provisório."

O rodapé repete o aviso no celular. Para um cliente em potencial, o recado é que o site não está pronto, e que outra empresa (Trevo) está por trás.
**Correção:** remover a faixa e a nota do rodapé.

### 2.2 Textos provisórios à vista do público
O site mostra 6 marcadores com borda tracejada:

| Onde | O que aparece | Precisa de |
|---|---|---|
| Agenda → "Duração" | `[cerca de 15 minutos]` | Confirmar a duração com a agência |
| Formatos → "Também atuamos com" | `[ponto de ônibus]` `[painel de LED]` `[redes sociais]` | Confirmar quais serviços eles fazem de fato |
| Rodapé | `© 2026 [Razão social] \| CNPJ [00.000.000/0001-00]` | Já temos: Agencia Plano Urbano Ltda · 58.332.620/0001-08 |

### 2.3 Endereço divergente
- O rodapé diz **"Sede no Rio de Janeiro, RJ"**.
- A política de privacidade e o CNPJ dizem **Niterói/RJ** (Rua São José, 253, Fonseca).

**Correção:** "Sede em Niterói, RJ. Atendimento em todo o Brasil."

### 2.4 O formulário perde informações no WhatsApp
O formulário tem 3 etapas, mas a mensagem que chega no WhatsApp **não leva** tudo:

| Campo preenchido | Chega no WhatsApp? |
|---|---|
| Nome, empresa, WhatsApp, segmento, região, formato, prazo, verba, objetivo | ✅ |
| **"Prefere receber o contato por: Ligação"** | ❌ **Perdido**. Quem pede ligação recebe WhatsApp |
| **Escolha feita no simulador** (marca, formato, cor) | ❌ Perdido |
| **Origem da visita** (UTM: Instagram, anúncio etc.) | ❌ Perdido. Quando começarem a anunciar, não vão saber qual anúncio trouxe o contato |

**Correção:** incluir os três campos na mensagem (é uma linha de código).

### 2.5 No computador, o envio depende do WhatsApp Web
Depois de preencher as 3 etapas, o site abre o WhatsApp. No celular, abre o aplicativo e funciona bem. **No computador**, abre o `web.whatsapp.com`, que exige estar logado. Quem não usa WhatsApp Web no computador vê um QR code e **desiste com o formulário já preenchido**, e o pedido se perde sem a agência saber.
Para um público B2B, que muitas vezes pesquisa no computador do trabalho, isso pesa.
**Opções:** (a) no computador, mostrar também "Prefere que a gente ligue? Seu número já foi anotado" junto com o número da agência, ou (b) guardar o pedido num banco simples (Firestore), que mais tarde vira o painel /admin. Essa decisão é do dono.

---

## 3. 🟠 Alto: afeta resultado e credibilidade

### 3.1 Sem prévia ao compartilhar o link
Não existem as tags **Open Graph** (`og:title`, `og:description`, `og:image`). Quando alguém manda o site **pelo WhatsApp, Instagram ou LinkedIn**, aparece só o endereço, **sem imagem nem título**. Para uma agência que vende pelo WhatsApp, é o canal número 1 de divulgação.
**Correção:** criar uma imagem de compartilhamento (1200×630, com a marca e o slogan) e adicionar as tags.

### 3.2 Nenhuma prova de que a agência entrega
O site explica bem os formatos, mas não mostra **nenhum**:
- cliente atendido (nem os logos);
- foto de campanha real na rua (todos os ônibus são ilustrações com "SUA MARCA");
- número ("X campanhas", "Y cidades", "desde 20XX");
- depoimento.

Quem anuncia investe de R$ 5 mil a R$ 50 mil ou mais, e a prova social é o que leva a pessoa a pedir o orçamento. **É o maior ganho de conversão disponível.** A apresentação em PDF que vocês têm pode ter material para isso.

### 3.3 As 25 cidades do topo precisam ser confirmadas
O título troca entre 25 cidades ("Campanhas nas maiores cidades do Brasil": São Paulo, Manaus, Belém, São Luís...). Se a agência não tem como executar em alguma delas, isso é **promessa que pode gerar problema** (CDC/CONAR) e frustração no primeiro contato. **Confirmar a lista com o dono.**

### 3.4 A agenda simula horários que não existem
A seção "Prefere agendar uma conversa?" mostra um calendário com horários de 30 em 30 minutos, das 9h às 18h, e diz "Os horários disponíveis aparecem aqui". Na verdade, ela **não consulta nenhuma agenda real**: qualquer horário pode ser escolhido, inclusive o almoço e um que já esteja ocupado. A escolha só vira uma mensagem de WhatsApp.
**Correção mínima:** trocar o texto para "Sugira um dia e horário; confirmamos pelo WhatsApp" e tirar o horário de almoço. **Alternativa:** um link do Google Agenda (agendamento de horários, grátis no Workspace) com a disponibilidade real.

### 3.5 E-mail sem DKIM
O DNS tem MX, SPF e DMARC, mas **não tem DKIM** (`google._domainkey`). Sem ele, os e-mails enviados pela agência têm **mais chance de cair no spam** dos clientes, principalmente no Gmail e no Yahoo, que endureceram as regras em 2024.
**Correção (5 min, depois que o Workspace passar para o Google):** admin.google.com → Apps → Gmail → **Autenticar e-mail** → Gerar registro → criar o TXT `google._domainkey` no Registro.br → **Iniciar autenticação**.

### 3.6 Página de erro 404 do Firebase, em inglês
Qualquer link quebrado (`/qualquer-coisa`) mostra uma página técnica do Firebase, **em inglês**, falando de `firebase.json` e `index.html`. Ela não tem a marca da agência nem um caminho de volta.
**Correção:** criar um `404.html` no visual do site, com um botão para voltar e outro para o WhatsApp.

### 3.7 Política de privacidade desatualizada em relação ao site
A política fala de **cookies do Google Analytics e do Meta Pixel** e manda o visitante a **"Preferências de cookies, no rodapé"**. O site não usa nenhum dos dois hoje, e esse link está escondido. A política também diz que guarda a **origem da visita (UTM)**, o que hoje não acontece (ver 2.4).
**Correção:** reescrever os itens 2 e 3 de acordo com o que o site realmente faz. Quando o Pixel entrar, voltam.

### 3.8 O site baixa a si mesmo de novo a cada visita
Um código da fase de demonstração ("se o servidor tem versão nova, recarrega a página") **baixa a página inteira de novo** a cada carregamento e a cada vez que o visitante volta à aba (2 vezes na carga, medido). Ele também pode **recarregar a página sozinho** enquanto a pessoa está no simulador ou na agenda, o que apaga o que ela digitou.
**Correção:** remover. Era útil para o cliente revisar a demo, não para o site oficial.

---

## 4. 🟡 Médio: polimento

| # | Item | Detalhe | Correção |
|---|---|---|---|
| 4.1 | **Botão flutuante** não parece WhatsApp | É um círculo mostarda com o **símbolo da Plano Urbano**. Ninguém reconhece como WhatsApp (só o leitor de tela "sabe") | Usar o ícone do WhatsApp, ou o símbolo da marca com um balão de conversa |
| 4.2 | **Favicon** só embutido no código | O Google Search não mostra favicon embutido no código (`data:`) nos resultados. Falta também o ícone do iPhone (apple-touch-icon) | Gerar `favicon.svg`/`.png` e `apple-touch-icon.png` |
| 4.3 | **Sem dados estruturados** | Sem JSON-LD de `Organization`/`LocalBusiness`, o Google não liga o site à empresa (CNPJ, endereço, telefone, Instagram) | Adicionar o bloco JSON-LD |
| 4.4 | **Imagem do topo pesada** | `onibus.jpg` tem **149 KB em JPEG**. Em WebP fica com ~50 KB | Converter (as outras já são WebP) |
| 4.5 | **Cache curto** | Imagens com `max-age=300` (5 min). Como os arquivos já têm `?v=versão`, podem ficar guardados 1 ano | Ajustar o `firebase.json` para `img/**` |
| 4.6 | **Imagem escura** em "A rua é sua vitrine" | `cidade.webp` está escura e sem contraste, parece um erro de exposição. É a última imagem antes do rodapé | Trocar por uma foto do brandbook ou clarear |
| 4.7 | **E-mail quebrado** no rodapé (desktop) | Fica "comercial@agenciaplanourbano.com." numa linha e "br" na outra | Quebrar antes do @, ou diminuir a fonte da coluna |
| 4.8 | **Contraste** | O rótulo "Sua marca" (mostarda sobre cinza, no simulador) tem contraste de 3,0:1; o mínimo do WCAG AA é 4,5:1 | Escurecer o fundo ou clarear o texto |
| 4.9 | **Search Console** | Ainda sem o sitemap enviado | Em andamento |
| 4.10 | **Fontes** | Pede os pesos 400 e 600 da Unbounded, que não são usados | Tirar da URL das fontes |
| 4.11 | **Cabeçalhos de segurança** | Tem HSTS e nosniff. Faltam `Content-Security-Policy`, `frame-ancestors` e `Permissions-Policy` | Adicionar no `firebase.json` (baixo risco, porque o site não tem login) |
| 4.12 | **DMARC sem relatórios** | `p=none` sem `rua`: não mostra quem tenta usar o domínio para mandar e-mail falso | Depois do DKIM, adicionar `rua` e, com o tempo, endurecer para `quarantine` |
| 4.13 | **Política de privacidade sem cabeçalho** | Página solta, sem logo nem menu. Só tem "Voltar" no fim | Adicionar o logo no topo, com link para a página inicial |

---

## 5. ⚪ Baixo

- **Nomes diferentes para o mesmo botão:** "Anunciar", "Colocar minha marca em cartaz", "Solicitar orçamento" e "Quero esta campanha" levam todos ao mesmo formulário. Dá para padronizar em 2 nomes.
- **Rodapé** usa `h4` sem `h3` antes, uma hierarquia de títulos pulada (detalhe de acessibilidade e SEO).
- **Opção "Ligação"** no formulário: se a agência não liga, é melhor remover; se liga, ver o item 2.4.
- **`geobus.api` fora do ar (erro 503)**. Não é do site, mas é do domínio. Avisar o Fabio.

---

## 6. ✅ O que está muito bom (manter)

- **Velocidade:** servidor em São Paulo (cache GRU), resposta em 0,29 s, página pronta em 0,7 s, **CLS 0** (nada pula na tela). HTML comprimido em Brotli (100 KB → 21 KB).
- **HTTPS** válido nos dois endereços (até 01/2027, renova sozinho). O endereço sem www e o `http://` **redirecionam para o www**.
- **Endereços antigos da Wix** (`/contact-8` e `/book-online`) redirecionam com 301, sem perder o Google.
- **Acessibilidade acima da média:** foco visível em todos os links (contorno de 3 px), todos os campos com rótulo, imagens com `alt`, `lang="pt-BR"`, menu do celular com `aria-expanded`, e **as animações param** para quem pede movimento reduzido. O título que troca de cidade tem uma versão fixa para leitor de tela.
- **Celular:** sem rolagem lateral, barra fixa com "Solicitar orçamento" e "WhatsApp", menu funcionando.
- **Formulário:** a validação é clara ("Informe um WhatsApp válido, com DDD."), o WhatsApp é formatado sozinho, há proteção anti-robô e o simulador **preenche o formulário** com o formato escolhido.
- **Nenhum erro de JavaScript** no console.
- **Nenhum arquivo interno exposto** (código-fonte, configuração e versões antigas dão 404).
- **Visual** fiel ao brandbook: as 5 cores, Unbounded + Rubik, as frases da marca. O simulador do ônibus é um diferencial real.

---

## 7. Plano de ação sugerido

| Ordem | O quê | Itens | Esforço | Depende de |
|---|---|---|---|---|
| **1** | Tirar a cara de demo | 2.1, 2.2 (rodapé), 2.3 | 15 min | Nada |
| **2** | Formulário completo no WhatsApp | 2.4, 3.8 | 20 min | Nada |
| **3** | Confirmar com o dono | 2.2 (duração, serviços), 3.3 (cidades), 2.5 (computador), opção "Ligação" | Conversa | Dono |
| **4** | Compartilhamento + Google | 3.1, 4.2, 4.3, 3.6 | 1–2 h | Nada |
| **5** | Agenda honesta + privacidade | 3.4, 3.7 | 30 min | Item 3 |
| **6** | Prova social | 3.2 | 2–4 h | Material da agência (clientes, fotos, números) |
| **7** | E-mail | 3.5, 4.12 | 10 min | Workspace já no Google |
| **8** | Polimento | 4.1, 4.4–4.8, 4.10, 4.11, 4.13 | 1–2 h | Nada |

Os itens **1 e 2** levam ~35 minutos, eu faço sozinho e já tiram os problemas mais visíveis.
