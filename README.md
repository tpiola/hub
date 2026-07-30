# TPiola Hub

Fonte única de governança dos projetos mantidos na conta [`@tpiola`](https://github.com/tpiola).

Este repositório não é uma aplicação para deploy. Ele documenta quais projetos são oficiais, quais podem ser publicados e quais existem apenas para histórico, template ou experimentação.

## Projetos oficiais

| Repositório | Finalidade | Estado | Deploy independente |
|---|---|---:|---:|
| [`reidasvendas`](https://github.com/tpiola/reidasvendas) | Site, design system, APIs e automações do Rei das Vendas | Ativo | Sim |
| [`thiagopiola`](https://github.com/tpiola/thiagopiola) | Portfólio profissional | Produção | Sim |
| [`saudegpt`](https://github.com/tpiola/saudegpt) | Plataforma principal SaúdeGPT | Ativo | Sim |
| [`sentinela-saude-ambiental`](https://github.com/tpiola/sentinela-saude-ambiental) | Site oficial da Sentinela | Produção | Sim |
| [`thiago-lab`](https://github.com/tpiola/thiago-lab) | Laboratório de produtos e ferramentas | Ativo | Sim |
| [`terapeuta`](https://github.com/tpiola/terapeuta) | Projeto de cliente do nicho terapêutico | Ativo | Sim |
| [`valdecikeeus`](https://github.com/tpiola/valdecikeeus) | E-commerce Keeus | Ativo | Sim |
| [`chuteiras`](https://github.com/tpiola/chuteiras) | E-commerce de chuteiras | Ativo | Sim |
| [`drogalar`](https://github.com/tpiola/drogalar) | Projeto do segmento farmacêutico | Desenvolvimento | Sim |
| [`spes`](https://github.com/tpiola/spes) | Jornada e comunidade SPES | Ativo | Sim |

## Infraestrutura e componentes

| Repositório | Papel | Regra |
|---|---|---|
| [`hub`](https://github.com/tpiola/hub) | Catálogo e governança | Não publicar |
| [`piola-site-template`](https://github.com/tpiola/piola-site-template) | Base para novos projetos | Usar como template; não publicar diretamente |
| [`saudegpt-core`](https://github.com/tpiola/saudegpt-core) | Biblioteca experimental | Não conectar à Vercel enquanto não for consumida pelo projeto principal |
| [`tpiolalocal`](https://github.com/tpiola/tpiolalocal) | Protótipo de CRM local | Pausado; não publicar até retomada |

## Verticais incorporadas ao SaúdeGPT

Os repositórios abaixo estão arquivados e não devem gerar deploy separado:

- `saudegpt-nutricao`
- `saudegpt-fisioterapia`
- `saudegpt-psicologia`

As especificações funcionais ficam centralizadas no repositório `saudegpt`.

## Repositórios descontinuados

Os projetos abaixo foram substituídos por fontes oficiais. Seus pontos de entrada de deploy foram removidos quando existiam:

| Legado | Substituído por |
|---|---|
| `sentinela-dedetizadora` | `sentinela-saude-ambiental` |
| `thiago-ai-studio` | `thiagopiola` |
| `vendas-ai-studio` | `reidasvendas` |
| `catolico-ai-studio` | `spes` |
| `thiago` | `thiagopiola` |
| `site.ai.studio` | `hub` |

Esses repositórios podem ser excluídos definitivamente nas configurações do GitHub após a conferência final do proprietário.

## Regra de publicação

1. Cada domínio possui um único repositório oficial.
2. Apenas projetos marcados como “Deploy independente: Sim” devem ser conectados à Vercel.
3. Template, biblioteca, catálogo, protótipo pausado e legado não recebem projeto Vercel.
4. Alterações entram no `main` somente após `lint`, `typecheck` e `build`, quando os scripts existirem.
5. Variáveis privadas permanecem na plataforma de deploy e nunca entram no Git.

Detalhes e critérios de manutenção: [`PROJECT.md`](./PROJECT.md).