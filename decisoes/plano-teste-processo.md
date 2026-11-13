---
type: Decision
title: Plano de teste do processo de escrita
description: Quatro testes para validar o fluxo de finalização, a detecção de erros, a atribuição de falas e a consistência entre storybible e livro.
tags: [processo, teste, plano]
timestamp: 2026-11-13T12:00:00-03:00
---

# Plano de teste do processo de escrita

Status (atualizado em 2026-11-13): teste 4 executado em 2026-11-12, com registro em `decisoes/teste-processo-2026-11-12.md`. Testes 1, 2 e 3 pendentes. Materiais dos testes 2 e 3 prontos em `decisoes/teste-processo/`. As chaves de respostas ficam com o autor, fora do repositório.

**Como retomar em outra sessão:** abra um contexto novo e peça "leia `storybible/decisoes/plano-teste-processo.md` e execute o teste N". Branch de trabalho: `ccr-a010bd86-ntyqcg`, nos repositórios `Livro` e `storybible`.

## Por que testar

Muita coisa foi construída e corrigida, mas o fluxo completo nunca foi executado de ponta a ponta. Em especial, a skill `finalizar-capitulo` nunca rodou. O teste deve rodar em sessão nova, sem o contexto desta conversa, para refletir o uso real.

## Teste 1: execução real de ponta a ponta

- **Entrada:** capítulo 46, depois que o autor aprovar a revisão. Pré-condição pendente: em 2026-11-13 o capítulo não tem notas `(*)` do autor, mas a revisão continua em curso segundo o estado estratégico.
- **Passos:** `/finalizar-capitulo 46` (Mini-INGEST); depois `/query-storybible` sobre um fato do capítulo.
- **Critérios de aprovação:**
  - A ficha `capitulos/capitulo-46.md` é criada no caminho certo e o texto do livro não é alterado.
  - Cada fato da ficha (personagens, eventos, sementes) confere com o texto. O autor confere manualmente.
  - A linha do esquema e a entrada do log são criadas.
  - Nenhuma informação de capítulos futuros aparece na ficha.

## Teste 2: semeadura de erros (detecção)

- **Entrada:** cópia do capítulo 46 com quatro erros inseridos, pronta em `decisoes/teste-processo/cap46-semeado.txt`. A chave de respostas fica com o autor, fora do repositório. Na sessão de teste, não ler a chave nem comparar a cópia com `Livro 1/capitulo46.md`. O texto base tem um defeito real, nas linhas 75 a 77 (fala de Nolan sem texto), que não foi semeado: apontá-lo não conta como falso alarme. Os erros semeados:
  1. Vazamento de POV: Mário sabe algo que só Kate sabe.
  2. Fala com fecho aforístico.
  3. Fala longa de Lakand, quebrando a fratura de voz.
  4. Erro de nome: um personagem chamado de outro nome.
- **Passos:** rodar o fluxo de revisão (guardião de coerência, revisor linguístico e a lista de candidatos) sobre a cópia e comparar com a chave.
- **Critérios de aprovação:** pelo menos três dos quatro encontrados, e nenhum falso alarme grave.

## Teste 3: atribuição cega de falas

- **Entrada:** 12 falas de Kate, Nolan e Mário, sem o nome do falante, prontas em `decisoes/teste-processo/falas-teste-3.txt`. A chave fica com o autor. Na sessão de teste, não buscar essas falas no livro nem na storybible, porque o texto revela o falante.
- **Passos:** duas rodadas. Uma sem as fichas de voz e outra com as fichas de `vozes/`. O autor atribui cada fala.
- **Critério de aprovação:** a precisão com as fichas é claramente maior que sem elas. Se não for, as fichas não estão funcionando, e a diferença percebida é outra (vocabulário, por exemplo).

## Teste 4: consistência entre storybible e livro

- **Entrada:** os repositórios `livro` e `storybible`.
- **Passos:** um checklist automático que confere caminhos citados, nomes de personagens, capítulos com ingest e linhas do esquema.
- **Como rodar:** na raiz de `storybible`, `python3 scripts/checar_consistencia.py` (checklist; lê o `Livro` na pasta-irmã) e `bash scripts/mutacao.sh` (detecção: oito cenários em cópias descartáveis; o esperado é 8 de 8). Já executado em 2026-11-12.
- **Critério de aprovação:** o checklist precisa pegar os problemas já encontrados à mão: capítulos 34 a 38 sem ingest, caminhos antigos de `.github/`, a palavra "Iquize" fora do lugar (já removida), e capítulos sem linha no esquema.

## Registro

Os resultados vão para `storybible/decisoes/teste-processo-AAAA-MM-DD.md`, com o que passou, o que falhou e o que ajustar.

## Materiais

- Teste 2: `decisoes/teste-processo/cap46-semeado.txt`.
- Teste 3: `decisoes/teste-processo/falas-teste-3.txt`.
- Teste 4: `scripts/checar_consistencia.py` e `scripts/mutacao.sh`.
- Chaves dos testes 2 e 3: com o autor, fora do repositório. A sessão de teste não as lê.

## Custos

Testes 2 e 4 devem usar scripts sempre que possível, sem modelo. Testes 1 e 3 usam Sonnet. Ver a divisão de modelos por tarefa na conversa de 2026-11-12. Não usar Opus nos testes.
