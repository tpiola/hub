# Inventário de infraestrutura — 13 de julho de 2026

> Documento de controle. Nenhum recurso deve ser excluído apenas com base no nome. Toda exclusão exige backup, identificação do proprietário e confirmação de que não atende domínio, API, banco, automação, e-mail ou cliente.

## Objetivo

Consolidar o GitHub como fonte de código, a Vercel como plataforma padrão para sites e aplicações web compatíveis e desativar a VPS da Hostinger somente depois de provar que nenhum serviço necessário depende dela.

## GitHub

Foram encontrados 16 repositórios acessíveis na conta `tpiola`.

### Núcleo protegido

| Repositório | Função proposta | Ação |
|---|---|---|
| `hub` | Controle do ecossistema e documentação operacional | Manter e atualizar |
| `piola-site-template` | Fundação para a futura fábrica de sites | Manter e reconstruir |
| `reidasvendas` | Site e plataforma institucional | Manter |
| `thiagopiola` | Site profissional de Thiago Piola | Manter |
| `saudegpt` | Plataforma principal SaúdeGPT | Manter como canônico |
| `sentinela-saude-ambiental` | Site da Sentinela | Manter |

### Projetos ativos ou demonstrativos

| Repositório | Situação inicial | Ação proposta |
|---|---|---|
| `thiago-lab` | Aplicação Next.js com Supabase e funções | Revisar antes da migração definitiva |
| `terapeuta` | Site demonstrativo/cliente | Manter se ainda fizer parte do portfólio |
| `valdecikeeus` | E-commerce demonstrativo | Manter se ainda fizer parte do portfólio |
| `chuteiras` | E-commerce demonstrativo | Manter se ainda fizer parte do portfólio |
| `drogalar` | Projeto de farmácia em desenvolvimento | Corrigir deploy ou arquivar |
| `tpiolalocal` | Plataforma antiga em Next.js 14 | Comparar com a nova fábrica antes de manter |
| `saudegpt-core` | Núcleo separado do SaúdeGPT | Comparar e consolidar ou arquivar |

### Repositórios já arquivados

| Repositório | Evidência | Ação proposta |
|---|---|---|
| `saudegpt-nutricao` | Conteúdo já consolidado no `saudegpt` | Exportar backup e excluir após aprovação |
| `saudegpt-fisioterapia` | Conteúdo já consolidado no `saudegpt` | Exportar backup e excluir após aprovação |
| `saudegpt-psicologia` | Conteúdo já consolidado no `saudegpt` | Exportar backup e excluir após aprovação |

## Vercel

Foram encontrados 15 projetos na equipe `thiagopiola`.

### Protegido

| Projeto | Estado observado | Domínio próprio | Ação |
|---|---|---|---|
| `reidasvendas` | Deployment de produção READY | `reidasvendas.com.br` | Não excluir |

### Manter ou validar como projeto canônico

| Projeto | Estado observado | Ação proposta |
|---|---|---|
| `thiagopiola_repo` | READY | Validar como destino de `thiagopiola.com.br` |
| `terapeuta-next` | READY | Manter se o projeto continuar ativo |
| `saudegpt` | READY | Manter como candidato canônico |
| `valdecikeeus` | READY | Manter se o projeto continuar ativo |
| `thiago-lab` | READY | Validar rotas, funções e domínio |
| `chuteiras` | READY | Manter se o projeto continuar ativo |
| `tpiolalocal` | READY | Revisar utilidade |
| `drogalar` | BLOCKED | Reparar ou recriar a partir do GitHub |

### Candidatos a consolidação ou exclusão

| Projeto | Motivo | Condição para excluir |
|---|---|---|
| `thiagopiola-site` | Sem deployment e sem domínio | Confirmar que não contém configuração exclusiva |
| `rv-premium` | Experimento sem domínio próprio | Comparar com `reidasvendas` |
| `keeus-inspired-site` | Possível duplicação de `valdecikeeus` | Comparar deployments e origem Git |
| `saudegpt-full` | Possível duplicação de `saudegpt` | Comparar variáveis, branch e conteúdo |
| `site` | Nome genérico e deployment ERROR | Identificar repositório de origem |
| `second-brain` | Sem repositório GitHub correspondente no inventário | Exportar código/configuração antes de qualquer exclusão |

## Domínios públicos identificados

| Domínio | Estado público observado | Destino Vercel confirmado nesta equipe |
|---|---|---|
| `reidasvendas.com.br` | Ativo | Sim |
| `thiagopiola.com.br` | Ativo | Não confirmado |
| `saudegpt.com` | Ativo | Não confirmado |
| `sentinelasaudeambiental.com.br` | Ativo | Não confirmado |
| `thiagolab.com` | Apresentou erro durante a verificação | Não confirmado |

A ausência do domínio na equipe Vercel conectada pode significar que ele ainda aponta para a Hostinger, está em outra equipe Vercel ou usa outro provedor. O DNS precisa ser confirmado antes de qualquer desligamento.

## Fontes de inconsistência encontradas

- Documentação antiga aponta para nomes de repositórios que não correspondem ao inventário atual.
- Existem deployments e aliases associados ao nome histórico `thiagoso`.
- Há múltiplos projetos Vercel para SaúdeGPT e para experiências ligadas ao Rei das Vendas.
- O `hub` ainda descreve comandos de deploy por Docker/VPS.
- Existem pull requests antigos que foram superados por mudanças posteriores, mas continuam abertos.
- Alguns repositórios públicos expõem detalhes operacionais e devem passar por revisão de segurança.

## Regra de fonte única

Cada produto deve ter exatamente:

1. Um repositório canônico no GitHub.
2. Um projeto canônico na Vercel.
3. Um domínio de produção documentado.
4. Uma branch `main` protegida.
5. Uma lista de variáveis de ambiente sem valores secretos.
6. Um proprietário e um status definidos.
7. Um runbook de deploy e recuperação.
