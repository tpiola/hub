# 🌐 THIAGO LAB HUB — SaaS Intelligence System

> **📊 [Piola.Build — Sites Premium (GitHub Project)](https://github.com/users/tpiola/projects/3)** — board central com todos os 15+ repositórios do ecossistema, organizados por nicho, stack, fase e pacote. Detalhes: [PROJECT.md](./PROJECT.md).
>
> **🚀 [piola-site-template](https://github.com/tpiola/piola-site-template)** — template repository oficial. Clique em "Use this template" para clonar um novo site de cliente.

## Arquitetura do Ecossistema

```
┌─────────────────────────────────────────────────────┐
│              THIAGO LAB HUB (Saas)                   │
│  Conector universal de IA + Produtos Digitais        │
├─────────────────────────────────────────────────────┤
│                                                     │
│  🧠 HERMES AGENT (orquestrador central)              │
│  ├─ 🤖 DeepSeek V4 · Gemini · Claude · GPT-4.1      │
│  ├─ 🔧 47 skills instaladas (design, dev, dados)     │
│  └─ 📡 OmniRoute Gateway (48 modelos, porta 20128)   │
│                                                     │
│  📦 PRODUTOS DIGITAIS                                │
│  ├─ thiagopiola.com.br  → Authority Card Pharma      │
│  ├─ reidasvendas.com.br → Design System Pinnacle     │
│  ├─ saudegpt.com        → Sovereign Game OS          │
│  ├─ thiagolab.com       → Intelligence OS            │
│  └─ sentinelasaudeambiental.com.br                   │
│                                                     │
│  🔌 INTEGRAÇÕES                                      │
│  ├─ 📓 Notion (via API MCP)                         │
│  ├─ 📧 Gmail (leitura, envio, drafts)               │
│  ├─ ☁️ Google Drive (Docs, Sheets, Slides)           │
│  ├─ 💾 Supabase (auth, db, realtime)                 │
│  ├─ 📊 n8n (workflows de automação)                  │
│  └─ 🛒 Shopify (e-commerce)                         │
│                                                     │
│  🎨 DESIGN SYSTEMS                                   │
│  ├─ Rei das Vendas Gold (tokens, Style Dictionary)   │
│  ├─ SaúdeGPT Navy Luxury (globals.css consolidado)   │
│  ├─ Thiago Lab Intelligence OS (#06080C, #3DF5C5)     │
│  └─ Authority Card Pharma (#0B3B3C Medical Teal)     │
│                                                     │
│  📈 ANALYTICS                                        │
│  ├─ Vercel Analytics + Speed Insights                │
│  └─ PostHog (eventos, funis, retenção)               │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## Sites no Ar

| Site | URL | Stack | Status | Último Deploy |
|------|-----|-------|--------|---------------|
| Authority Card Pharma | thiagopiola.com.br | HTML/CSS puro (SSG) | ✅ Pronto para deploy |
| Rei das Vendas | reidasvendas.com.br | Vite + Tokens DS | ✅ Design System |
| SaúdeGPT | saudegpt.com | Next 16 + Game OS | ✅ 9 jogos, XP, ranking |
| Thiago Lab | thiagolab.com | Next 15 + Intelligence OS | ✅ Build 0 erros |
| Sentinela Saúde | sentinelasaudeambiental.com.br | Próximo ciclo | ⏳ |

## Habilidades Hermes Instaladas (47 skills)

### Design & UI/UX (9)
- premium-design-framework, premium-web-design, power-design, design-genius
- ui-ux-pro-max, material-design-3, google-stitch-advanced-web-design-motion-cwv
- premium-portfolio-redesign, design-plus-code

### Desenvolvimento (8)
- tailwind-css, production-saas-site-builder, vibe-coding
- mobile-first-responsive, nextjs-upgrade-workflow, subagent-driven-development
- test-driven-development, html-in-canvas-api

### DevOps & Deploy (6)
- docker-management, vercel-deploy-premium, hostinger-vps
- inference-sh-cli, omniroute, skills-infrastructure-manager

### Dados & Automação (5)
- workflow-automation (Make.com, n8n), watchers
- chroma, faiss, qdrant-vector-search

### IA & ML (5)
- google-gemini-ai, openai-image-generation, huggingface-hub
- outlines, instructor

### Conteúdo & SEO (5)
- copywriting, site-audit, ecommerce-content-marketing
- local-business-seo, seo-tools

### Jogos & Gamificação (3)
- sovereign-game-os (custom), architecture-diagram, concept-diagrams

### Produtividade (6)
- notion, google-workspace, obsidian, siyuan
- memento-flashcards, here.now

## Deploy Imediato

```bash
# Authority Card (thiagopiola.com.br)
cp /opt/data/projects/authority-card/index.html /var/www/thiagopiola/public/
cd /opt/data/projects/thiagopiola && git add -A && git commit -m "feat: authority card" && git push

# Design System RDV
cd /opt/data/projects/reidasvendas && pnpm run build
cd packages/design-system && npm run build

# Thiago Lab (thiagolab.com)
cd /opt/data/projects/thiago-lab && docker compose up -d --build
```

## Próximos Passos

1. 🚀 Deploy Authority Card no Vercel (git push)
2. 🎨 Integrar tokens do Design System no site RDV
3. 🔗 Conectar Notion como CMS dos sites
4. 📊 Dashboard unificado de analytics
5. 🤖 Pipeline de IA: Hermes → n8n → Supabase → Sites
