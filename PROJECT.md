# 🜂 Piola.Build — Sites Premium (GitHub Project v2)

> **Board central de todos os repositórios de sites e plataformas piola.build.**
> [🔗 Abrir Project no GitHub](https://github.com/users/tpiola/projects/3)

---

## 📊 Estrutura do Project

O Project **"Piola.Build — Sites Premium"** organiza todos os 15+ repositórios da conta [`@tpiola`](https://github.com/tpiola) com **8 campos customizados** para gestão profissional:

| Campo | Tipo | Valores |
|---|---|---|
| **Status** | select | Todo · In Progress · Done |
| **Nicho** | select | Farmácia/Saúde · Odontologia · Restaurante · Fitness · Advocacia · Estética · E-commerce · Terapia · Plataforma/SaaS · Institucional |
| **Stack** | select | Next.js 15 · Next.js+Supabase · Vite SPA · Monorepo Turborepo · Python/FastAPI |
| **Fase** | select | 📋 Backlog · 🎨 Design · 🔨 Dev · 🧪 Homologação · 🚀 Produção · 🔧 Manutenção · ⏸️ Pausado |
| **Pacote** | select | STARTER R$2.5K · PRO R$5K · PREMIUM R$10K · Interno |
| **URL Live** | text | Domínio publicado |
| **Cliente** | text | Nome do cliente/empresa |
| **HERMES-Score** | number | Score 0-100 do lead/projeto |
| **MRR (R$)** | number | Receita recorrente mensal |

---

## 🏷️ Sistema de Labels (padronizado em todos os repos)

**27 labels** aplicadas automaticamente em cada repositório do ecossistema:

### Prioridade
`priority/critical` · `priority/high` · `priority/medium` · `priority/low`

### Tipo
`type/feature` · `type/bug` · `type/design` · `type/copy` · `type/seo` · `type/perf` · `type/security` · `type/deploy` · `type/docs`

### Stack
`stack/nextjs` · `stack/supabase` · `stack/tailwind` · `stack/vercel`

### Cliente (Pacote)
`cliente/premium` · `cliente/pro` · `cliente/starter`

### Fase
`fase/design` · `fase/dev` · `fase/qa` · `fase/producao` · `fase/manutencao`

### Hermes
`hermes/neurobuild` · `hermes/auto-deploy`

---

## 🏷️ Topics dos Repositórios

Todos os repos têm o topic `piola-build` + topics específicos do nicho/stack.
Busque por `topic:piola-build` no GitHub para ver o ecossistema:
[🔗 github.com/search?q=topic:piola-build+org:tpiola](https://github.com/search?q=topic%3Apiola-build+user%3Atpiola)

---

## 🚀 Template Repository

**[tpiola/piola-site-template](https://github.com/tpiola/piola-site-template)** — clique em **"Use this template"** para clonar um novo site de cliente em 1 clique.

O template já vem com:
- Next.js 15 (App Router) + TypeScript strict
- Tailwind CSS 4 + shadcn/ui + Framer Motion
- Estrutura de landing page Hermes (Hero → Preço → CTA)
- WhatsApp flutuante + Schema LocalBusiness
- LGPD (banner + política + rota /excluir-dados)
- Supabase-ready (auth + RLS helpers)
- Stripe + Mercado Pago (Pix) stubs
- CI/CD (typecheck + lint + build)
- Issue templates + PR template com checklist Error-Proof

---

## 📋 Repositórios Mapeados (15)

| Repo | Nicho | Stack | Fase | Pacote |
|---|---|---|---|---|
| [thiagopiola](https://github.com/tpiola/thiagopiola) | Institucional | Next.js 15 | 🚀 Produção | Interno |
| [drogalar](https://github.com/tpiola/drogalar) | Farmácia/Saúde | Next.js 15 | 🔨 Dev | PREMIUM |
| [saudegpt](https://github.com/tpiola/saudegpt) | Plataforma/SaaS | Next.js+Supabase | 🚀 Produção | Interno |
| [saudegpt-core](https://github.com/tpiola/saudegpt-core) | Plataforma/SaaS | Next.js+Supabase | 🔨 Dev | Interno |
| [saudegpt-psicologia](https://github.com/tpiola/saudegpt-psicologia) | Terapia/Psicologia | Next.js+Supabase | 🔨 Dev | Interno |
| [saudegpt-fisioterapia](https://github.com/tpiola/saudegpt-fisioterapia) | Fitness/Esporte | Next.js+Supabase | 🔨 Dev | Interno |
| [saudegpt-nutricao](https://github.com/tpiola/saudegpt-nutricao) | Farmácia/Saúde | Next.js+Supabase | 🔨 Dev | Interno |
| [reidasvendas](https://github.com/tpiola/reidasvendas) | Plataforma/SaaS | Turborepo | 🔨 Dev | Interno |
| [sentinela-saude-ambiental](https://github.com/tpiola/sentinela-saude-ambiental) | Plataforma/SaaS | Next.js 15 | 🧪 Homologação | Interno |
| [terapeuta](https://github.com/tpiola/terapeuta) | Terapia/Psicologia | Next.js 15 | 📋 Backlog | STARTER |
| [valdecikeeus](https://github.com/tpiola/valdecikeeus) | E-commerce | Next.js 15 | 🔨 Dev | PRO |
| [chuteiras](https://github.com/tpiola/chuteiras) | E-commerce | Next.js 15 | 📋 Backlog | PRO |
| [tpiolalocal](https://github.com/tpiola/tpiolalocal) | Plataforma/SaaS | Next.js 15 | 🔨 Dev | Interno |
| [thiago-lab](https://github.com/tpiola/thiago-lab) | Plataforma/SaaS | Next.js+Supabase | 🧪 Homologação | Interno |
| [hub](https://github.com/tpiola/hub) | Plataforma/SaaS | Python/FastAPI | 🔨 Dev | Interno |

---

## 🛠️ Como usar no dia a dia

### Criar novo site de cliente
1. GitHub → `piola-site-template` → **Use this template**
2. Nome: `cliente-nome` (privado)
3. O novo repo já vem com labels, templates e CI configurados
4. Vá no Project e adicione o repo como draft item (título com emoji do nicho)
5. Preencha: Nicho · Stack · Fase · Pacote · Cliente

### Abrir issue rastreada
- Bugs → template `bug_report` (label auto `type/bug`)
- Features → template `feature_request` (label auto `type/feature`)
- Onboarding → template `client_onboarding` (label auto `hermes/neurobuild`)

### PRs
- Todo PR passa pelo checklist Error-Proof automaticamente
- CI valida: typecheck + lint + build

---

## 📈 Métricas do Ecossistema

Para consultar rapidamente (via `gh` CLI):

```bash
# Todos os repos piola.build
gh search repos --owner tpiola --topic piola-build

# Issues abertas em todos
gh search issues --owner tpiola --state open

# PRs pendentes de review
gh search prs --owner tpiola --state open --review-requested tpiola

# Todos os "Cliente Premium"
gh search issues --owner tpiola --label cliente/premium
```

---

*Configurado por Hermes Agent | piola.build | thiago.piola@cs.unifran.edu.br*
