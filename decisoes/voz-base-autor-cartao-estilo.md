---
type: Decision
title: Voz-base do autor como seção de calibração no tom-e-voz
description: Decisão de registrar a voz natural do autor (extraída de 4 textos humanos de gêneros diferentes) como seção fixa em temas/tom-e-voz.md, servindo de régua para a escrita e para o passe anti-slop.
tags: [decisao, estilo, voz, anti-slop, calibracao]
timestamp: 2026-09-13T12:00:00-03:00
---

# Decisão: Voz-base do autor como seção de calibração no tom-e-voz

## Contexto

O passe anti-slop testado no cap. 28 (texto 100% IA) levantou o risco de o
passe "alisar" a voz do autor junto com o slop. O autor forneceu quatro textos
100% humanos, de gêneros diferentes (terror histórico, conto-fábula, narrativa
bíblica, crônica satírica), como referência de estilo. A análise cross-gênero
extraiu 7 marcas de núcleo; o autor decidiu onde guardar o cartão: seção dentro
de `temas/tom-e-voz.md` (não arquivo novo).

## Decisão

1. **Local**: o cartão de voz vive como seção "Voz-base do autor — calibração
   de estilo" em `temas/tom-e-voz.md` (fonte única). Agentes que já leem esse
   arquivo herdam a calibração.
2. **Filtro de entrada**: só entra no cartão o que aparece em mais de um
   gênero; manha de gênero não conta como voz.
3. **Régua do anti-slop**: repetição de frase com função, batida curta,
   personificação irônica concreta e trio de substantivos ritmado NÃO se
   cortam; eco de palavra funcional, abstração solta e trio de adjetivos
   continuam caindo.
4. **Léxico subido**: tempero por POV (Mário nunca; Kate concreta; registro
   régio onde couber). Confirmada pelo autor em 2026-09-13.
5. **Material-fonte**: os 4 textos originais ficam arquivados brutos em
   `raw/voz-autor/` (verbatim, com os erros de digitação originais). O cartão
   cita trechos; o bruto fica como amostra de consulta para calibrar a
   escrita.

## Arquivos alterados

- `temas/tom-e-voz.md` — nova seção "Voz-base do autor — calibração de estilo
  (2026-09-13)", com 7 marcas, regras de tradução e régua do anti-slop;
  frontmatter atualizado (description, tags, timestamp).
- `raw/voz-autor/` — criada; 4 textos-fonte salvos verbatim
  (`01-novela-terror-alemanha-nazista.md`, `02-haroldo.md`,
  `03-lamentacoes-de-abaddon.md`, `04-ativismo.md`).
- `Livro/.github/agents/editor-anti-slop.agent.md` — ponteira: as marcas da
  voz-base do autor não se cortam (referência à seção no tom-e-voz).
- `Livro/.github/agents/livro-writer.agent.md` — ponteira: seção "Voz-base do
  autor" como régua da prosa na escrita. *(Edições em arquivos de agente só
  valem após Reload Window.)*

## Riscos mapeados

- Uma amostra só mostraria a superfície do autor — mitigado pelo filtro
  cross-gênero (4 gêneros).
- O cartão pode virar desculpa para manter slop disfarçado de "voz" — mitigado
  pela régua explícita (o que continua caindo) e pelo teste rápido ("o corte
  deixou mais liso/genérico?").
- Léxico alto pode virar prosa roxa — mitigado pela regra do tempero por POV.
