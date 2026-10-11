# 02 — Web design e implementação técnica

## Princípios visuais
- **Hierarquia**: o olho deve cair em título → imagem → botão. Uma coisa dominante por seção.
- **Um único acento de cor** reservado para CTAs. Se tudo é laranja, nada é.
- **Contraste** WCAG AA: texto normal ≥ 4.5:1, texto grande/botão ≥ 3:1.
- **Espaço em branco** é o que faz parecer "caro". Seções com padding vertical generoso (64–120 px desktop, 48–72 px mobile).
- **Grid**: largura de leitura 60–75 caracteres por linha (~680 px de texto corrido). Container 1100–1240 px.
- **Tipografia**: no máximo 2 famílias (1 é suficiente). Corpo 16–18 px mobile, 18–20 px desktop; line-height 1.5–1.7. Escala de títulos modular (ex.: 1.25). Google Fonts com `font-display: swap` e subset latin; ou fonte do sistema (mais rápido).
- **Leis úteis**: Fitts (alvo grande e perto = mais fácil → botão largo no mobile, área de toque ≥ 44–48 px); Hick (menos opções = decisão mais rápida); Jakob (o usuário espera que sua página funcione como as outras — não reinvente padrões); proximidade/Gestalt (agrupar o que é relacionado); padrão de leitura em F/Z (títulos à esquerda, CTA no fim do caminho).
- **Imagens**: pessoas reais > banco de imagens. Rosto olhando para o CTA/título direciona atenção. Mostrar o produto em uso / o resultado (antes-depois quando permitido).
- **Botão**: parece botão (preenchido, cantos arredondados, sombra leve), verbo + benefício, 1ª pessoa costuma funcionar ("Quero meu orçamento"). Microcópia de apoio embaixo: "Resposta em até 10 min · Sem compromisso".
- **Consistência**: tokens de design (cores, raios, sombras, espaçamento em múltiplos de 4/8).

## Mobile primeiro
No Brasil a maioria do tráfego de redes sociais é mobile (frequentemente 80%+ em Meta Ads). Projetar em 360–390 px de largura primeiro.
- Primeira dobra mobile: título + subtítulo + botão visíveis sem rolar.
- CTA fixo no rodapé da tela (sticky) em páginas longas.
- Formulários: `type="tel"`, `inputmode="numeric"`, `autocomplete="name|email|tel"`, labels visíveis (placeholder não é label), máscara de telefone, poucos campos.
- Nada de pop-up de entrada no mobile (Google penaliza intersticiais intrusivos; e irrita).

## Performance (afeta conversão, custo do anúncio e SEO)
Core Web Vitals (Google, avaliado no percentil 75 de visitas reais):
| Métrica | Bom | Ruim |
|---|---|---|
| LCP (carregamento do maior elemento) | ≤ 2,5 s | > 4 s |
| INP (resposta a interação) | ≤ 200 ms | > 500 ms |
| CLS (estabilidade do layout) | ≤ 0,1 | > 0,25 |

Como atingir:
- Imagem do hero em **AVIF/WebP**, dimensionada (`srcset`), com `fetchpriority="high"` e **sem** lazy-load; demais imagens `loading="lazy"`.
- `width`/`height` em toda imagem e vídeo (evita CLS). Espaço reservado para banner de cookies.
- Vídeo: nunca autoplay pesado no hero; usar thumbnail + carregar player (YouTube/Vimeo) só no clique ("facade").
- CSS crítico inline, JS mínimo e `defer`. Evitar construtores pesados (Elementor) quando performance importa.
- Scripts de terceiros (pixel, GTM, chat) são o maior vilão: carregar após consentimento/interação.
- Hospedagem com CDN (Cloudflare, Vercel, Netlify, Firebase Hosting).
- Meta: PageSpeed Insights mobile ≥ 90; página total < 1 MB; LCP < 2 s em 4G.

## Acessibilidade (também é qualidade e alcance)
HTML semântico (`header`, `main`, `section`, `h1` único), `alt` descritivo, foco visível, navegação por teclado, contraste, `lang="pt-BR"`, não depender só de cor, respeitar `prefers-reduced-motion`. Lei Brasileira de Inclusão (Lei 13.146/2015, art. 63) exige acessibilidade em sites de empresas com sede/representação no país.

## SEO básico (mesmo LP de anúncio)
`<title>` ≤ 60 caracteres, meta description ≤ 155, `h1` com a palavra-chave, URL curta, Open Graph (imagem 1200×630 para compartilhar no WhatsApp), favicon, `schema.org` (LocalBusiness, Product, FAQPage, Organization), sitemap/robots se for indexar. LP de teste A/B: variante com `canonical` para a original. Página de obrigado: `noindex`.

## Stack — opções e quando usar
| Opção | Custo | Prós | Contras | Quando |
|---|---|---|---|---|
| HTML/CSS/JS puro (ou Astro) + hospedagem estática (Cloudflare Pages / Vercel / Netlify / Firebase) | hospedagem grátis–baixo | performance máxima, controle total, sem mensalidade | cliente não edita sozinho | padrão para nós; LP de alta conversão |
| Next.js / Astro + CMS headless | baixo | editável, escalável | mais horas | várias LPs, cliente edita |
| WordPress + Elementor/Bricks | hospedagem R$15–60/mês | cliente conhece, edita | mais lento, manutenção, plugins | cliente exige WP |
| Construtores SaaS (GreatPages, Leadlovers, RD Station, Unbounce, Framer, Webflow) | R$50–R$500+/mês | rápido, A/B embutido, edita sozinho | mensalidade, lock-in | cliente de marketing que testa muito |

Formulários sem backend: Formspree, Getform, Google Forms/Sheets via Apps Script, Firebase Functions, ou webhook para CRM (RD Station, HubSpot, Pipedrive, Kommo) / automação (Make, Zapier, n8n).
WhatsApp: link `https://wa.me/55DDDNUMERO?text=<mensagem codificada>` com mensagem pré-preenchida que identifica a origem ("Vim pela página de cortinas").
Pagamento: link de checkout (Mercado Pago, Stripe, Asaas, Hotmart/Kiwify para infoproduto).

## Checklist técnico de entrega (QA)
- [ ] Testado em Chrome Android, Safari iOS, desktop (Chrome/Edge/Firefox), larguras 360/390/768/1280/1440.
- [ ] PageSpeed mobile ≥ 90, CWV bons.
- [ ] Todos os links/CTAs funcionam; WhatsApp abre com mensagem; formulário envia e chega (testar de ponta a ponta), mensagem de sucesso, página de obrigado.
- [ ] Validação de formulário amigável; honeypot/Turnstile contra spam.
- [ ] Pixel/GA4/tags disparando os eventos certos (Tag Assistant, Meta Pixel Helper, Events Manager test).
- [ ] Banner de cookies bloqueando tags antes do aceite.
- [ ] Política de privacidade, CNPJ, contato no rodapé.
- [ ] HTTPS, domínio, redirecionamento www/sem-www, 404.
- [ ] OG image testada colando o link no WhatsApp.
- [ ] Ortografia revisada; números e preços conferidos com o cliente.
- [ ] Backup do código + acesso entregue ao cliente (domínio no nome do cliente).
