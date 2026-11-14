---
type: Decision
title: Fluxo de trabalho: PR por sessão para a main, com backup (2026-11-14)
description: Decisão do autor (2026-11-14). A main volta a ser a fonte. Cada sessão do Claude trabalha na própria branch e abre um PR para a main quando o autor pede. backup/main-2026-11-14 guarda a main anterior. A pasta .github (e .kilo, no Livro) fica como está na main. Supera a branch trabalho.
tags: [decisao, processo, git, branches]
timestamp: 2026-11-14T12:00:00-03:00
---

# Fluxo de trabalho: PR por sessão para a main (2026-11-14)

Status: decidido pelo autor em 2026-11-14. Supera `decisoes/2026-11-13-branch-de-trabalho.md`.

## Motivo

Uma branch paralela de longa duração (`trabalho`) exigiria conciliação no fim do mês. Com um PR por sessão para a `main`, nada acumula fora dela.

## Decisão

1. A `main` é a fonte. Cada sessão trabalha na própria branch `ccr-...` e, quando o autor pede, abre um PR para a `main`, mesclado com merge commit. Depois do merge, a branch da sessão é apagada.
2. Backup: `backup/main-2026-11-14` (Livro em `7072600`, storybible em `47a153c`) é a `main` antes deste fluxo. Para voltar atrás, a `main` é reposta a partir dela, com o autor.
3. `.github/` (nos dois repositórios), `.kilo/` e `kilo.json` (no Livro) ficam como estão na `main`. Mudanças nessas pastas não entram nos PRs. Os agentes e as skills do Claude estão em `.claude/`.
4. Documentos que se movem para `docs/` (handoff e marketing) têm cópia viva em `docs/`, e um retrato congelado em `.github/`. Vale a cópia de `docs/`.
5. A branch `trabalho` fica como registro. Só é apagada com pedido do autor.

## Pendências

- As branches de teste do processo `ccr-4b4c9a7b-o467yd` e `ccr-7c2a2b28-4xxnl2` ficam fora deste PR. O autor decide se entram.
- Branches antigas: no Livro, `copilot/avalie-meus-comentarios-capitulo-37`, `copilot/realizar-analises-checkpoint`, `kilo/friendly-node-63a`, `migrate/prompts-to-skills` e `feat/app`; no storybible, `copilot/resumo-capitulos-ato-3`. Sem ancestral comum com a `main`. Decidir uma a uma.
