# Candidatos a consolidação e exclusão

## Estados

- **PROTEGIDO:** não excluir.
- **REVISAR:** comparar conteúdo, domínio, variáveis e histórico.
- **CANDIDATO:** pode ser excluído após backup e confirmação.
- **BLOQUEADO:** não excluir até localizar código, dados ou proprietário.

## GitHub

| Recurso | Estado | Motivo | Ação antes da exclusão |
|---|---|---|---|
| `hub` | PROTEGIDO | Controle do ecossistema | Atualizar documentação |
| `piola-site-template` | PROTEGIDO | Base da fábrica futura | Modernizar |
| `reidasvendas` | PROTEGIDO | Produção | Nenhuma exclusão |
| `thiagopiola` | PROTEGIDO | Produção | Limpar assets e PRs |
| `saudegpt` | PROTEGIDO | Produto principal | Consolidar duplicações |
| `sentinela-saude-ambiental` | PROTEGIDO | Site de empresa | Migrar domínio e remover legado Docker depois |
| `thiago-lab` | REVISAR | Pode conter produto, APIs e automações | Auditar uso e domínio |
| `saudegpt-core` | REVISAR | Possível duplicação ou pacote futuro | Comparar com `saudegpt` |
| `tpiolalocal` | REVISAR | Stack antiga e função incerta | Comparar com fábrica futura |
| `terapeuta` | REVISAR | Projeto demonstrativo/cliente | Confirmar uso comercial |
| `valdecikeeus` | REVISAR | Projeto demonstrativo/cliente | Confirmar uso comercial |
| `chuteiras` | REVISAR | Projeto demonstrativo/cliente | Confirmar uso comercial |
| `drogalar` | REVISAR | Projeto em desenvolvimento | Corrigir ou arquivar |
| `saudegpt-nutricao` | CANDIDATO | Já arquivado e consolidado | Exportar ZIP e confirmar páginas no `saudegpt` |
| `saudegpt-fisioterapia` | CANDIDATO | Já arquivado e consolidado | Exportar ZIP e confirmar páginas no `saudegpt` |
| `saudegpt-psicologia` | CANDIDATO | Já arquivado e consolidado | Exportar ZIP e confirmar páginas no `saudegpt` |

## Vercel

| Projeto | Estado | Motivo | Ação antes da exclusão |
|---|---|---|---|
| `reidasvendas` | PROTEGIDO | Possui domínio de produção | Não excluir |
| `thiagopiola_repo` | REVISAR | Candidato canônico | Associar/confirmar domínio |
| `saudegpt` | REVISAR | Candidato canônico | Comparar com `saudegpt-full` |
| `terapeuta-next` | REVISAR | Deployment funcional | Confirmar uso |
| `valdecikeeus` | REVISAR | Deployment funcional | Confirmar uso |
| `thiago-lab` | REVISAR | Deployment funcional | Confirmar domínio e APIs |
| `chuteiras` | REVISAR | Deployment funcional | Confirmar uso |
| `tpiolalocal` | REVISAR | Deployment funcional, produto incerto | Confirmar utilidade |
| `drogalar` | REVISAR | Deployment bloqueado | Reparar ou recriar |
| `thiagopiola-site` | CANDIDATO | Sem deployment e sem domínio | Verificar env/configuração |
| `rv-premium` | CANDIDATO | Experimento sem domínio | Comparar com `reidasvendas` |
| `keeus-inspired-site` | CANDIDATO | Possível duplicação | Comparar com `valdecikeeus` |
| `saudegpt-full` | CANDIDATO | Possível duplicação | Comparar com `saudegpt` |
| `site` | CANDIDATO | Deployment ERROR e nome genérico | Identificar origem |
| `second-brain` | BLOQUEADO | Não há repo GitHub correspondente no inventário | Exportar projeto e localizar fonte |

## Pull requests

Não fechar ou mesclar em massa. Aplicar estas regras:

1. PR já incorporado por outro commit: fechar como superseded.
2. PR antigo com grande refatoração: comparar com `main` antes de qualquer merge.
3. PR de dependência major: testar isoladamente.
4. PR que contém segredo em descrição ou comentário: revogar segredo e solicitar remoção do histórico visível.
5. PR de projeto cliente: confirmar com o proprietário antes de fechar.

### Filas prioritárias

- `thiagopiola`: PRs antigos e mutuamente sobrepostos.
- `reidasvendas`: Dependabot e PRs de auditoria/performance ainda abertos.
- `sentinela-saude-ambiental`: vários PRs antigos provavelmente superados por versões posteriores.
- `drogalar`: PR aberto descrevendo stack diferente da stack atual.

## Aprovação de exclusão

A exclusão final deve ser autorizada por uma lista exata, por exemplo:

```text
APROVO EXCLUIR:
- GitHub: tpiola/saudegpt-nutricao
- GitHub: tpiola/saudegpt-fisioterapia
- GitHub: tpiola/saudegpt-psicologia
- Vercel: thiagopiola-site
```

Autorizações genéricas como “apagar tudo que não precisa” não são suficientes para recursos sem dono ou com dados desconhecidos.
