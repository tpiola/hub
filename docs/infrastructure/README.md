# Reorganização de infraestrutura

Este diretório é a fonte de verdade para a reorganização do GitHub, Vercel e Hostinger.

## Documentos

1. [Inventário de GitHub e Vercel](./INVENTORY-2026-07-13.md)
2. [Plano de migração para Vercel](./MIGRATION-TO-VERCEL.md)
3. [Checklist de desativação da VPS](./VPS-DECOMMISSION.md)
4. [Candidatos a consolidação e exclusão](./DELETION-CANDIDATES.md)
5. [Ações urgentes de segurança](./SECURITY-ACTIONS.md)

## Sequência oficial

```text
Segurança
→ inventário da VPS
→ definir repositórios canônicos
→ corrigir projetos Vercel
→ migrar domínios individualmente
→ observar produção
→ parar containers migrados
→ remover dados somente após backup
→ cancelar a VPS se estiver vazia
```

## Regra de operação

Nenhuma exclusão é aprovada por inferência. Recursos são removidos somente quando constarem em um manifesto com nome exato, backup confirmado e autorização explícita.
