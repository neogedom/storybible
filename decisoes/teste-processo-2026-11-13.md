---
type: Decision
title: Teste 1 do processo — Mini-INGEST do cap. 46
description: Resultado da execução real de /finalizar-capitulo 46 e de /query-storybible, com o que passou, o que falhou e o que ajustar.
tags: [teste, processo, mini-ingest]
timestamp: 2026-11-13T12:00:00-03:00
---

# Teste 1 — execução de ponta a ponta (2026-11-13)

Plano: `decisoes/plano-teste-processo.md`. Entrada: cap. 46. Passos: `/finalizar-capitulo 46` (executado à mão, seguindo a skill) e consulta à storybible sobre um fato do capítulo. Sessão nova, branch `ccr-8f7f45c3-8prynp` (o plano cita outra branch).

## Critérios

| Critério | Resultado |
|---|---|
| Ficha em `capitulos/capitulo-46.md`, livro intacto | Passou. O repo `Livro` ficou sem alterações. |
| Fatos da ficha conferem com o texto | Conferido pelo agente. **Pendente: conferência manual do autor.** |
| Linha do esquema e entrada do log | Passou. |
| Nada de capítulos futuros | Passou. |

Também feitos: visuais de seis personagens e "não aparece" de três; `lugares/metropole.md`; payoff de Lupe'i em `temas/sementes.md`; bloco de fronteira no esquema. A consulta ("quando há quebra de vigilância na Metrópole?") foi respondida com citação e confiança ✅.

## O que falhou ou ficou frouxo

1. **Contagem de palavras sem método fixo.** `wc -w` deu 2.123 e a tabela usa 2.186 (tokens separados por espaço). **Ajustado:** método fixado na skill `finalizar-capitulo`.
2. **`index.md` sem os capítulos recentes.** A consulta não chega ao cap. 46 pelo índice; só achou o fato por `lugares/metropole.md`. **A ajustar:** listar os capítulos no índice (ou definir que a consulta navega também por `capitulos/`).
3. **Totais divergentes no esquema.** As notas dão 114.483 e 114.321 para o acumulado até o cap. 45. Usado 114.321 (nota mais recente). **A ajustar:** consolidar no próximo recálculo.
4. **Plano cita branch antiga.** Atualizar o plano para a branch vigente da sessão.
5. **Gatilho de checkpoint atingido** (último em 2026-09-18, 18 capítulos atrás). Só oferecido, não executado.

## Achados de texto no cap. 46 (livro não alterado)

- "Nolan interrompeu o traço de carvão:" sem fala, seguido de outra linha de Nolan.
- Kate diz "O prazo dele está certo", sem prazo antes na cena.
- Risco estrutural: Kate e Nolan concordam no plano sem Mário em cena; Nolan não erra em nada no capítulo.

## Veredito

Processo funciona de ponta a ponta. Itens 2 a 4 são ajustes pequenos; o item 1 já foi corrigido.
