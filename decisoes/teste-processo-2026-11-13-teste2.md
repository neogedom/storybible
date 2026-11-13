---
type: Decision
title: Resultado do teste 2 do processo (semeadura de erros)
description: Lista de candidatos produzida pelo fluxo de revisão sobre a cópia semeada do capítulo 46, para o autor comparar com a chave.
tags: [processo, teste, resultado]
timestamp: 2026-11-13T12:00:00-03:00
---

# Teste 2: semeadura de erros (2026-11-13)

Entrada: `decisoes/teste-processo/cap46-semeado.txt`. Fluxo: `guardiao-coerencia` e `revisor-linguistico` (Sonnet, somente leitura, sem edição). Chave não lida. Cópia não comparada com `Livro 1/capitulo46.md`.

**Veredito: pendente.** A comparação com a chave é do autor. Abaixo, os candidatos por categoria de erro semeado.

## Candidatos por categoria

| Erro semeado | Candidato | Fonte | Confiança |
| --- | --- | --- | --- |
| 1. Vazamento de POV | L35: "Mário já sabia do bilhete que ela escondera na bota, e nunca perguntara por ele." (Kate sabendo o que Mário sabe; "bilhete" não existe na storybible) | guardião | média-baixa |
| 2. Fecho aforístico | L99, Kate: "Quem entrega um inocente já escolheu o próprio carrasco." | guardião e linguístico | alta |
| 3. Fala longa de Lakand | L133, monólogo de cerca de 90 palavras terminando em aforismo | guardião e linguístico (este só como aforismo) | alta |
| 4. Erro de nome | L69: "o general Valenor" (canon: Valinor Addorbek) | guardião | alta |

O linguístico não pegou o nome (listou "Valenor" entre os nomes que não conseguiu validar) nem o vazamento de POV (L35 só como frase solta, sem relação com o parágrafo).

## Outros achados (não semeados ou duvidosos)

- Guardião: fecho sentencioso em Nolan (L107, média); fala de Lakand na L41 longa e terminando em "Somos presas" (baixa-média); Nolan chamando o rei de louco e desconfiando de Benjamim (L87, baixa).
- Defeito real do texto base, L75 a 77 (fala de Nolan sem texto): apontado pelos dois. Conforme o plano, não conta como falso alarme.
- Linguístico, confiança alta e real: L21 "para fumaça" (falta artigo); L23 "antes dos Clãs descerem"; L31 "não passava despercebida" e "postura" repetida; oscilação "os/as Espadas da Lei" (L55, L65, L69); ideia "preciso dele vivo" repetida (L33, L87, L103).
- Linguístico, ruído: cerca de metade dos 47 itens foi descartada pelo próprio agente no texto ("sem erro", "descarto"); muitos outros são preferência estilística. Ele também marcou como aforismo falas que podem ser legítimas (L33, L41, L93, L127).

## Contaminação do teste (ajustar no próximo)

- O guardião leu `capitulos/capitulo-46.md` (ficha do capítulo original) e `vozes/kate.md`, que cita a fala canônica de Kate (nº 6) sem o fecho. Ele declarou usar a ficha "só para localizar divergências". Isso é comparação indireta com o original e pode ter inflado a detecção dos erros 2 e 4. A instrução do plano só proíbe ler a chave e comparar com `Livro 1/capitulo46.md`; vale decidir se a ficha também deve ficar de fora.
- Para uma medida limpa, repetir o guardião sem acesso a `capitulos/capitulo-46.md`.

## Rodada 2: guardião sem a ficha do capítulo

Isolamento: o agente não abriu `capitulos/capitulo-46.md` nem `decisoes/`, mas houve vazamento parcial, informado por ele: um grep em `capitulos/` exibiu linhas do resumo do cap. 46; `vozes/kate.md`, `vozes/nolan.md`, `lugares/metropole.md`, `lugares/cidadela-de-gus.md` e `conceitos/clas-de-sangue.md` citam o cap. 46. Ele declarou ter ignorado esse conteúdo como fonte. Isolamento total não é possível enquanto a storybible referenciar o capítulo; o que dá para fazer é limitar a leitura direta.

Resultado por categoria:

| Erro semeado | Candidato na rodada 2 | Confiança |
| --- | --- | --- |
| 1. Vazamento de POV | L35 (bilhete) **não foi apontada**. Apontou L1: Kate sabendo nome e filiação de Ossan ("Ossan d'Tirath, filho de Devour"), sem fonte em capítulo de POV dela | média |
| 2. Fecho aforístico | L99, Kate | alta |
| 3. Fala longa de Lakand | L133 (e também L41) | alta |
| 4. Erro de nome | L69, "Valenor" em vez de Valinor | alta |

Os erros 2, 3 e 4 se repetiram sem a ficha do capítulo, então a detecção deles não dependeu dela. O erro 1 mudou de candidato entre as rodadas (L35 na primeira, L1 na segunda): é o ponto fraco da detecção e o que a chave resolve.

Novos candidatos da rodada 2, a conferir se são preexistentes no original ou falsos alarmes:

- L45: "degelo da serra" contra o outono em `temas/timeline.md` (média).
- L31: "aro de prata" contra "armação de ébano" no cap. 4 e na ficha de Nolan (média; o agente nota que `vozes/nolan.md` já cita "aro de prata" para o cap. 46, o que sugere texto original).
- L83: Kate "quase esboçando um sorrisinho" contra "humor seco, sem sorriso" (média).
- L1/L27/L29: Orval sem apresentação; L37: "o prazo dele" sem antecedente; L61/L41: Clãs ao sul e ao norte (média).
- L127 Decian, L135 "adaga" contra faca de caça, L89 Ossan "posso usá-los", vocabulário das embarcações (baixa).

## Para o autor

Comparar as tabelas das duas rodadas com a chave. Critério do plano: pelo menos 3 de 4 encontrados e nenhum falso alarme grave. Os erros 2, 3 e 4 foram apontados com confiança alta nas duas rodadas. O erro 1 depende de qual candidato (L35 ou L1) é o semeado; se nenhum, a detecção é 3 de 4, ainda dentro do critério. Dizer quais candidatos novos da rodada 2 são falsos alarmes e se algum é grave.

## Conferência com a chave (2026-11-13)

Conferido contra a chave do teste, guardada fora do repositório.

| Erro semeado | Rodada 1 | Rodada 2 |
|---|---|---|
| 1. Vazamento de POV (L35) | apontado | não apontado (apontou L1, ver abaixo) |
| 2. Fecho aforístico (L99) | apontado | apontado |
| 3. Fala longa de Lakand (L133) | apontado | apontado |
| 4. Nome "Valenor" (L69) | apontado | apontado |

- Rodada 1: 4 de 4. Rodada 2: 3 de 4.
- Defeito real do texto base (L75 a 77): apontado nas duas rodadas. Não conta como falso alarme.
- L1 (Kate conhecer nome e filiação de Ossan): não é erro semeado; a frase já estava no original. Possível problema real do texto, para o autor avaliar. Não é falso alarme grave.
- Veredito pelo critério do plano (pelo menos 3 de 4, sem falso alarme grave): **passou**.
- Contaminação: a rodada 1 leu a ficha do cap. 46. Por isso a rodada 2 é a medida mais limpa. Regra de isolamento incluída no plano.
