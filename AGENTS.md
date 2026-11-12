# Story Bible — Schema Operacional (OKF v0.1)

Este repositório combina o padrão **LLM Wiki** (Andrej Karpathy) com a especificação
**Open Knowledge Format (OKF) v0.1** (Google Cloud Platform):

- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md

---

## Ideia Central

A Story Bible é o **segundo cérebro** do universo "Evangelho às Estrelas".
Ela acumula conhecimento de forma persistente: novas fontes (capítulos finalizados,
brainstormings, referências externas) atualizam páginas, conexões e sínteses já
existentes. O agente mantém a wiki: resume, organiza, cria relações e cuida da
consistência.

**Repositório-fonte de capítulos:** `neogedom/livro`

---

## Arquitetura

```
storybible/
├── personagens/               # Fichas OKF (type: Character)
├── capitulos/                 # Resumos de capítulos (type: Chapter)
├── visuais/                   # Timelines visuais (type: VisualState)
├── lugares/                   # Locais do universo (type: Location)
├── conceitos/                 # Conceitos transversais (type: Concept)
├── temas/                     # Sínteses temáticas (type: Theme)
├── insights/                  # Ideias de brainstorming
├── decisoes/                  # Decisões formais
├── ideias-rejeitadas/         # Anti-memória
├── index.md                   # Índice raiz (okf_version: "0.1")
├── log.md                     # Log de operações
├── AGENTS.md                  # Este schema operacional
├── protocolo-ingest.md        # Passo a passo do INGEST
└── .github/copilot-instructions.md
```

---

## Documentos de Conceito OKF

Todo arquivo `.md` dentro das pastas de conteúdo (exceto `index.md` e `log.md`)
representa exatamente um conceito. O caminho sem a extensão `.md` é o identificador
estável.

Cada documento começa com frontmatter YAML:

```markdown
---
type: Character # Tipo OKF (ver taxonomia abaixo)
title: Mário
description: Protagonista, Souhma trazido à força para Ornick.
tags: [protagonista, souhma, humano]
resource: https://github.com/neogedom/storybible/blob/main/personagens/mario.md
timestamp: 2026-07-24T12:00:00-03:00
---
```

### Taxonomia de tipos

| Tipo           | Uso                           | Onde                 |
| -------------- | ----------------------------- | -------------------- |
| `Character`    | Ficha de personagem           | `personagens/`       |
| `Chapter`      | Resumo de capítulo            | `capitulos/`         |
| `VisualState`  | Timeline visual de personagem | `visuais/`           |
| `Location`     | Lugar no universo             | `lugares/`           |
| `Concept`      | Conceito transversal          | `conceitos/`         |
| `Theme`        | Síntese temática              | `temas/`             |
| `Entity`       | Raça, criatura, objeto        | `conceitos/`         |
| `Decision`     | Decisão formal tomada         | `decisoes/`          |
| `Insight`      | Ideia de brainstorming        | `insights/`          |
| `RejectedIdea` | Ideia rejeitada com motivo    | `ideias-rejeitadas/` |

### Regras do frontmatter

- `type` é **obrigatório** — string curta, não vazia
- `title`, `description`, `tags`, `timestamp` são recomendados
- `description` deve ser uma frase útil para índices e busca
- `resource` identifica o recurso canônico (URL do GitHub)
- `tags` lista YAML de strings curtas
- `timestamp` ISO 8601 da última alteração significativa

---

## Operações

### INGEST (Mini-INGEST e INGEST completo)

Disparado pela skill **`/finalizar-capitulo X`** (Mini-INGEST, modo privado) ou **`/ingest-completo X`** (INGEST completo, congelamento).

O protocolo detalhado está em `protocolo-ingest.md`. Resumo:

> **Dois modos (ver `protocolo-ingest.md`):**
> - **Mini-INGEST (modo privado)** — gatilho "cap. X pronto" ou `/finalizar-capitulo X`; roda a cada
>   capítulo fechado durante a escrita privada do L1; só fatos duros.
> - **INGEST completo (congelamento)** — skill `/ingest-completo X`;
>   enriquece os Mini-INGESTs; inclui LINT e análise de arco.

1. Ler capítulo de `neogedom/livro/Livro 1/capituloX.md`
2. Extrair fatos: eventos, personagens, decisões, falas, sementes
3. Extrair visuais: roupas, ferimentos, expressões
4. Atualizar `capitulos/capitulo-XX.md` (type: Chapter)
5. Atualizar `personagens/<nome>.md` com novos fatos de arco
6. Atualizar `visuais/<nome>.md` com estado visual do capítulo
7. Atualizar `conceitos/` afetados
8. Executar **LINT automático** — cruzar novo capítulo com histórico
9. Reportar contradições ao usuário
10. Atualizar `index.md` e `log.md`

### INGEST — Insights automáticos

Durante qualquer conversa no chat, o agente DEVE detectar automaticamente:

- **Decisões confirmadas** pelo usuário → salvar em `decisoes/`
- **Ideias aprovadas** → salvar em `insights/` + atualizar conceitos afetados
- **Ideias rejeitadas com motivo** → salvar em `ideias-rejeitadas/`
- **Conexões entre conceitos** → atualizar páginas existentes

**Regras:**

- Só salvar se o conteúdo for NOVO (não duplicar o que já existe)
- Não salvar perguntas exploratórias sem resolução
- Ao final da resposta, reportar resumo discreto: `📥 storybible: 1 insight, 1 decisão`
- Salvamento faz parte da resposta — não requer confirmação do usuário

### QUERY — Consultar a storybible

Disparado pela skill **`/query-storybible [pergunta]`**.

1. Ler `index.md` para localizar páginas relevantes
2. Navegar por subíndices e links entre conceitos
3. Ler documentos relevantes
4. Sintetizar resposta com citações (links para os documentos)
5. Quando a resposta tiver valor durável, incorporar à wiki como conceito

### LINT — Verificar saúde da wiki

Disparado pela skill **`/lint-storybible`** (ou automaticamente pós-INGEST).

Verificar:

**Estrutura OKF:**

- [ ] Todo documento tem frontmatter YAML parseável?
- [ ] Todo frontmatter tem `type` não vazio?
- [ ] `index.md` tem `okf_version`? `log.md` segue formato reservado?
- [ ] Timestamps ISO 8601 e consistentes?

**Links e navegação:**

- [ ] Links internos funcionam?
- [ ] Páginas órfãs (sem links de entrada)?
- [ ] Conceitos mencionados mas sem página própria?

**Coerência narrativa:**

- [ ] Algum fato em capítulo recente contradiz capítulo anterior?
- [ ] Decisões de personagens consistentes com seu arco?
- [ ] Linha do tempo coerente (datas, durações)?
- [ ] Sementes plantadas colhidas ou ainda pendentes?

**Coerência visual:**

- [ ] Personagem com roupa diferente sem registro de transição?
- [ ] Cicatriz some entre capítulos sem explicação?
- [ ] Estado visual consistente com a narrativa?

**Lacunas:**

- [ ] Personagens secundários sem ficha?
- [ ] Lugares mencionados mas não documentados?
- [ ] Conceitos teológicos mencionados mas não definidos?

---

## Prompts do Usuário

| Comando (repo `livro`, Claude)      | O agente faz                                                                                                             |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `/revisar-capitulo X`               | Ciclo de revisão, em ordem: subagentes `arquiteto-densidade` → `guardiao-coerencia` → `revisor-linguistico` |
| `/finalizar-capitulo X`             | Mini-INGEST do capítulo fechado (modo privado): ficha, visuais, canon duro, esquema e log. Para o INGEST completo, use `/ingest-completo X` |
| `/lint-storybible`                  | LINT completo: estrutura, links, coerência narrativa, coerência visual, lacunas |
| `/query-storybible [pergunta]`      | Navega índice, lê docs, responde com citações |
| `/ingest-completo X`               | INGEST completo (congelamento): fatos, personagens, visuais, conceitos, sementes e LINT |
| Publicação e áudio                  | Arquivados em `docs/arquivo/skills/` (repo `livro`), por pausa da publicação. Ver `docs/handoff/estado-estrategico.md` |

---

## Gatilhos de LINT

| Momento                                              | Escopo                                                                     | Automático? |
| ---------------------------------------------------- | -------------------------------------------------------------------------- | ----------- |
| Pós-INGEST (após `/ingest-completo X`)             | Parcial: contradições do capítulo novo vs. histórico + consistência visual | ✅          |
| Sob demanda (`/lint-storybible`)                    | Completo                                                                   | Manual      |
| Pré-publicação (pausada; skill arquivada) | Visual: estado dos personagens                                             | ✅          |
| Pré-escrita (antes de iniciar capítulo novo)         | Fronteira: estado atual                                                    | Manual      |
| Periódico (a cada ~5 capítulos)                      | Completo                                                                   | Manual      |

---

## Conformidade OKF v0.1

O bundle está conforme OKF v0.1 quando:

1. Cada `.md` não reservado (exceto `index.md`, `log.md`) tem frontmatter YAML
   parseável com `type` não vazio
2. `index.md` segue estrutura reservada com `okf_version: "0.1"`
3. `log.md` segue estrutura reservada com data ISO 8601

Campos opcionais ausentes, tipos desconhecidos, links quebrados e índices
ausentes em subdiretórios **não invalidam** o bundle.

---

## Regras de Ouro (migradas de `.github/copilot-instructions.md`, 2026-11-12)

- Personagens (type: Character) SEMPRE têm frontmatter YAML válido
- Visuais (type: VisualState) SEMPRE registram "não aparece" quando o personagem não está no capítulo
- NUNCA contradizer um fato registrado sem reportar ao usuário primeiro
- Milagre tem custo — registrar qual foi o custo em cada ocorrência
- Quando 2 dos 3 (Mário/Nolan/Kate) concordam, o mundo piora — verificar se isso se mantém
- Links entre conceitos DEVEM ter contexto explicativo (o link sozinho não tipa a relação)
- Salvamento de insights é automático — não perguntar se pode salvar

## Guardrails

- **Teologia**: Milagre resolve o problema | Deus confirma plano do personagem | Fé funciona como superpoder → **todos são erro**
- **Voz**: Prosa fluida demais (tom YA/autoajuda) | Decisão crucial sem reflexão interior | Diálogo genérico → **todos são erro**
- **Ambiguidade é intencional; confusão é erro**
- **Sofrer é parte da prosa** — se o personagem não paga, o leitor desconfia
