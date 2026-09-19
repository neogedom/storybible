# Protocolo INGEST — Finalização de Capítulo

> **Dois modos.** O **Mini-INGEST** roda a cada capítulo fechado durante a
> escrita privada do L1 (gatilho "cap. X pronto"); o **INGEST completo** roda
> no congelamento (gatilho "Finalizar capítulo X"). Norte: avançar sobre
> aperfeiçoar; revisão fina só no congelamento (ver
> `decisoes/estrategia-publicacao-l1.md`).

---

## Mini-INGEST (modo privado)

### Quando executar

Usuário diz **"cap. X pronto"** ao fim da sessão em que o capítulo atingiu a
Definition of Done (prosa completa, fronteira ok).

### Passos (agente, ~15-20 min)

1. Criar `capitulos/capitulo-XX.md` (type: Chapter) com frontmatter mínimo
   (`pov`, `beat_stc`, `percentual_l1` — a **posição real** do capítulo na
   régua vigente; ver nota de réguas em `temas/esquema-l1.md`) e 4 seções
   curtas: Resumo (3-6 linhas),
   Personagens, Eventos, Sementes e Conexões.
2. Append em `visuais/<nome>.md`: estado visual de quem apareceu; "não
   aparece" dos esperados.
3. Registrar canon duro novo: regra de mundo, milagre (com o custo), mudança
   de relação/posição → `conceitos/`; semente cross-livro nova → `temas/sementes.md`.
4. Atualizar a tabela de progresso em `temas/esquema-l1.md` (1 linha).
5. Checagem de fronteira: reler o Mini-INGEST do capítulo anterior + o bloco
   do próximo no esquema (sem contradição; ponto de partida claro). Anotar
   **como o capítulo fecha** — decisão (personagem escolhe) ou desastre
   (algo dá errado)? Desastre sem sequel → o próximo abre processando;
   decisão → o próximo abre executando. Decisão adiada há mais de 2
   capítulos: sinalizar no esquema (dívida — não reescrever). Anotar também
   **onde o capítulo corta** (A/B/C/D — ver `passe-fechos.prompt.md`, no
   Livro): é o dado que alimenta o passe de fechos do checkpoint.
6. `log.md`: 1 linha (pode ser batch a cada 5 caps).
7. Contador de checkpoint: verificar quantos capítulos passaram desde o
   último checkpoint registrado no `log.md` (se nunca houve, contar desde o
   início do bloco/beat). Da **6ª** marca em diante → **oferecer ao autor**
   o checkpoint leve (decisão do autor, 2026-09-14), que roda sobre os
   capítulos fechados desde o último checkpoint:
   - **Arquiteto de Densidade** — leve, nas fronteiras de beat: corrige o
     mapa para frente, nunca o texto.
   - **Passe anti-slop em lote** — cirurgia local (teste F13).
   - **Passe de fechos** — cortes A/B/C/D do bloco, repetição de gesto
     final, rotação de POV e quem decide em cada capítulo
     (`passe-fechos.prompt.md`, no Livro).
   Executado, registrar no `log.md`.

### Obrigatório agora vs. espera o congelamento

| Obrigatório (Mini-INGEST) | Espera o congelamento |
|---|---|
| Fatos duros: eventos, decisões, localização, canon novo, custo do milagre | Análise de arco psicológico em `personagens/` |
| Sementes novas (promessas + cross-livro) | LINT completo (cruzamento com histórico) |
| Visual de cada personagem que aparece | `index.md`, log detalhado, expansão de conceitos |
| Ponto de partida do próximo capítulo | Polimento (densidade fina/linguística), áudio, reconciliação com versão pública 0-19 |

> **Anti-slop (decisão do autor, 2026-09-12):** o **passe anti-slop** (cirurgia
> local — teste F13) roda **em lote no checkpoint de beat** (passo 7), cobrindo
> os capítulos fechados desde o último checkpoint — não roda por capítulo no
> modo privado. No congelamento permanece só a **varredura final leve**
> (uniformidade + capítulos com reescrita pesada).

> **Passe de fechos (decisão do autor, 2026-09-14):** no mesmo checkpoint,
> além do anti-slop, roda o **passe de fechos** (`passe-fechos.prompt.md`, no
> Livro). Ele lê o bloco **como sequência**, não capítulo a capítulo: onde
> cada capítulo corta (A/B/C/D), se dois fechos seguidos repetem o mesmo
> gesto ("norte", corpo em movimento, "E" inicial), como girou o POV e quem
> **decidiu** em cada capítulo. Diagnóstico + marcas no `esquema-l1.md` para
> os caps. futuros — nunca reescreve prosa no modo privado.

Regra de bolso: `personagens/<nome>.md` só muda quando um **fato duro** muda
(nova habilidade, morte, mudança de papel). Estado cena-a-cena vive em
`capitulos/capitulo-XX.md`.

### Semáforo de ideias

- **Verde (micro):** detalhe local que não toca esquema/arco/canon → implementa, zero registro.
- **Amarelo (estrutural):** mudaria capítulo/arco/canon → **não implementa**; registra em `insights/` com `destino: L2/L3` ou `destino: congelamento-L1`.
- **Vermelho (guardrail):** viola teologia/risco estrutural → registra e alerta; nunca implementa.

`temas/esquema-l1.md` é o contrato: nunca editá-lo no meio de um capítulo.
Ideias absorvem para frente.

### Definition of Done (modo privado)

1. Prosa completa em `Livro 1/capituloXX.md` (sem markdown, POV do beat).
2. Mini-INGEST feito.
3. Checagem de fronteira ok.
4. Nenhuma pergunta em aberto bloqueando o próximo capítulo (resolvida ou estacionada em `insights/`).
5. Canon duro novo registrado (ou estacionado).
6. Anti-slop e passe de fechos em dia: rodam em lote no checkpoint (passo 7) — **não** são exigência por capítulo.
7. Próximo capítulo NÃO começa antes do Mini-INGEST.

---

## INGEST completo (congelamento)

### Quando executar

Usuário diz **"Finalizar capítulo X"** após o ciclo de revisão estar completo.

## Pré-condições

- [ ] Capítulo X está finalizado em `neogedom/livro/Livro 1/capituloX.md`
- [ ] Ciclo de revisão foi executado (densidade → coerência → linguística)
- [ ] Áudiochapter gerado (se aplicável)

## Passos

### 1. Leitura do capítulo

- [ ] Ler o capítulo completo de `neogedom/livro/Livro 1/capituloX.md`
- [ ] **Nunca** modificar o arquivo original

### 2. Extração de fatos

Para cada cena do capítulo, extrair:

#### Personagens

- [ ] Personagens presentes e seus estados físicos/emocionais
- [ ] Decisões tomadas por cada personagem
- [ ] Falas que revelam personalidade, conflito ou lore
- [ ] Mudanças de papel ou posição na hierarquia

#### Eventos

- [ ] Eventos relevantes para a trama principal
- [ ] Eventos que podem ser sementes para capítulos futuros
- [ ] Mudanças de localização dos personagens

#### Sementes plantadas

- [ ] Informações reveladas que ainda não foram explicadas
- [ ] Promessas narrativas (coisas que o leitor espera ver resolvidas)
- [ ] Conexões com capítulos anteriores

#### Avanço narrativo

- [ ] Posição no beat do Save The Cat! (qual beat, % de avanço)
- [ ] Progresso no arco de cada personagem presente

### 3. Extração visual

Para cada personagem que **aparece** no capítulo:

- [ ] Roupas e equipamento (novos ou alterados?)
- [ ] Ferimentos, cicatrizes, sujeira
- [ ] Mudanças de cabelo/estilo/barba
- [ ] Expressão predominante
- [ ] Condição geral (saudável, ferido, exausto, etc.)

Para personagens que **não aparecem**, o registro visual recebe "não aparece".

### 4. Atualização da Story Bible

- [ ] **Criar/atualizar** `capitulos/capitulo-XX.md` (type: Chapter) com:
  - Frontmatter: POV, timeline, STC beat
  - Seções: Resumo, Personagens, Eventos, Sementes, Conexões
  - Links para outros capítulos e conceitos

- [ ] **Atualizar** `personagens/<nome>.md` de cada personagem presente:
  - Adicionar novos fatos de arco
  - Atualizar relações com outros personagens
  - Registrar evolução emocional/psicológica

- [ ] **Atualizar** `visuais/<nome>.md` de cada personagem:
  - Adicionar entrada do capítulo com estado visual
  - Se não apareceu, registrar "não aparece"

- [ ] **Atualizar** `conceitos/` afetados pelos eventos do capítulo

- [ ] **Atualizar** `lugares/` se novos locais forem introduzidos

- [ ] **Atualizar** `temas/` se o capítulo avançar temas transversais

### 5. Verificação de coerência (LINT automático)

- [ ] **Cruzar fatos**: comparar cada fato extraído com todos os capítulos anteriores
- [ ] **Detectar contradições**: mesma informação dita de forma diferente, eventos incompatíveis, timelines conflitantes
- [ ] **Verificar consistência visual**: personagem não pode ter roupa diferente da registrada sem transição
- [ ] **Verificar links**: todos os links criados no novo documento funcionam
- [ ] **Reportar ao usuário**: lista de contradições encontradas (se houver)

### 6. Finalização

- [ ] Atualizar `index.md` se novas categorias ou entradas forem necessárias
- [ ] Registrar operação em `log.md` (data, capítulo, resumo)
- [ ] Reportar resumo ao usuário

---

## Protocolo INGEST — Insights Automáticos

### Quando executar

Automaticamente durante conversas no chat, quando o agente detecta:

| Situação                                                  | O que salvar                 | Onde                           |
| --------------------------------------------------------- | ---------------------------- | ------------------------------ |
| Usuário diz "E se...", "que tal..." e a ideia é explorada | Ideia aprovada               | `insights/`                    |
| Usuário confirma "é, faz sentido", "vamos nessa"          | Decisão confirmada           | `decisoes/`                    |
| Usuário diz "não, isso não funciona porque..."            | Ideia rejeitada + motivo     | `ideias-rejeitadas/`           |
| Conexão entre dois conceitos é descoberta                 | Atualizar páginas existentes | conceito afetado               |
| Semente narrativa identificada                            | Registrar semente            | capítulo ou sementes pendentes |

### Regras

- Só salvar se o conteúdo for **novo** (verificar se já existe na storybible)
- **Não** salvar perguntas exploratórias sem resolução
- **Não** salvar conversas puramente factuais (ex: "qual a cor do cabelo do Mário?")
- Ao final da resposta, incluir resumo discreto: `📥 storybible: 1 insight, 1 decisão, 1 conceito atualizado`
- Se nada foi salvo, não mencionar

---

## Protocolo INGEST — Referências Externas

### Quando executar

Usuário adiciona material de referência (ex: resumo de livro, artigo, palestra).

### Passos

1. Ler o material
2. Discutir com o usuário os pontos relevantes para o universo
3. Destilar em documento curto (3-5 parágrafos) em `conceitos/`
4. Adicionar links para capítulos que utilizam aquele conceito
5. Atualizar `index.md` e `log.md`
