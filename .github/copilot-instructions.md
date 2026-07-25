# Story Bible — Instruções do Agente

> A Story Bible é o segundo cérebro do universo "Evangelho às Estrelas" — um
> bundle OKF v0.1 (LLM Wiki) que acumula conhecimento de forma persistente:
> personagens, capítulos, visuais, conceitos, temas, decisões e insights.
>
> **Repositório-fonte de capítulos:** `neogedom/livro`

## Schema Operacional

Consulte `AGENTS.md` para definições completas de tipos OKF e operações.

## Protocolo de INGEST

Consulte `protocolo-ingest.md` para o passo a passo detalhado de:
- Finalização de capítulo (INGEST manual)
- Insights automáticos (detecção implícita)
- Referências externas

## Prompts Disponíveis

| Prompt | Ação |
|---|---|
| "Iniciar revisão do capítulo X" | Ciclo qualidade (densidade → coerência → linguística) + audiochapter no repo `livro` |
| "Finalizar capítulo X" | INGEST na storybible + LINT automático |
| "Lintar storybible" | Varredura completa de coerência |
| "Query: [pergunta]" | Consulta com citações |
| "Preparar capítulo X para Substack" | LINT visual + prompt de imagem + show notes |

## Regras de Ouro

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
