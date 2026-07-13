# Ações urgentes de segurança

## Prioridade crítica

### 1. Credencial de API exposta em histórico de pull request

Foi identificada uma credencial de provedor de IA colada no texto de um pull request antigo. Mesmo que a implementação não tenha gravado a chave em arquivo, ela deve ser considerada comprometida.

Ações:

- Revogar a chave imediatamente no provedor.
- Criar uma nova chave com escopo mínimo.
- Atualizar somente os ambientes que realmente utilizam a chave.
- Solicitar remoção ou edição do conteúdo público do PR quando possível.
- Verificar logs de uso e cobranças desde a exposição.

### 2. Credencial administrativa divulgada em PR

Um pull request antigo documenta credenciais administrativas de teste para o SaúdeGPT.

Ações:

- Trocar usuário e senha em todos os ambientes.
- Invalidar sessões existentes.
- Remover credenciais padrão do código e da documentação.
- Armazenar credenciais somente em variáveis protegidas.
- Adotar autenticação com hash, rate limiting e segundo fator quando aplicável.

### 3. Token e detalhes da Hostinger

Scripts antigos fazem referência a um token local da Hostinger e ao IP da VPS.

Ações:

- Rotacionar o token da Hostinger.
- Remover scripts obsoletos após a migração.
- Não versionar IPs, IDs internos de painel ou caminhos de tokens quando não forem necessários.
- Revisar logs de API da Hostinger.

## Revisão de repositórios públicos

Revisar especialmente:

- `thiagopiola`
- `saudegpt`
- `thiago-lab`
- `valdecikeeus`
- `piola-site-template`

Procurar:

- `.env` e variantes.
- Tokens.
- Senhas.
- Chaves privadas.
- URLs de banco com credenciais.
- Service role keys.
- Segredos de webhook.
- Credenciais administrativas.
- Backups e dumps.
- Arquivos `.vercel`.
- Dados de clientes.

## Comandos de busca local recomendados

Executar em clone privado, sem publicar a saída:

```bash
git grep -n -I -E '(sk-|api[_-]?key|secret|token|password|passwd|service[_-]?role|private[_-]?key|database_url)'

git log -p --all -- .env .env.local .env.production '*.pem' '*.key'
```

Também usar secret scanning do GitHub e revisar alertas do Dependabot.

## Padrão futuro

- `.env.example` contém apenas nomes e descrições.
- Segredos ficam no Vercel, GitHub Actions ou cofre de segredos.
- Cada projeto usa credenciais próprias.
- Preview não reutiliza credenciais de produção quando não for necessário.
- Chaves são rotacionadas periodicamente.
- Logs nunca exibem tokens, senhas ou conteúdo sensível.
- Toda integração externa possui timeout e escopo mínimo.

## Condição para continuar a migração

Nenhum projeto com credencial exposta deve ser promovido ou migrado para domínio de produção antes da rotação e da validação dos novos segredos.
