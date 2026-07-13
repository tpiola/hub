# Política operacional — somente recursos gratuitos

## Regra principal

Nenhuma ferramenta, integração, modelo, observabilidade ou automação pode gerar cobrança sem uma decisão explícita e separada do proprietário.

## Permitido por padrão

- GitHub e GitHub Actions dentro das cotas incluídas na conta.
- Vercel Git Integration, previews e recursos já incluídos no plano atual.
- Ferramentas locais e open source: Node.js, pnpm, Next.js, React, TypeScript, ESLint, Prettier, Playwright, Vitest e Lighthouse.
- SVG, CSS, Canvas e assets próprios para criação visual.
- Google Search Console, Google Business Profile e Bing Webmaster Tools nos recursos gratuitos disponíveis.
- Revisões automáticas gratuitas apenas dentro das cotas já incluídas.

## Bloqueado por padrão

- Magnific, pois o MCP respondeu exigindo conta premium.
- CodeRabbit com cobrança por arquivo ou revisão baseada em uso.
- Expansão paga de logs ou observabilidade na Vercel.
- APIs de IA pagas, créditos comprados e geração cobrada por imagem ou token.
- n8n Cloud, bancos ou serviços SaaS pagos sem autorização específica.
- Compra de domínio, storage, tráfego adicional ou add-ons automáticos.

## Magnific

A integração foi alcançada e respondeu, portanto o MCP está instalado e autenticando a chamada. Entretanto, a operação retornou exigência de conta premium. Resultado operacional:

- Integração tecnicamente alcançável.
- Uso indisponível no modo gratuito.
- Nenhuma geração executada.
- Nenhum crédito ou cobrança acionado.
- Magnific não faz parte da arquitetura oficial enquanto exigir pagamento.

## Substituições gratuitas de alta qualidade

| Necessidade | Solução padrão |
|---|---|
| Otimizar imagens | Sharp, Squoosh CLI ou ImageMagick local |
| Criar ícones e grafismos | SVG próprio, Lucide e CSS |
| Imagens de interface | Capturas reais do produto e mockups em CSS |
| Testes visuais | Playwright screenshots |
| Auditoria de performance | Lighthouse e Web Vitals |
| Revisão de código | ESLint, TypeScript, testes e revisão humana |
| CI/CD | GitHub Actions + Vercel Git Integration |
| SEO | Metadata nativa, sitemap, robots, JSON-LD e Search Console |

## Gate de cobrança

Qualquer ferramenta que retornar `billing`, `premium`, `upgrade`, `credits`, `usage-based` ou equivalente deve ser interrompida. O evento deve ser registrado no relatório, sem tentativa de contornar o limite.
