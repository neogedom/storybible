# Teste 4 do processo: consistência storybible ↔ livro

Data: 2026-11-12
Plano: `decisoes/plano-teste-processo.md`, Teste 4
Método: script somente leitura, sem modelo (conforme o plano). Nenhum arquivo dos repositórios foi alterado pelo teste.
Script: `/tmp/claude-0/-home-user/de91e502-c9c7-55c5-bd46-45c39263d024/scratchpad/checar_consistencia.py` (fora do repositório; a decisão de versioná-lo fica para o autor). Os testes de detecção estão em `scratchpad/mutacao.sh`.

## Veredito

**Passou no critério de detecção.** O checklist aponta os quatro problemas que o plano exige (caps. 34 a 38 sem ingest, caminhos antigos de `.github/`, "Iquize", capítulo sem linha no esquema). Três deles já estão corrigidos no estado atual, então a detecção foi verificada reintroduzindo cada problema em uma cópia descartável (tabela abaixo).

O teste também encontrou problemas reais que não estavam na lista. O mais grave está no próprio texto do livro (achado 1).

## Detecção: problemas reintroduzidos em cópia

| # | Problema | Resultado |
|---|---|---|
| M1 | Caps. 34 a 38 sem ingest (problema encontrado à mão) | PASS (5 caps. apontados) |
| M2 | Nome "Iquize" fora do cânone (encontrado à mão) | PASS (aparece em ❓) |
| M3 | Caminho `.github/` antigo em documento vivo (encontrado à mão) | PASS |
| M4 | Capítulo sem linha no esquema (encontrado à mão) | PASS |
| M5 | POV divergente entre esquema e ficha | PASS |
| M6 | Caminho citado que não existe | PASS |
| M7 | "?" no lugar de letra em capítulo que estava limpo | PASS |
| M8 | Seção "Pendências" vazia (caso dos caps. 37 e 38) | PASS |

Resultado: 8 de 8.

## Estado atual dos problemas encontrados à mão

- **Caps. 34 a 38 sem ingest**: resolvido. As fichas existem, e o log registra a refação de hoje. Restam pendências: ver achado 4.
- **Caminhos `.github/` antigos**: nenhum em documento vivo. Só duas menções intencionais, em contexto de histórico ou negação (`conceitos/glossario.md:68` e `.claude/agents/livro-writer.md:22`).
- **"Iquize"**: ausente de todo o livro e da storybible.
- **Capítulo sem linha no esquema**: resolvido. Os 68 capítulos têm linha. Resta a linha do cap. 38 marcada como "sem entrada própria" (achado 4).

## Achados reais (estado atual)

### 1. Texto corrompido no livro (crítico)

Em **20 arquivos** do livro (`Livro 1/capitulo48.md` a `capitulo66.md` e `epilogo.md`) há **2.020 ocorrências de "?" no lugar de letras acentuadas**: "N?o", "M?r", "S?o Paulo", "persegui??o", "Metr?pole". Os caps. 1 a 47 e o prólogo estão limpos.

- Origem no git: o commit `786ee5d` (2026-11-05, "Add chapters 62 to 66 and epilogue...") adicionou os arquivos 46 a 66 e o epílogo de uma vez. Não há versão anterior limpa no repositório.
- Não corrigi. A letra certa depende do contexto ("M?r" pode ser "Mar" ou "Mór"), e o texto só muda em lote pedido pelo autor. Precisa restaurar a partir do texto de origem.

### 2. Grafias e nomes no livro

- `Livro 1/capitulo13.md:187`: "Dërunmege". A grafia predominante é "Daërunmege" (49 ocorrências no livro e 82 na storybible). A storybible também usa a forma sem trema "daerunmege(s)" (17 ocorrências): decidir a grafia canônica.
- `Livro 1/capitulo18.md:83`: "Kate Daggon". Sobrenome sem nenhuma ocorrência na storybible. Decidir se entra no cânone ou sai do texto.

### 3. Referências a arquivos que não existem em documentos vivos (❌)

Agentes e skills do livro apontam para nomes do layout antigo:

- `.claude/memoria/stc-beat.md`: em `arquiteto-densidade.md:80`, `guardiao-coerencia.md:70` e `livro-writer.md:159`. O diretório não existe no disco, não está no `.gitignore` e nunca esteve no git.
- `GLOSSARIO.md`: em `revisor-linguistico.md:32` e `:92`, e `revisar-trecho/SKILL.md:116`.
- `SERIE.md`, `TOM-GENERO.md`, `PERSONAGENS.md`: em `coerencia-visual-imagens/SKILL.md:15` e `revisar-trecho/SKILL.md:113-115`. O equivalente atual de `TOM-GENERO.md` é `temas/tom-genero.md`. Os outros dois precisam ser verificados.
- `esquema-l1.md` solto: em `livro-writer.md:136` e `protocolo-ingest.md:65`. O caminho certo é `temas/esquema-l1.md`.
- `storybible/temas/outline.md:17`: aponta para `memories/repo/arquiteto-densidade-avaliacao-l1.md`, que não existe.

### 4. Fichas e esquema dos caps. 23 a 38

- `capitulos/capitulo-23.md`: não tem seção de sementes. O conteúdo existe, mas como rótulo `sementes:` (linha 22) em vez de `## Sementes e conexões`.
- `capitulos/capitulo-37.md` e `capitulo-38.md`: a seção `## Pendências para o autor` está vazia. Os itens ficaram embaixo de `## Canon (decidido pelo autor em 2026-11-12)`. Pode ser intencional, mas parece erro de posição.
- `capitulos/capitulo-34.md` (2 pendências), `capitulo-35.md` (2) e `capitulo-36.md` (1): pendências abertas, registradas pelo próprio processo.
- `temas/esquema-l1.md`, linha do cap. 38: "Ponto Central (sem entrada própria)". Pendência já registrada no log.

### 5. Registros históricos (⚠️, não corrigidos)

18 referências a caminhos antigos em `decisoes/` e `insights/`. São fotografias do momento em que foram escritas. Só registrar, não corrigir.

## Ressalvas do checklist

- Ruído na seção de nomes: 28 candidatos, a maioria palavras do mundo real ("Constituição", "Trindade", "Renascentismo") ou nomes que o autor só precisa confirmar. Serve como fila de revisão, não como erro.
- A expectativa de ingest usa o trecho "revisão manual, a partir do cap. 46" de `docs/handoff/estado-estrategico.md`. Se esse marco mudar, o checklist muda junto.
- Caminhos são resolvidos a partir da pasta do documento, da raiz de cada repositório e da pasta-pai (onde os docs escrevem `Livro/...` e `storybible/...`).
- Não é possível garantir ausência de erro. O checklist pega o que tem forma verificável.

## O que ajustar (decisão do autor)

1. Restaurar os caps. 48 a 66 e o epílogo a partir do texto de origem. Fazer isso antes de qualquer revisão desses arquivos.
2. Decidir a grafia canônica de "Daërunmege" e corrigir `capitulo13.md:187`.
3. Decidir se "Kate Daggon" entra no cânone (`capitulo18.md:83`).
4. Mover os itens dos caps. 37 e 38 para a seção de pendências, ou confirmar que a posição é intencional.
5. Transformar o rótulo `sementes:` do cap. 23 em seção `## Sementes e conexões`.
6. Atualizar as referências antigas de agentes e skills listadas no achado 3.
7. Atualizar `temas/outline.md:17`.
8. Decidir onde o script fica: pode ir para `storybible/scripts/` e rodar no processo de congelamento.

## Registro de execução

- Teste 4: executado. Passou no critério de detecção. Achados reais acima.
- Testes 1, 2 e 3: não executados.
- Nada foi commitado. Branch de trabalho atual: `ccr-a010bd86-ntyqcg` (o plano cita `claude/port-github-agents-n5ufc8`, que não é mais a branch em uso).
