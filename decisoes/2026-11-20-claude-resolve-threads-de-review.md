---
type: Decision
title: O Claude resolve as threads de review tratadas (2026-11-20)
description: Decisão do autor (2026-11-20). Depois de aplicar um lote de comentários de review, o Claude resolve as threads tratadas no GitHub e deixa abertas só as que dependem do autor, para que o autor veja se pode mesclar sem reler tudo. Substitui "quem resolve é o autor" (2026-11-16).
tags: [decisao, processo, pr, review]
timestamp: 2026-11-20T21:45:00-03:00
---

# O Claude resolve as threads de review tratadas (2026-11-20)

Status: decidido pelo autor em 2026-11-20. Muda o item 4 de "Comentários de Review no PR" em `docs/guardrails.md` do Livro, que dizia que o Claude só resolvia threads quando o autor pedisse ("quem resolve é o autor").

## Motivo

O autor quer saber de relance se pode mesclar o PR, sem reler todos os comentários. Com as threads resolvidas à medida que são tratadas, "aberta" passa a significar que falta tratamento ou decisão.

## Decisão

1. Depois de aplicar o lote, o Claude resolve no GitHub as threads que tratou (aplicadas ou respondidas).
2. Fica aberta só a thread que depende de decisão do autor. Comentário novo fica aberto até o lote seguinte.
3. Se o texto aplicado difere da sugestão (grafia, pontuação ou palavra), a diferença vai no relatório do lote antes de resolver.
4. O Claude não responde nas threads (as respostas vão no relatório do chat e na decisão da storybible), salvo pedido do autor. O autor pode reabrir qualquer thread.
5. O relatório de cada rodada diz quantas threads seguem abertas. PR sem conflito com a `main` e sem thread aberta está pronto para o autor mesclar. Quem mescla é o autor.

## Aplicação em 2026-11-20 (PR #20 do Livro)

- Das 46 threads do lote, 2 (cap. 49, L7 e L13, perguntas sem mudança de texto) já estavam resolvidas pelo autor. O Claude resolveu as 44 restantes depois de conferir o cap. 49 linha a linha contra as sugestões.
- A conferência achou uma sugestão não aplicada (L57: "qual a deus" ficou "qual deus") e sete ajustes do Claude em relação ao texto sugerido: pontuação em L19 e L41, "bênçãos" no L55, o L67 sem o trecho duplicado, "Apoiou a mão sobre o pacote" no L85 (o original e a sugestão diziam "Estendeu o pacote", e o L89 pede o pacote no colo), "cadência monocórdia" no L97 (a sugestão tinha "monotônica") e "fedia a vembra" no L129 (a sugestão tinha "à vembra", com quatro pontos). O autor decidiu manter o texto como está.

## Ligações

- Decisão do lote: [Cap. 49, comentários do autor em lote](/decisoes/2026-11-20-cap49-comentarios-em-lote.md).
- Fluxo geral: [Fluxo de trabalho: PR por sessão](/decisoes/2026-11-14-fluxo-pr-por-sessao.md).
