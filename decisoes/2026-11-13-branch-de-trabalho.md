---
type: Decision
title: Branch de trabalho única para o trabalho com o Claude (teste de um mês)
description: Decisão do autor (2026-11-13). A branch trabalho centraliza o trabalho com o Claude nos repositórios livro e storybible por cerca de um mês. Se der certo, ela vira a main; se não, a main segue como está.
tags: [decisao, processo, git, branches]
timestamp: 2026-11-13T12:00:00-03:00
---

# Branch de trabalho única (teste de um mês)

Status: decidido pelo autor em 2026-11-13. Motivo: cada sessão do Claude cria a própria branch (`ccr-...`), e isso vira bagunça de branches.

## Decisão

- O trabalho com o Claude fica na branch **`trabalho`**, nos dois repositórios (`neogedom/livro` e `neogedom/storybible`).
- A `main` não é tocada durante o teste. Ela está intacta e é um ancestral direto da `trabalho` (nada a mesclar à mão).
- O teste dura cerca de um mês, até 2026-12-13. Se der certo, a `trabalho` assume a `main`.
- Ponto de partida: o checkpoint de 2026-11-13, com tudo o que foi feito nas sessões desta data.

## Regras

1. Sessão começa na `trabalho`, commita nela e dá push nela (push autorizado pelo autor).
2. Se o ambiente criar uma branch própria da sessão, o trabalho é integrado na `trabalho` ao final, de preferência por fast-forward.
3. Sem outras branches, sem PRs e sem apagar branches, a menos que o autor peça.
4. Fim do teste: se der certo, `git push origin trabalho:main` (fast-forward, desde que a `main` não tenha andado). Se não der, a `main` segue como está e a `trabalho` fica como registro.

## Passo do autor (GitHub)

Mudar a default branch de cada repositório para `trabalho`: Settings, General, Default branch. Sem isso, uma sessão nova clona a `main` e não lê as regras que estão na `trabalho`. Quando o teste terminar, voltar a default para `main` (ou, se a `trabalho` assumir a `main`, nada a fazer).

## Estado das branches em 2026-11-13

**`livro`** (a `main` está 37 commits atrás do checkpoint; ela não andou):

| Branch | Situação |
| --- | --- |
| `ccr-8f7f45c3-8prynp`, `ccr-a010bd86-ntyqcg`, `claude/port-github-agents-n5ufc8` | Nenhum commit fora do checkpoint (já incluídos). Podem ser apagadas, se o autor quiser. |
| `ccr-9341f1f3-ex07nl` | Branch da sessão de hoje, igual ao checkpoint. |
| `feat/app` | 2 commits de 2026-11-08 (PWA de autoria com sync GitHub; integração da Story Bible), ainda fora da linha. Decidir. |
| `copilot/avalie-meus-comentarios-capitulo-37`, `copilot/realizar-analises-checkpoint`, `kilo/friendly-node-63a`, `migrate/prompts-to-skills` | De 8 a 13/10, com 300 a 324 commits cada e **sem ancestral comum com a main** (histórico paralelo antigo). Não foram tocadas. |

**`storybible`** (a `main` está 74 commits atrás do checkpoint; ela não andou):

| Branch | Situação |
| --- | --- |
| `ccr-8f7f45c3-8prynp`, `ccr-a010bd86-ntyqcg`, `claude/port-github-agents-n5ufc8` | Nenhum commit fora do checkpoint (já incluídos). Podem ser apagadas, se o autor quiser. |
| `ccr-9341f1f3-ex07nl` | Branch da sessão de hoje, igual ao checkpoint. |
| `ccr-4b4c9a7b-o467yd` | 1 commit de 2026-11-13: resposta do teste 3 de atribuição de falas (`decisoes/teste-processo/falas-teste-3-resposta.md`). Fora da linha. |
| `ccr-7c2a2b28-4xxnl2` | 1 commit de 2026-11-13: rodada 2 do teste 2 do processo (`decisoes/teste-processo-2026-11-13.md`). Fora da linha. |
| `copilot/resumo-capitulos-ato-3` | De 2026-10-11, 116 commits, **sem ancestral comum com a main**. Não foi tocada. |
