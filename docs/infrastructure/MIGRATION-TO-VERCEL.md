# Plano de migração para Vercel

## Princípio

A Vercel será o destino padrão para sites e aplicações Next.js, React e Vite compatíveis com funções serverless. A VPS não será desligada enquanto hospedar qualquer banco de dados, n8n, fila, worker contínuo, armazenamento local, servidor de e-mail, proxy ou integração que não tenha sido migrada.

## Ordem obrigatória

### Fase 0 — Congelamento de exclusões

- Não apagar projetos do GitHub, Vercel ou VPS.
- Não alterar DNS antes de gerar backups.
- Não cancelar Hostinger antes do período de observação.
- Não copiar arquivos `.env` para repositórios.

### Fase 1 — Segurança

- Revogar e substituir credenciais expostas em conversas, PRs ou documentação.
- Trocar credenciais administrativas divulgadas em histórico de PR.
- Rotacionar o token da Hostinger usado por scripts antigos.
- Revisar repositórios públicos em busca de segredos, IPs, senhas e tokens.
- Remover vínculos `.vercel` versionados quando existirem.

### Fase 2 — Definir projetos canônicos

| Produto | GitHub canônico proposto | Vercel canônica proposta |
|---|---|---|
| Rei das Vendas | `tpiola/reidasvendas` | `reidasvendas` |
| Thiago Piola | `tpiola/thiagopiola` | `thiagopiola_repo` |
| SaúdeGPT | `tpiola/saudegpt` | `saudegpt` |
| Sentinela | `tpiola/sentinela-saude-ambiental` | Criar ou localizar projeto canônico |
| Thiago Lab | `tpiola/thiago-lab` | `thiago-lab` |
| Terapeuta | `tpiola/terapeuta` | `terapeuta-next` |
| Drogalar | `tpiola/drogalar` | Reparar ou recriar `drogalar` |
| Valdeci/Keeus | `tpiola/valdecikeeus` | `valdecikeeus` |
| Chuteiras | `tpiola/chuteiras` | `chuteiras` |

### Fase 3 — Preparar cada repositório

Cada projeto precisa conter:

- `README.md` atualizado.
- `.env.example` sem segredos.
- `DEPLOYMENT.md`.
- `RUNBOOK.md`.
- Script `validate` executando lint, typecheck, testes e build.
- CI no GitHub.
- Configuração correta de root directory.
- Rotas de health check quando houver APIs.
- Política de rollback.

### Fase 4 — Variáveis e serviços externos

Antes do deploy, registrar para cada projeto:

- Variáveis de produção, preview e desenvolvimento.
- Banco de dados utilizado.
- Buckets e armazenamento.
- Webhooks.
- n8n.
- E-mail transacional.
- Analytics.
- Calendário.
- WhatsApp.
- APIs de IA.
- Cron jobs.
- Domínios e DNS.

Nunca migrar um domínio antes de validar essas dependências no preview.

## Ordem de migração por domínio

### 1. `thiagopiola.com.br`

- Confirmar qual infraestrutura responde atualmente.
- Validar `tpiola/thiagopiola` no projeto `thiagopiola_repo`.
- Copiar somente variáveis necessárias.
- Testar formulário, WhatsApp, SEO, sitemap e analytics.
- Associar domínio na Vercel.
- Alterar DNS.
- Observar por pelo menos 72 horas.

### 2. `saudegpt.com`

- Consolidar `saudegpt` e `saudegpt-full`.
- Confirmar banco, Notion, Supabase, autenticação e painel administrativo.
- Remover dependência de armazenamento em memória para dados permanentes.
- Rotacionar credenciais administrativas.
- Testar cadastro, aprovação, login, progresso e APIs.
- Associar domínio e observar por pelo menos sete dias.

### 3. `sentinelasaudeambiental.com.br`

- Usar o app Next.js da pasta `site`.
- Criar ou localizar projeto Vercel com root directory `site`.
- Migrar variáveis do calendário, analytics e configurações públicas.
- Verificar formulário, WhatsApp, mapa, SEO e mídia.
- Associar domínio e observar por pelo menos 72 horas.

### 4. `thiagolab.com`

- Resolver primeiro o erro público atual.
- Auditar APIs, Supabase, scraping, uploads e tarefas longas.
- Migrar somente as rotas compatíveis com serverless.
- Mover tarefas contínuas para serviço apropriado, caso existam.
- Associar domínio apenas após testes ponta a ponta.

## Testes mínimos antes do DNS

- Build de produção aprovado.
- Preview acessível.
- Todas as rotas importantes respondem.
- Formulários persistem dados.
- Webhooks são recebidos.
- E-mails são enviados.
- WhatsApp abre com mensagem correta.
- Login e área administrativa funcionam.
- Dados sobrevivem a reinicialização/cold start.
- Sitemap e robots usam o domínio correto.
- Canonical e Open Graph estão corretos.
- Mobile verificado em 360 px.
- Erros de runtime da Vercel revisados.

## Período de convivência

Durante a migração, Hostinger e Vercel devem coexistir temporariamente. A VPS só pode ser desmontada quando:

1. Todos os domínios estiverem na Vercel.
2. Não houver tráfego necessário chegando ao IP da VPS.
3. Bancos, automações e arquivos tiverem destino confirmado.
4. Backups restauráveis tiverem sido testados.
5. O período de observação terminar sem regressões.

## Resultado esperado

- Um repositório por produto.
- Um projeto Vercel por produto.
- Nenhum projeto Vercel órfão.
- Nenhum domínio dependente da VPS para servir sites.
- VPS mantida somente para serviços que realmente necessitem servidor contínuo, ou cancelada quando estiver vazia.
