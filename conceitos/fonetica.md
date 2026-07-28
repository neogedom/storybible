---
type: Concept
title: Dicionário Fonético
description: Guia de pronúncia para TTS/Minimax. Substituir termos originais pela versão fonética nos scripts de áudio.
tags: [conceito, fonetica, audio, TTS]
timestamp: 2026-07-24T12:00:00-03:00
---

# Dicionário Fonético

> Ao gerar scripts de áudio, substituir os termos originais pela **Versão Fonética**
> para pronúncia correta no sintetizador de voz.

| Original        | Fonética      | Notas |
| --------------- | ------------- | ----- |
| Genocydo        | Ghenócido     |       |
| Deltëra         | Deltéra       |       |
| Vonos           | Vônos         |       |
| Cressadar       | Cressadár     |       |
| Guenayer        | Ghenáier      |       |
| Daërunmege      | Daérunmedh    |       |
| Künervs         | Kúnervs       |       |
| Saramant        | Saramânt      |       |
| Mesmia          | Mésmia        |       |
| Souhma          | Sôuma         |       |
| Gaviorn'l       | Gaviorn'l     |       |
| Lakand          | Lêikand       |       |
| Vitysh          | Vitísh        |       |
| rampillas       | rampílas      |       |
| Devour d'Tirath | Devôr d Tirat |       |
| Charles         | Tcharles      |       |
| Opium           | Ópium         |       |
| Gornads         | Gornáds       |       |
| Rohdis          | Róhdis        |       |
| Koda            | Kôda          |       |
| Gerikhad        | Jerikádh      |       |
| Lupe'i          | Lupêi         |       |
| Decian          | Décian        |       |
| Kenod           | Kenód         |       |
| d'Teraghar      | Dhteragár     |       |
| Valinor         | Valinór       |       |
| Addorbek        | Adôrbék       |       |
| Godi            | Godí          |       |
| Devour          | Devôr         |       |
| Ornick          | Orníck        |       |
| Nuh             | Nú            |       |
| Gerdialias      | Gerdiálias    |       |
| Dagmar          | Dagmár        |       |
| Ornickenho      | Ornikênho     |       |

---

## Acentuação Fonética de Tritongos e Ditongos Decrescentes

> Regra geral para o script de narração Minimax: após a substituição dos nomes
> (tabela acima), percorra TODO o texto e adicione acento agudo (`´`) na **vogal
> forte** (a, e, o) de cada tritongo ou ditongo decrescente que ainda não possua
> acento gráfico.

### Definições

| Fenômeno                | Estrutura                                              | Exemplos                   |
| ----------------------- | ------------------------------------------------------ | -------------------------- |
| **Ditongo decrescente** | Vogal forte + vogal fraca (mesma sílaba)               | ai, ei, oi, ui, au, eu, ou |
| **Tritongo**            | Vogal fraca + vogal forte + vogal fraca (mesma sílaba) | uai, uei, uau, iau         |

> ⚠️ Não alterar ditongos nasais já marcados (ão, õe, ãe, ãi).
> ⚠️ Não alterar palavras já acentuadas ortograficamente (céu, mãe, herói).
> ⚠️ Não confundir hiato com ditongo (ex: "país" é hiato, não ditongo).

### Tabela de Substitution

| Sequência        | Acento                                                | Exemplos |
| ---------------- | ----------------------------------------------------- | -------- |
| ai (tônico) → ái | `mais` → `máis`, `pai` → `pái`, `cai` → `cái`         |
| ei (tônico) → éi | `leite` → `léite`, `peito` → `péito`, `deus` → `déus` |
| oi (tônico) → ói | `noite` → `nóite`, `coisa` → `cóisa`, `foi` → `fói`   |
| ui (tônico) → úi | `cuidado` → `cúidado`, `muito` → `múito`              |
| au (tônico) → áu | `mau` → `máu`, `causa` → `cáusa`, `pausa` → `páusa`   |
| eu (tônico) → éu | `meu` → `méu`, `seu` → `séu`, `neutro` → `néutro`     |
| ou (tônico) → óu | `sou` → `sóu`, `vou` → `vóu`, `ouro` → `óuro`         |
| uai → uái        | `Paraguai` → `Paraguái`, `iguais` → `iguáis`          |
| uei → uéi        | `enxaguei` → `enxaguéi`, `averiguei` → `averiguéi`    |
| uau → uáu        | `uau` → `uáu`                                         |

### Regras de ouro

1. Acento **sempre na vogal forte** (a, e, o) do ditongo/tritongo.
2. Só acentuar se a sílaba que contém o ditongo/tritongo for a **sílaba tônica** da palavra.
3. Se a palavra já está na tabela fonética acima (nomes de fantasia), a versão fonética já contém o acento correto — não duplicar.
4. Tratar APENAS ditongos decrescentes orais. Ditongos nasais (ão, õe) não precisam de alteração.
5. Em caso de dúvida se uma sequência é ditongo ou hiato, preservar a ortografia original (não arriscar acento falso).
