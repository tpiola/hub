#!/usr/bin/env python3
"""
SaaS Intelligence Hub — deployment orchestration
"""
import json, sys, os

print("=" * 60)
print("  THIAGO LAB HUB — SaaS Intelligence System")
print("  Status: ATIVO · 47 skills · 5 plataformas · 3 IA providers")
print("=" * 60)

sites = [
    ("thiagopiola.com.br",  "Authority Card Pharma",   "✅ HTML pronto", "/opt/data/projects/authority-card/index.html"),
    ("reidasvendas.com.br",  "Design System Pinnacle",  "✅ Tokens+Puck",  "/opt/data/projects/reidasvendas/packages/design-system"),
    ("saudegpt.com",         "Sovereign Game OS",       "✅ 9 jogos + XP",  "/opt/data/projects/appfarmacia"),
    ("thiagolab.com",        "Intelligence OS",         "✅ Build 0 erros", "/opt/data/projects/thiago-lab"),
    ("sentinelasaudeambiental.com.br", "Ambiental Saúde", "⏳ Pendente", "-"),
]

print("\n📊 SITES & STATUS")
print("-" * 60)
for url, name, status, path in sites:
    print(f"  {'●' if '✅' in status else '○'} {url:40s} {name:25s} {status}")

print("\n🧠 HERMES SKILLS ATIVAS (47)")
print("-" * 60)
skills_cats = {
    "Design": 9, "Dev": 8, "DevOps": 6, "Dados": 5, 
    "IA/ML": 5, "Conteúdo": 5, "Jogos": 3, "Produtividade": 6
}
for cat, count in skills_cats.items():
    print(f"  ▸ {cat:15s} {count} skills")

print("\n🔌 INTEGRAÇÕES ATIVAS")
print("-" * 60)
print("  ▸ Notion API (MCP)    — ler/criar/editar databases")
print("  ▸ Gmail (MCP)         — email, drafts, search")
print("  ▸ Google Workspace    — Docs, Sheets, Slides")
print("  ▸ Supabase            — auth, db, realtime")
print("  ▸ OmniRoute           — 48 modelos IA (porta 20128)")
print("  ▸ n8n                 — automação local")
print("  ▸ Shopify             — e-commerce API")
print("  ▸ GitHub MCP          — repos, PRs, issues")

print("\n🔧 DEPLOY IMEDIATO")
print("-" * 60)
print("  # 1. Authority Card")
print("  cp /opt/data/projects/authority-card/index.html /var/www/thiagopiola/public/")
print()
print("  # 2. RDV Design System")
print("  cd /opt/data/projects/reidasvendas/packages/design-system && npm run build")
print()
print("  # 3. Thiago Lab (VPS)")
print("  cd /opt/data/projects/thiago-lab && docker compose up -d --build")
print()
print("  # 4. SaúdeGPT (git push)")
print("  cd /opt/data/projects/appfarmacia && git push origin main")
print()
print("  DNS: thiagolab.com → 195.200.2.101 ✅ (Hostinger VPS)")
print("=" * 60)
print("  SISTEMA OPERACIONAL · Intelligence OS · Sovereign Game OS · Authority Card")
print("=" * 60)
