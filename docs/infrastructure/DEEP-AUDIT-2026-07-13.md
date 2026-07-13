# Auditoria profunda do ecossistema — 13 de julho de 2026

## Escopo analisado

- 16 repositórios GitHub.
- 15 projetos Vercel.
- Deployments, origem Git/CLI, domínios, erros de build e erros de runtime disponíveis sem cobrança.
- Integração Magnific MCP.
- CI, scripts de validação, segurança administrativa e duplicações.

## Resumo executivo

O ecossistema possui bons projetos, porém ainda não está em estado de encerramento. Os maiores riscos atuais são:

1. Produção do Rei das Vendas servida por deployment manual, divergente do GitHub.
2. Credencial administrativa padrão incorporada no SaúdeGPT.
3. Projetos duplicados na Vercel recebendo deploy de cada push.
4. Sentinela ligada a um projeto Vercel com Root Directory incorreto.
5. Thiago Lab com domínio apresentando erro e dependência histórica de VPS.
6. Repositórios demonstrativos muito grandes por causa de mídia.
7. Falta de CI uniforme em grande parte dos repositórios.
8. Documentação e PRs antigos contradizendo o estado atual.

## Matriz GitHub

| Repositório | Classe | Estado | Melhoria prioritária |
|---|---|---|---|
| `reidasvendas` | Produção | Crítico | Restaurar deploy Git, integrar limpeza de assets e validar domínio |
| `thiagopiola` | Produção | Ativo | CI com lint, typecheck e build; consolidar PRs antigos |
| `saudegpt` | Produção | Crítico | Remover credencial padrão, corrigir dados públicos e consolidar Vercel |
| `sentinela-saude-ambiental` | Produção/cliente | Ativo | Projeto Vercel canônico com root `site`; depois migrar domínio |
| `thiago-lab` | Produto interno | Instável | Corrigir domínio, separar tarefas serverless de serviços contínuos |
| `hub` | Governança | Ativo | Tornar fonte única do inventário e runbooks |
| `piola-site-template` | Fundação | Desatualizado | Atualizar stack e criar CI antes de gerar novos clientes |
| `terapeuta` | Demonstração/cliente | Preview | Adicionar CI e definir se será publicado ou arquivado |
| `valdecikeeus` | Demonstração/cliente | Pesado | Auditar aproximadamente 260 MB de assets e separar mídia |
| `chuteiras` | Demonstração/cliente | Pesado | Auditar aproximadamente 260 MB de assets e separar mídia |
| `drogalar` | Desenvolvimento | Bloqueado | Corrigir projeto Vercel e alinhar stack documentada com o código |
| `tpiolalocal` | Legado | Desatualizado | Escolher entre upgrade ou arquivamento |
| `saudegpt-core` | Possível duplicação | Indefinido | Comparar com `saudegpt` e arquivar se não houver código exclusivo |
| `saudegpt-nutricao` | Consolidado | Arquivado | Manter como backup ou excluir após exportação |
| `saudegpt-fisioterapia` | Consolidado | Arquivado | Manter como backup ou excluir após exportação |
| `saudegpt-psicologia` | Consolidado | Arquivado | Manter como backup ou excluir após exportação |

## Matriz Vercel

| Projeto | Origem observada | Estado | Decisão |
|---|---|---|---|
| `reidasvendas` | CLI em produção; Git falhando | Crítico | Corrigir Git e substituir deployment manual |
| `thiagopiola_repo` | Git/Next.js | READY | Candidato canônico; confirmar domínio próprio |
| `thiagopiola-site` | Nenhum deployment | Vazio | Excluir |
| `rv-premium` | CLI | Experimento | Excluir após capturar referência visual necessária |
| `saudegpt` | Git `tpiola/saudegpt` | READY | Manter como canônico |
| `saudegpt-full` | Mesmo repo, branch e commit de `saudegpt` | Duplicado comprovado | Copiar variáveis exclusivas e excluir |
| `site` | Git Sentinela, root incorreto | ERROR | Excluir e criar projeto canônico com root `site` |
| `drogalar` | Projeto sem framework detectado | BLOCKED | Reparar/recriar |
| `valdecikeeus` | Git/Next.js | READY | Manter enquanto projeto estiver ativo |
| `keeus-inspired-site` | CLI | Experimento duplicado provável | Excluir após comparação visual |
| `terapeuta-next` | Git/Next.js | READY | Manter se houver finalidade definida |
| `thiago-lab` | Git/Next.js | READY | Validar domínio e APIs |
| `chuteiras` | Git/Next.js | READY | Manter se houver finalidade definida |
| `tpiolalocal` | Git/Next.js | READY | Revisar ou arquivar |
| `second-brain` | CLI, sem origem Git identificada | Órfão | Bloqueado para exclusão até exportar código |

## Exclusões comprovadas

### Vercel — prontas tecnicamente

1. `thiagopiola-site`: sem deployment e sem domínio.
2. `site`: deployment quebrado do repositório Sentinela com Root Directory incorreto.
3. `saudegpt-full`: mesmo repositório, branch e commit do projeto `saudegpt`.
4. `rv-premium`: deployment manual sem domínio próprio e sem vínculo Git.
5. `keeus-inspired-site`: deployment manual sem domínio próprio e provável duplicação do projeto Keeus.

Antes de excluir os itens 3, 4 e 5, copiar a lista de variáveis e registrar qualquer asset visual que não esteja no GitHub.

### Bloqueado

- `second-brain`: não excluir até localizar/exportar o código-fonte e as variáveis.
- Projetos com domínio próprio ou cliente identificado.
- VPS Hostinger antes do inventário e backup.

## Ações de código executadas

- PR de infraestrutura no `hub` com inventário e runbooks.
- PR de segurança no SaúdeGPT para bloquear credenciais padrão em produção.
- PR de CI no portfólio Thiago Piola.
- Correção da configuração de runtime Vercel incorporada ao PR de limpeza do Rei das Vendas.
- PR com segredo exposto teve descrição sanitizada e foi fechado.

## Critério de projeto finalizado

Um projeto só recebe status `FINALIZADO` quando:

- `main` passa lint, typecheck, testes e build.
- Deployment de produção vem da integração Git.
- Domínio canônico aponta para o projeto correto.
- Não existe credencial padrão ou segredo versionado.
- Formulários e integrações foram testados.
- Sitemap, robots, metadata e JSON-LD estão corretos.
- Existe proprietário, finalidade e runbook.
- Não há projeto Vercel duplicado recebendo deploy.

Nenhum status deve ser inferido apenas porque o deployment está `READY`.
