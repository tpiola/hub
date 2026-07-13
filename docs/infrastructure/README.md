# Reorganização de infraestrutura

Este diretório é a fonte de verdade para a reorganização do GitHub, Vercel e Hostinger.

## Documentos

1. [Auditoria profunda do ecossistema](./DEEP-AUDIT-2026-07-13.md)
2. [Inventário de GitHub e Vercel](./INVENTORY-2026-07-13.md)
3. [Política operacional somente gratuita](./FREE-ONLY-POLICY.md)
4. [Plano de migração para Vercel](./MIGRATION-TO-VERCEL.md)
5. [Checklist de desativação da VPS](./VPS-DECOMMISSION.md)
6. [Candidatos a consolidação e exclusão](./DELETION-CANDIDATES.md)
7. [Ações urgentes de segurança](./SECURITY-ACTIONS.md)

## Sequência oficial

```text
Segurança
→ inventário da VPS
→ definir repositórios canônicos
→ corrigir CI e builds
→ corrigir projetos Vercel
→ migrar domínios individualmente
→ observar produção
→ remover projetos duplicados
→ parar containers migrados
→ remover dados somente após backup
→ cancelar a VPS se estiver vazia
```

## Regra de operação

Nenhuma exclusão é aprovada por inferência. Recursos são removidos somente quando constarem em um manifesto com nome exato, backup confirmado e autorização explícita.

Nenhum recurso pago é ativado automaticamente. Respostas de ferramentas contendo exigência de upgrade, premium, billing ou cobrança por uso encerram aquela operação.
