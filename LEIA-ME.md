# Landing pages — base de trabalho

Pesquisa feita em 22/09/2026. Tudo aqui foi escrito para ser usado na criação e na venda de landing pages.

## Base de conhecimento (`base-de-conhecimento/`)
1. `01-fundamentos-e-estrutura.md` — tipos, níveis de consciência (Schwartz), anatomia das seções, teste dos 5 segundos, message match.
2. `02-web-design-e-tecnico.md` — hierarquia, tipografia, mobile primeiro, Core Web Vitals, acessibilidade, SEO, stack, checklist de QA.
3. `03-copy-e-psicologia.md` — voz do cliente, frameworks (PAS, AIDA, BAB, StoryBrand, Hormozi), títulos, psicologia **classificada por força de evidência**, ética, vendas pós-clique.
4. `04-marketing-digital-trafego-e-medicao.md` — funil, fontes de tráfego, métricas, benchmarks (com ressalvas), rastreamento (UTM, GA4, Pixel+CAPI, Consent Mode), CRO e estatística de A/B.
5. `05-legal-brasil.md` — LGPD e cookies (ANPD), CDC e Decreto 7.962, CONAR, nichos regulados, políticas de anúncios.
6. `06-orcamento-e-precificacao.md` — preços do mercado, valor-hora, horas por etapa, pacotes, recorrentes, condições, estrutura da proposta.
7. `07-briefing-e-processo.md` — questionário de 20 perguntas, etapas, definição de "pronto".
8. `08-design-visual-sem-cara-de-template.md` — método de design das skills frontend-design e taste-skill (instaladas em `~/.claude/skills`): leitura do briefing, dials, tokens, padrões de IA a evitar, checklist visual.

## Ferramentas
- `ferramentas/orcamento.html` — abre no navegador, preenche escopo e gera a proposta (imprime em PDF).

## Modelo
- `modelo/index.html` — landing page completa de serviço local (exemplo: cortinas): 11 seções, CTA de WhatsApp com a origem na mensagem, formulário com máscara, honeypot e UTMs em campos ocultos, barra fixa no celular, banner de cookies que só carrega GA4 e Pixel depois do aceite, rodapé legal. Configure pelo objeto `CFG` no fim do arquivo. Textos entre [ ] e números 0.000 são marcadores: trocar por dados reais.
- `modelo/privacidade.html` — modelo de política de privacidade.

## Fontes principais consultadas
LanderLab, Unbounce e Apexure (benchmarks) · Safira Design, Big Data University, Gabriel do Site, HTMLy, BluePaper (preços BR 2026) · web.dev/corewebvitals.io (CWV) · Guia de Cookies da ANPD e LegalSuite (LGPD) · Decreto 7.962/2013 · guias de Meta CAPI e Consent Mode v2 · The Behavioral Scientist e atticusli.com (replicação em economia comportamental) · Schwartz, *Breakthrough Advertising*; Cialdini, *Influence*; Fogg Behavior Model; Miller, *StoryBrand*; Hormozi, *$100M Offers*.

## Clientes
- **Plano Urbano** (agência de mídia exterior, Niterói/RJ, atende todo o Brasil). **Negócio fechado em 11/10/2026.** Site no ar em https://www.agenciaplanourbano.com.br: fonte em `demos/plano-urbano-v4/` (editar `src.html`, rodar `python build.py` e publicar com `firebase deploy --only hosting --project planourbano` de dentro dessa pasta). Testes: `python testes/regressao.py <url> <rodada>`. A v3 de mármore ficou em `demos/plano-urbano/` (histórico). A proposta comercial foi excluída depois do fechamento.
