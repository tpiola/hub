# Inventário canônico do ecossistema

Atualizado em 14 de agosto de 2026 após auditoria cruzada entre GitHub e Vercel.

## Produção

| Produto | GitHub canônico | Vercel canônica | Domínio | Situação |
|---|---|---|---|---|
| Rei das Vendas | `reidasvendas` | `reidasvendas` | `reidasvendas.com.br` | Consolidar duplicados |
| Thiago Piola | `thiagopiola` | `thiagopiola_repo` → renomear | a confirmar | Duas Vercel |
| SaúdeGPT | `saudegpt` | `saudegpt` | a confirmar | Excluir `saudegpt-full` |
| Sentinela Saúde Ambiental | `sentinela-saude-ambiental` | `site` → renomear | `www.sentinelasaudeambiental.com.br` | Duas Vercel |
| Thiago Lab | `thiago-lab` | `thiago-lab` | a confirmar | Canônico |
| Terapeuta | `terapeuta` | `terapeuta-next` → renomear | a confirmar | Nome divergente |
| Keeus | `valdecikeeus` | `valdecikeeus` | a confirmar | Comparar legado |
| Chuteiras | `chuteiras` | `chuteiras` | a confirmar | Canônico |
| Drogalar | `drogalar` | `drogalar` | a confirmar | Canônico |
| SPES | `spes` | `epes` → renomear | `spes.blog` | Nome incorreto |

## Projetos Vercel a remover

### Duplicação comprovada

- `reidasvendas-site`: mesmo repositório e commit de `reidasvendas`.
- `0d6e4079e367`: mesmo repositório e commit de `reidasvendas`.
- `rv-premium`: implantação paralela antiga sem vínculo Git atual.
- `thiagopiola-site`: mesmo repositório e commit de `thiagopiola_repo`.
- `saudegpt-full`: mesmo repositório e commit de `saudegpt`.

### Verificação antes de remoção

- `keeus-inspired-site`: sem vínculo Git exposto; comparar com `valdecikeeus`.
- `second-brain`: não possui repositório GitHub identificado; exportar ou localizar a fonte.
- `sentinela-saude-ambiental`: mesmo repositório e commit de `site`, mas o domínio está em `site`; preservar o projeto que controla o domínio até completar a troca nominal.
- `tpiolalocal`: projeto documentado como pausado, embora ainda possua produção ativa.

## GitHub a arquivar

### Marcadores vazios de domínio

- `thiagopiola.com.br`
- `reidasvendas.com.br`
- `thiagolab.com`
- `saudegpt.com`
- `sentinelasaudeambiental.com.br`
- `keeus`
- `spes.blog`

### Legados já substituídos

- `sentinela-dedetizadora`
- `thiago-ai-studio`
- `vendas-ai-studio`
- `catolico-ai-studio`
- `thiago`
- `site.ai.studio`

## Política obrigatória

1. Um produto possui um repositório canônico.
2. Um repositório publicável possui no máximo um projeto Vercel permanente.
3. O nome do projeto Vercel deve coincidir com o repositório.
4. Domínios não viram repositórios vazios.
5. `main` é a única branch de produção e deve ser protegida.
6. Toda mudança entra por pull request com CI aprovado.
7. Branches integradas ou abandonadas são removidas após classificação.
8. Projetos pausados são desconectados da produção.
9. Protótipos recebem prefixo ou tópico `experimental`.
10. Este inventário é atualizado antes de criar, renomear, arquivar ou publicar qualquer projeto.

## Critério de conclusão

- nenhuma origem Git dispara mais de um projeto Vercel;
- nenhum projeto Vercel permanente existe sem fonte Git identificada;
- nenhum domínio oficial depende de projeto com nome genérico;
- todos os repositórios ativos possuem README, política de segurança, CI e branch protegida;
- legados permanecem arquivados, não misturados aos produtos ativos.
