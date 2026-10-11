# Relatório do estado atual: www.agenciaplanourbano.com.br
**Data:** 08/10/2026 · **Para:** revisão externa (ChatGPT) · **Versão no ar:** v3

## 1. Contexto
- **Cliente:** Agência Plano Urbano (Agencia Plano Urbano Ltda, CNPJ 58.332.620/0001-08, Niterói/RJ). É uma agência de mídia exterior, principalmente em ônibus: busdoor, backbus e envelopamento. Também faz painéis em shopping, outdoor e projetos especiais, como ônibus iluminados de Natal.
- **Site:** uma página só (landing page) + política de privacidade + página 404 com a marca. Foi migrado da Wix em 06/10/2026.
- **Objetivo:** gerar pedidos de orçamento. **Toda a conversão vai para o WhatsApp** (decisão do dono: nada por e-mail, nenhum banco de dados).
- **Identidade:** brandbook oficial. Só as 5 cores (Mostarda #E9AC00, Abóbora #F06101, Índigo #5757C1, Asfalto #2F2E2E, branco, com tons de 75% e 40%), fontes Unbounded (títulos, caixa alta) + Rubik (texto) e assinatura "A cidade é seu público". O tom é profissional e nacional, sem gírias.

## 2. Infraestrutura
| Item | Situação |
|---|---|
| Hospedagem | Firebase Hosting (Google), plano gratuito, HTML/CSS/JS estáticos, sem framework |
| Domínio | Registro.br, administrado diretamente (saiu do provedor da Wix). DNS no Registro.br com DNSSEC válido |
| HTTPS | Certificados válidos; `http://` e o domínio sem www redirecionam para `https://www` |
| E-mail | Google Workspace (3 caixas). MX, SPF e DMARC configurados. **A cobrança está sendo transferida da Wix para o Google** (aguardando a Wix). **DKIM pendente** (só depois da transferência) |
| Cabeçalhos | CSP estrita, sem domínios externos (`default-src 'self'`; fontes e imagens locais), HSTS, nosniff, Referrer-Policy, Permissions-Policy, `frame-ancestors 'none'` |
| Cache | Imagens e fontes com 1 ano (`immutable`, nomes versionados); HTML com 5 minutos |
| Banco de dados / Firebase Auth / Storage | **Não usa.** O site não guarda dados de ninguém |

## 3. Estrutura da página (ordem atual)
1. **Topo:** "A cidade é seu público." + a cidade que troca (25 capitais e grandes cidades; **cobertura confirmada como real pelo dono**) + "E a sua marca, está em cartaz?" + botões. Mosaico com **fotos reais**: ônibus da própria Plano Urbano ("Promova seu negócio aqui"), ônibus de Natal, ônibus iluminado e a peça oficial "A cidade fala, sua marca responde".
2. **Letreiro** inclinado: "Visível. Memorável. Inevitável. A rua é sua vitrine."
3. **Formulário em 3 etapas** (seus dados → sua empresa → sua campanha). Valida o WhatsApp (DDD real, aceita +55), marca os campos opcionais e tem "Faixa de investimento". Na etapa 3 aparece um **resumo do pedido igual à mensagem que será enviada**, com o aviso "Seus dados não são enviados automaticamente…". O envio abre o WhatsApp com o pedido escrito, incluindo a origem (as 5 UTMs) e a escolha do simulador. Para quem está no computador sem WhatsApp, há o botão "Copie o pedido".
4. **Agenda:** "Prefere conversar? Sugira um horário." Calendário de dias úteis; a sugestão vai pelo WhatsApp e a agência confirma (sem agenda em tempo real, e o texto deixa isso claro).
5. **Carrossel de situações** (busdoor, envelopado, backbus no trânsito).
6. **Faixa:** "Varejo, serviços ou indústria…" + CTA.
7. **Formatos:** envelopado, busdoor e backbus, cada um com "indicado para", + "Criação da campanha".
8. **Campanhas na rua** (nova): **8 fotos reais** (busdoor em São Gonçalo e em Niterói, backbus, outdoor, painéis em shopping, ônibus de Natal, aplicação do adesivo) com legenda de formato e cidade. Os anúncios dos clientes que aparecem nas fotos foram **autorizados pelo dono**.
9. **Simulador:** a pessoa digita a marca e escolhe formato e cor, vê a prévia num ônibus ilustrado, lê "Gostou de ver sua marca na rua?" e clica no botão, que preenche o formulário.
10. **Como funciona** (nova): 5 passos (você conta o objetivo → estudamos o seu público → criamos a campanha com você → cuidamos da execução → sua marca na rua) + foto real da garagem.
11. **Chamada final:** "A rua é sua vitrine." + foto real do ônibus com o anúncio "Anuncie aqui! Plano Urbano".
12. **Rodapé:** bloco de confiança (Agência de mídia exterior · CNPJ · Sede em Niterói, RJ · Atendimento em todo o Brasil), links, WhatsApp, e-mail, Instagram e privacidade.

Elementos fixos: botão flutuante de WhatsApp (desktop) e barra "Solicitar orçamento | WhatsApp" (celular).

## 4. O que já foi feito (3 rodadas de auditoria e correção)
**Rodada 1 (22 correções):** tirada a faixa "Demonstração" e todos os textos provisórios `[ ]`; dados reais da empresa; mensagem do WhatsApp completa; política de privacidade reescrita de acordo com o que o site faz; Open Graph + imagem de compartilhamento; favicon e ícone de iPhone; dados estruturados (AdvertisingAgency, com CNPJ e endereço); página 404 com a marca; imagens em WebP; cache; contraste; cabeçalhos de segurança; rolagem lateral corrigida.

**Rodada 2 (16 itens):** chaves sobrando no CSS; WhatsApp com +55 que perdia dígito; validação de DDD; limites de tamanho nos campos; Esc fecha o menu; WhatsApp funciona sem JavaScript; carrossel acessível pelo teclado; contraste do calendário; contorno dos botões no alto contraste do Windows; `/privacidade/` e `/favicon.ico`; **fontes no próprio site** (3 arquivos variáveis em vez de 6 do Google, CSP sem domínios externos).

**Rodada 3 (análise do ChatGPT + fotos reais, 16 itens):** contradição dos cookies resolvida (o aviso só existe se houver medição; hoje não há); 5 UTMs; aviso de transparência; resumo do pedido; campos opcionais; faixa de investimento; agenda como "sugerir horário"; frase do letreiro uma vez só no código; Backbus com "indicado para"; seção "Como funciona"; fechamento do simulador; bloco de confiança no rodapé; **14 fotos reais** no topo, na galeria, em "Como funciona", na chamada final e na imagem de compartilhamento.

## 5. Resultado dos testes (no site oficial, depois de publicar)
Bateria automática com **54 verificações**, todas aprovadas, entre elas:
- **axe-core** (WCAG 2.2 AA + boas práticas): **0 violações** no desktop e no celular.
- **Validador W3C:** privacidade e 404 sem nenhuma mensagem; página inicial com 1 aviso, que é falso positivo (`mask: linear-gradient(...)` é CSS válido e já tem a versão `-webkit-`).
- **11 larguras de tela** (320 a 2560 px): sem rolagem lateral e sem nada cortado.
- **Formulário:** 24 casos de telefone (digitados e colados) corretos; mensagem com emoji e caracteres especiais intacta; foco e teclado corretos; Esc fecha o menu.
- Sem erros de JavaScript; nenhum arquivo interno exposto; links ok; nenhum texto provisório.
- **Desempenho** (celular de entrada simulado, 4G lenta, CPU 4×): primeira pintura ~2–3 s e conteúdo principal ~2,5–4,5 s, com oscilação da rede. CLS ≈ 0. Página com ~290 KB, contando fontes e imagens.

## 6. Decisões do dono (não reabrir)
- Conversão **só pelo WhatsApp**; nada por e-mail, sem banco de dados.
- **Sem medição de visitas** por enquanto (sem GA4). O Pixel da Meta entra quando começarem a anunciar.
- **Cobertura das 25 cidades é real**: manter.
- Anúncios de clientes nas fotos: **autorizados**.
- **Uma página só**: não criar páginas por cidade ou formato.
- **Não mexer no desempenho/efeitos visuais** (o celular fica ~1,5 s ocupado com layout; o dono preferiu manter o design).
- Por enquanto, **só o material dos serviços já realizados** (fotos): sem números, logos, foto do sócio, duração da conversa ou faixas novas.
- Sem Perfil da Empresa no Google por enquanto.

## 7. Pendências (fora do código)
- Transferência do Google Workspace da Wix para o Google (aguardando a Wix) → cadastrar o cartão no Google → testar o e-mail → cancelar o Premium da Wix.
- DKIM e relatórios de DMARC, depois do Workspace.
- Enviar o sitemap no Search Console.
- Renovar o domínio no Registro.br antes de 31/01/2027.

## 8. Limitações conhecidas (aceitas)
- A agenda sugere horário; não consulta agenda real.
- No computador sem WhatsApp Web, o envio depende do botão "Copie o pedido".
- CSP com `'unsafe-inline'` (CSS e JS ficam dentro do HTML; o site não tem login nem dados sensíveis).
- O subdomínio `geobus.api` (outro projeto da agência) está fora do ar de propósito: o projeto está parado.

## 9. Pedido para a revisão
Analisar o site **no estado atual**, considerando as decisões da seção 6 como definitivas. Apontar apenas:
1. erros ou inconsistências que ainda existam;
2. melhorias de conversão ou credibilidade possíveis **só com o material que já existe**;
3. riscos técnicos, jurídicos (LGPD) ou de SEO não cobertos acima.

Para cada ponto: onde está, por que importa e qual a correção sugerida.
