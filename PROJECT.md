# Governança dos repositórios

## Objetivo

Manter uma fonte de código por produto, reduzir manutenção duplicada e impedir que versões antigas sejam publicadas por engano.

## Classificação

### Produto

Aplicação ou site com domínio, público e ciclo de manutenção próprios. Pode receber projeto independente na Vercel.

### Infraestrutura

Código ou documentação compartilhada. Não deve ser publicado como site independente.

### Template

Base usada para criar um novo repositório. O template em si não recebe domínio nem projeto de produção.

### Protótipo pausado

Código preservado para retomada futura, sem conexão ativa de deploy.

### Legado

Projeto substituído por outro repositório. Deve conter apenas aviso de descontinuação e histórico; nenhum ponto de entrada executável.

## Mapa oficial

| Produto | Repositório oficial | Observação |
|---|---|---|
| Rei das Vendas | `reidasvendas` | Monorepo com site, design system, API e automações |
| Portfólio Thiago Piola | `thiagopiola` | Substitui páginas estáticas AI Studio |
| SaúdeGPT | `saudegpt` | Plataforma principal e destino das verticais |
| Sentinela Saúde Ambiental | `sentinela-saude-ambiental` | Única fonte para site e captura de leads |
| Thiago Lab | `thiago-lab` | Laboratório de ferramentas e produtos |
| SPES | `spes` | Substitui `catolico-ai-studio` |
| Terapia | `terapeuta` | Projeto independente de cliente |
| Keeus | `valdecikeeus` | E-commerce independente |
| Chuteiras | `chuteiras` | E-commerce independente |
| Drogalar | `drogalar` | Projeto farmacêutico em desenvolvimento |

## Consolidações realizadas

- `sentinela-dedetizadora` → `sentinela-saude-ambiental`
- `thiago-ai-studio` e `thiago` → `thiagopiola`
- `vendas-ai-studio` → `reidasvendas`
- `catolico-ai-studio` → `spes`
- `saudegpt-nutricao`, `saudegpt-fisioterapia` e `saudegpt-psicologia` → especificações no `saudegpt`
- `site.ai.studio` → catálogo no `hub`

## Projetos que não devem receber deploy

- `hub`
- `piola-site-template`
- `saudegpt-core`
- `tpiolalocal`, enquanto estiver pausado
- todos os repositórios descontinuados ou arquivados

## Critérios antes de excluir um repositório

1. O repositório oficial substituto está identificado.
2. Não existe domínio, webhook, banco ou automação dependendo do legado.
3. O código relevante está no projeto oficial ou não possui valor técnico.
4. O README do legado registra o destino correto.
5. A Vercel não mantém projeto de produção conectado ao legado.

## Checklist de qualidade para projetos ativos

- script único `validate` ou equivalente;
- lint sem avisos relevantes;
- TypeScript sem erros;
- build de produção aprovado;
- `.env.example` sem segredos;
- nenhuma URL de webhook privada no frontend;
- canonical, sitemap e robots coerentes;
- apenas um projeto Vercel por produto;
- documentação curta com repositório e domínio oficiais.

## Política contra loops de deploy

- não usar commits vazios ou comentários como gatilho de redeploy;
- não manter dois repositórios ligados ao mesmo domínio;
- não duplicar `vercel.json` sem necessidade;
- corrigir a causa do build e executar uma única validação final;
- deploy é solicitado somente após o commit definitivo estar no `main`.