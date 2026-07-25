# Story Bible — Evangelho às Estrelas

A **Story Bible** é o segundo cérebro do universo "Evangelho às Estrelas" — um
bundle OKF v0.1 (LLM Wiki) que organiza o conhecimento da obra em conceitos
interligados com frontmatter YAML, índice hierárquico e operações
INGEST/QUERY/LINT para agentes de IA.

## Propósito

- **Fonte de verdade canônica** do universo (personagens, lugares, conceitos, lore)
- **Segundo cérebro** que acumula conhecimento entre conversas e sessões
- **Referência para agentes** (Copilot, futuramente Claude, Cursor) via
  `.github/copilot-instructions.md` e `AGENTS.md`
- **Vault Obsidian** acessível de qualquer lugar via GitHub (web, mobile, Codespaces)

## Repositórios Relacionados

- [neogedom/livro](https://github.com/neogedom/livro) — Capítulos escritos e audiobooks (fonte para INGEST)

## Como Usar

### Como Vault Obsidian

1. Clone este repositório
2. Abra o Obsidian → "Open folder as vault" → selecione a pasta clonada
3. Plugins recomendados: Obsidian Git (auto-sync), Graph View, Backlinks

### Prompts para o Copilot

| Prompt | Ação |
|---|---|
| "Iniciar revisão do capítulo X" | Ciclo qualidade (densidade → coerência → linguística) + audiochapter |
| "Finalizar capítulo X" | INGEST na storybible + LINT automático |
| "Lintar storybible" | Varredura completa de coerência |
| "Query: [pergunta]" | Consulta com citações |
| "Preparar capítulo X para Substack" | LINT visual + prompt de imagem + show notes |

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
