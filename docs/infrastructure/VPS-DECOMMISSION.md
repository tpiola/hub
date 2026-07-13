# Checklist de desativação da VPS Hostinger

## Aviso

Não executar `rm -rf`, `docker system prune -a --volumes`, exclusão de volumes, formatação, reinstalação ou cancelamento do plano antes de concluir este documento.

A VPS pode conter mais do que sites. Vercel não substitui automaticamente bancos, n8n, workers, filas, armazenamento persistente, e-mail, VPN, proxy e serviços Docker contínuos.

## 1. Inventário somente leitura

Executar na VPS e salvar a saída em arquivo:

```bash
mkdir -p ~/infra-audit

date | tee ~/infra-audit/date.txt
hostnamectl | tee ~/infra-audit/hostname.txt
uname -a | tee ~/infra-audit/uname.txt

docker ps -a | tee ~/infra-audit/docker-ps.txt
docker compose ls | tee ~/infra-audit/docker-compose-ls.txt
docker images | tee ~/infra-audit/docker-images.txt
docker volume ls | tee ~/infra-audit/docker-volumes.txt
docker network ls | tee ~/infra-audit/docker-networks.txt

systemctl --type=service --state=running | tee ~/infra-audit/services-running.txt
ss -tulpn | tee ~/infra-audit/ports.txt

crontab -l | tee ~/infra-audit/crontab-user.txt
sudo crontab -l | tee ~/infra-audit/crontab-root.txt

sudo du -h --max-depth=2 /opt /docker /var/www /srv /home 2>/dev/null | sort -h | tee ~/infra-audit/disk-usage.txt
sudo find /etc/systemd/system -maxdepth 2 -type f | tee ~/infra-audit/custom-systemd-files.txt
```

Também registrar:

- Domínios apontando para o IP da VPS.
- Bancos em execução.
- Backups existentes.
- Diretórios com uploads.
- Certificados.
- Workflows n8n.
- Arquivos `.env` e localização dos segredos, sem copiá-los para o GitHub.
- Servidores de e-mail.
- Regras de firewall.
- Jobs agendados.

## 2. Serviços já suspeitos de dependência

### Sentinela

O repositório contém configuração Docker/Traefik e documentação de deploy Hostinger. O site Next.js deve ser validado na Vercel antes de parar o container.

### Thiago Lab

O repositório contém script de deploy para o IP da VPS e `docker-compose.yml` com Traefik. O site web pode ser compatível com Vercel, mas APIs, Supabase, scraping e tarefas longas precisam de auditoria.

### Serviços compartilhados

Confirmar especialmente:

- Traefik.
- n8n.
- Banco MySQL/Postgres.
- Redis.
- Painéis administrativos.
- Volumes Docker.
- Backups automáticos.
- Serviços nas portas 80, 443, 3000–3999, 5432, 3306, 5678 e 6379.

## 3. Backup obrigatório

Antes de qualquer parada:

1. Gerar snapshot da VPS pelo painel da Hostinger.
2. Exportar bancos com ferramentas próprias do banco.
3. Exportar workflows e credenciais do n8n de forma segura.
4. Copiar uploads e volumes persistentes.
5. Salvar arquivos de configuração e compose.
6. Registrar versões das imagens Docker.
7. Guardar o inventário em Google Drive privado.
8. Testar pelo menos uma restauração.

## 4. Manifesto de preservação

Criar uma tabela final:

| Serviço/container | Função | Domínio | Dados persistentes | Novo destino | Pode parar? |
|---|---|---|---|---|---|
| Exemplo | Site | exemplo.com | Não | Vercel | Após DNS |

Nenhum item pode ser removido sem uma linha nessa tabela.

## 5. Ordem de desligamento

1. Migrar e validar o site na Vercel.
2. Alterar DNS.
3. Observar logs e tráfego por 72 horas a sete dias.
4. Parar somente o container do site migrado.
5. Observar novamente.
6. Remover container e imagem somente após aprovação.
7. Manter volumes até o backup ser verificado.
8. Remover proxy/Traefik apenas quando nenhum domínio depender dele.
9. Cancelar a VPS somente quando nenhum serviço necessário estiver rodando.

## 6. Hostinger que pode continuar necessária

Mesmo sem VPS, a conta da Hostinger pode continuar sendo usada para:

- Registro e renovação de domínios.
- DNS.
- Caixas de e-mail.
- Backups contratados.
- Outros produtos independentes da VPS.

Não cancelar toda a conta apenas porque os sites foram para a Vercel. Cancelar somente o produto VPS depois da auditoria.

## 7. Critério de conclusão

A VPS está pronta para cancelamento quando:

- `docker ps` não mostra serviço necessário.
- Nenhum domínio resolve para o IP da VPS.
- Nenhum webhook envia requisições para ela.
- Nenhum banco necessário está nela.
- Nenhum arquivo único está nela.
- n8n e automações foram migrados ou deliberadamente mantidos em outro serviço.
- Backups e restauração foram testados.
- O período de observação foi concluído.
