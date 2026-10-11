# 04 — Marketing digital: tráfego, medição e otimização (CRO)

## Funil
Topo (atenção: conteúdo, anúncio frio) → Meio (consideração: isca, remarketing) → Fundo (decisão: oferta, orçamento) → Pós-venda (retenção, indicação).
A LP normalmente vive no meio/fundo. Tráfego frio quase nunca compra de primeira em ofertas caras → capturar lead e nutrir.

## Fontes de tráfego e o que a LP precisa para cada uma
| Fonte | Intenção | Implicação para a LP |
|---|---|---|
| Google Ads (Pesquisa) | alta, ativa | título = termo buscado; ir direto à oferta; "Qualidade da página de destino" influencia Índice de Qualidade → CPC menor |
| Google Perfil da Empresa / Maps | alta, local | endereço, telefone clicável, horários, avaliações |
| Meta Ads (Instagram/Facebook) | baixa–média, interrompida | mais persuasão, prova social, vídeo; mobile; carregamento rápido (usuário no 4G, no navegador interno do app) |
| TikTok Ads | baixa, entretenimento | estética nativa, vídeo, oferta simples |
| E-mail/WhatsApp para base | alta (já conhece) | curta, direto à oferta |
| Orgânico/SEO | variada | conteúdo mais completo, indexável |
| QR code / offline | média | mobile, carregamento imediato, mensagem ligada ao material impresso |

## Métricas
- **Taxa de conversão (CVR)** = conversões ÷ visitantes únicos (ou sessões — definir e manter).
- **CPL** (custo por lead) = investimento ÷ leads. **CPA/CAC** = investimento ÷ vendas.
- **ROAS** = receita ÷ investimento em anúncio. **LTV** (valor do cliente no tempo). Regra saudável: LTV ≥ 3 × CAC.
- Taxa de rejeição / engajamento (GA4 usa "sessões engajadas"), profundidade de rolagem, cliques no CTA, tempo até o clique.
- Qualidade do lead: % que responde, % que vira proposta, % que vira venda.

### Benchmarks (use com cautela)
Fontes de fornecedores (Unbounce, LanderLab, etc.) citam mediana de LP dedicada entre ~4% e ~6,6%, variando de ~3% (e-commerce/SaaS) a >10% (eventos, serviços locais). LP de serviço com CTA de WhatsApp no Brasil costuma relatar 8–15%, mas são números de blogs sem metodologia auditável.
**Uso prático:** o benchmark que importa é o da própria página antes/depois. Para o cliente: comprometer-se com processo e medição, **não com taxa de conversão**.

## Rastreamento (setup padrão que entregamos)
1. **UTMs** em todo link de campanha: `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`. Salvar UTMs em campos ocultos do formulário → chega no CRM.
2. **GA4**: eventos `generate_lead`, `click_whatsapp`, `click_phone`, `form_start`, `scroll` (90%), `purchase`. Marcar como conversões-chave.
3. **Google Tag Manager** (GTM) para organizar tudo; ou gtag direto em páginas simples.
4. **Meta Pixel + Conversions API (CAPI)** — pixel sozinho perde eventos (bloqueadores, iOS). CAPI envia pelo servidor (via Stape/GTM server-side, integração nativa do CRM/plataforma, ou função serverless). Eventos: `PageView`, `ViewContent`, `Lead`, `Contact`, `InitiateCheckout`, `Purchase`, com `event_id` para deduplicar pixel×servidor.
5. **Google Ads**: conversão + conversões otimizadas (enhanced conversions, dados com hash).
6. **Consent Mode v2** do Google + bloqueio do pixel até aceite (LGPD — arquivo 05).
7. **Mapa de calor / gravação de sessão**: Microsoft Clarity (grátis) — ver onde as pessoas travam.
8. Página de obrigado com URL própria (facilita medir).

## CRO — otimização de conversão
Processo: **pesquisar → hipótese → priorizar → testar → aprender**.
- Pesquisa qualitativa: Clarity (gravações, cliques mortos, rage clicks), pesquisa na página ("O que te impediu de…?"), conversas com vendas.
- Priorização ICE (Impacto, Confiança, Facilidade 1–10) ou PIE.
- O que testar primeiro (maior alavanca): oferta > título/proposta de valor > prova > formulário/atrito > layout > cor de botão (quase nunca vale).

### Teste A/B — estatística mínima honesta
- Precisa de tráfego. Ex.: CVR base 5%, detectar melhora relativa de 20% (5% → 6%) com 95% de confiança e 80% de poder ≈ **8.000 visitantes por variante**. Detectar +50% (5% → 7,5%) ≈ 1.500 por variante.
- Rodar ciclos completos de semana (mínimo 1–2 semanas), não parar quando "deu significância" (peeking).
- Pouco tráfego (< 1.000 visitas/mês)? Não faça A/B; faça mudanças grandes com base em pesquisa qualitativa e compare períodos, ciente do ruído.
- Ferramentas: construtores com A/B nativo, VWO, Convert; split por URL com ferramenta de anúncio (testes A/B do Meta); Google Optimize foi descontinuado (2023).

## Ciclo de vida de uma LP que performa
Semana 0: lançamento com tracking validado. Semanas 1–2: ler Clarity, corrigir atritos óbvios. Mês 1+: testes de título/oferta. Mensal: relatório CPL/CVR/qualidade de lead. Esse ciclo é o produto de **manutenção/otimização recorrente** (arquivo 06).
