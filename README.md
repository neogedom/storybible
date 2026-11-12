# Story Bible — Evangelho às Estrelas

A **Story Bible** é o segundo cérebro do universo "Evangelho às Estrelas" — um
bundle OKF v0.1 (LLM Wiki) que organiza o conhecimento da obra em conceitos
interligados com frontmatter YAML, índice hierárquico e operações
INGEST/QUERY/LINT para agentes de IA.

## Propósito

- **Fonte de verdade canônica** do universo (personagens, lugares, conceitos, lore)
- **Segundo cérebro** que acumula conhecimento entre conversas e sessões
- **Referência para agentes** via `AGENTS.md` (esquema) e as skills do Claude no repo `livro`
- **Vault Obsidian** acessível de qualquer lugar via GitHub (web, mobile, Codespaces)

## Repositórios Relacionados

- [neogedom/livro](https://github.com/neogedom/livro) — Capítulos escritos e audiobooks (fonte para INGEST)

## Como Usar

### Como Vault Obsidian

1. Clone este repositório
2. Abra o Obsidian → "Open folder as vault" → selecione a pasta clonada
3. Plugins recomendados: Obsidian Git (auto-sync), Graph View, Backlinks

### Comandos para o Claude

| Comando (no repo `livro`, Claude) | Ação |
| --------------------------------- | ---- |
| `/revisar-capitulo X` | Ciclo de revisão (densidade → coerência → linguística) |
| `/finalizar-capitulo X` | Mini-INGEST do capítulo fechado (modo privado) |
| `/ingest-completo X` | INGEST completo, no congelamento |
| `/lint-storybible` | Varredura completa de coerência |
| `/query-storybible [pergunta]` | Consulta com citações |
| `/passe-anti-slop X`, `/passe-fechos X` | Passes de checkpoint (sob demanda) |

Publicação (`/publicar-substack`) e áudio (`/audiochapter`) estão arquivados em `docs/arquivo/skills/` no repo `livro`, por decisão de 2026-11-12.

## Estrutura

```
storybible/
├── personagens/           # Fichas OKF dos personagens
├── capitulos/             # Resumos OKF dos capítulos
├── visuais/               # Timelines visuais por capítulo
├── lugares/               # Locais do universo
├── conceitos/             # Conceitos transversais (fé, milagre, STC, etc.)
├── temas/                 # Sínteses temáticas (arco STC, teologia)
├── insights/              # Ideias de brainstorming registradas automaticamente
├── decisoes/              # Decisões formais de desenvolvimento
├── ideias-rejeitadas/     # Anti-memória (ideias descartadas)
├── AGENTS.md              # Schema operacional do agente
├── protocolo-ingest.md    # Protocolo de INGEST detalhado
└── index.md               # Índice raiz do bundle OKF
```

## Licença

CC-BY-NC — Uso não-comercial.
