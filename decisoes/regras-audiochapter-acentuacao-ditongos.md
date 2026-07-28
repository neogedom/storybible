---
type: Decision
title: Regras de Acentuação Fonética e Extração de Narração para Minimax
description: Decisão de implementar regras sistemáticas de acentuação de tritongos/ditongos decrescentes e extração rigorosa de narração (sem falas) no script de áudio Minimax.
tags: [decisao, audio, minimax, fonetica, narracao]
timestamp: 2026-07-27T15:30:00-03:00
---

# Decisão: Regras de Acentuação Fonética e Extração de Narração para Minimax

## Contexto

O script de narração para o Minimax TTS estava vazando falas de personagens no
arquivo de narração. Além disso, palavras com tritongos e ditongos decrescentes
não tinham acento gráfico, fazendo a TTS ler com entonação incorreta em alguns
casos.

## Decisão

1. **Extração de narração**: adotar regras precisas de identificação de falas vs.
   narração, com tabela de casos concretos e estratégia passo a passo. Verbos de
   elocução são preservados; todo conteúdo entre travessões que seja fala direta
   é removido. Pensamentos diretos (aspas) também são removidos.

2. **Acentuação fonética**: adicionar acento agudo na vogal forte (a, e, o) de
   todo tritongo ou ditongo decrescente oral na sílaba tônica que ainda não
   possua acento gráfico. Ex: "mais" → "máis", "noite" → "nóite", "meu" → "méu".

3. **Hífens em pronomes**: remover hífens de ênclise/próclise/mesóclise, exceto
   quando o pronome for "se" (mantém hífen).

## Arquivos alterados

- `Livro/.github/skills/preparar-audiochapter/SKILL.md` — reescrita completa com
  regras detalhadas de extração, acentuação e formatação.
- `storybible/conceitos/fonetica.md` — adicionada seção "Acentuação Fonética de
  Tritongos e Ditongos Decrescentes" com tabela de substituição e regras de ouro.
- `Livro/.github/prompts/audiochapter.prompt.md` — atualizado para referenciar a
  skill e as regras fonéticas completas.
- `Livro/.github/agents/preparador-audio.agent.md` — agente especializado criado
  para executar o workflow de áudio com checklist de qualidade.

## Riscos mapeados

- Acentuação excessiva pode tornar o texto difícil de revisar visualmente —
  mitigado pela regra de só acentuar na sílaba tônica e não alterar palavras já
  acentuadas.
- Confusão entre ditongo e hiato pode gerar acentos falsos — mitigado pela regra
  "em caso de dúvida, preservar original".
