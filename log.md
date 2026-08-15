# Log de Atualizações

## 2026-08-15 (auditoria de voz de Nolan — caps. 0-20)

- **Auditoria completa das falas de Nolan** (~115 falas/pensamentos): 4 correções
  aplicadas ("Cadê" → "Onde está"; subjuntivo indevido "haja" → "há";
  "lembro-te" ao Rei → "lembro a Vossa Majestade"; "Kôda" → "Koda").
- **Canon corrigido**: nome do personagem é **Edgard Lupe'i** (cap. 3 usava
  "Vyengard") — alinhado com `personagens/lupei.md`.
- **Risco #2 avaliado**: bem mitigado (Nolan erra no cap. 13, é enganado no 6,
  falha no 9, paga em 16/18). Fresta do trauma do pai (cap. 9) registrada como
  oportunidade.
- **Arquivos**: `Livro 1/capitulo3.md`, `Livro 1/capitulo6.md`, `log.md`.

## 2026-08-15 (auditoria de voz de Kate — caps. 0-20)

- **Auditoria completa das falas de Kate** (~119 falas/pensamentos, 9 capítulos):
  2 aforismos do cap. 5 corrigidos ("Quase não enche cova, irmão..."; "Tamanho
  sem cabeça..."), 1 ruído de voz na narração do cap. 8 corrigido (luta como
  salvação, em registro concreto), travessão U+2015 → U+2014 nas falas de
  Tharin (cap. 5).
- **Arquivos**: `Livro 1/capitulo5.md`, `Livro 1/capitulo8.md`, `log.md`.

## 2026-08-15 (auditoria de voz de Mário — caps. 0-20)

- **Auditoria completa das falas de Mário** (78 falas, 76 coerentes): 2 ajustes
  aplicados (fechamento aforístico do cap. 12 → transação; jurista ausente no
  pacto da Mina, cap. 20). Exceção canônica mantida (oração do cap. 19,
  ditada pela Voz).
- **Nova regra de voz**: fechamentos de argumento terminam em transação/
  evidência, nunca em aforismo. Registrado em `temas/tom-e-voz.md`.
- **Arquivos**: `Livro 1/capitulo12.md`, `Livro 1/capitulo20.md`,
  `temas/tom-e-voz.md`, `log.md`.

## 2026-08-15 (lote 2 de comentários — cap. 20, persona de Mário, Mina/Segregação)

- **Lote 2 aplicado no cap. 20**: fala de Kate reescrita na voz dela (concreta:
  "Escravo que vê um morto voltar não teme mais o chicote...") — removida a
  sensação de filosofia; marcadores respondidos (oração/Voz; Mina temporal;
  persona de Mário).
- **Pendência resolvida**: fluência em ornickenho confirmada no **cap. 12**
  (autor corrigiu: "Eu errei") — ficha de Mário já está correta.
- **Novo canon — persona de Mário**: terráqueo, morador de Goiânia (GO),
  século XXI; voz de jovem urbano brasileiro moderno. Registrado em
  `personagens/mario.md`.
- **Novo canon — Mina de Quartzo**: só virou reduto de escravidão de humanos
  com a Segregação (antes, mina com outras formas de trabalho). Registrado em
  `conceitos/segregacao.md`.
- **Workflow — links de linha no relatório do lote**: agentes e skills
  passam a reportar cada alteração com link de âncora de linha
  (`path#L{linha}`).
- **Arquivos**: `Livro 1/capitulo20.md`, `personagens/mario.md`,
  `conceitos/segregacao.md`, `log.md`.

## 2026-08-15 (lote de comentários do autor — cap. 20 + canon Lucas)

- **Lote de comentários do autor aplicado no cap. 20** (protocolo `(* ...)`):
  (a) glossolalia sem espanto de idioma — Voz ≠ Deus para Mário ("soco na
  porta da Voz", não "do Deus"); (b) distância Kate/Lakand sem comparação
  temporal (POV de Mário); (c) vozes de Mário e Kate ajustadas na cena da
  Mina; (d) artefato tipográfico corrigido.
- **Novo canon — Lucas (Terra)**: irmão de Mário, morreu por drogas; caco de
  vidro = culpa teológica (não tinha a teologia certa à época) → estudo
  obsessivo e arrogância teológica. Registrado em `personagens/mario.md`.
- **Pendência (resolvida 2026-08-15)**: fluência em ornickenho confirmada no
  **cap. 12** — o autor corrigiu a informação (era cap. 12, não cap. 7).
- **Arquivos**: `Livro 1/capitulo20.md`, `personagens/mario.md`, `log.md`.

## 2026-08-14 (canon — manto de xilomagia: gatilho, carga finita, recarga)

- **Gatilho (canon)**: manto fechado sobre o corpo + imobilidade +
  respiração controlada em ciclo lento; camufla com a madeira presente
  (viva ou trabalhada) — floresta total, mina/cidade situacional, pedra nua
  falha; tell: movimento/fôlego alto quebram a trama (cap. 5).
- **Carga (canon)**: xilomagia armazenada FINITA, gasta no uso; sem recarga
  natural — só ritual de xilomago. Potencial: **Ossan** (irmão d'Tirath,
  asset de Nolan, L2; o manto provavelmente não chega a ele). Para Kate no
  L1: efeitos acabam — depleção NA PÁGINA (momento crítico).
- **Kate pragmática (canon)**: posse por conquista — "É a minha. Tomei de
  quem não sabia usar." Frases de apego removidas do cap. 20 (prova o manto
  como ferramenta, sem "sempre foi").
- **Arquivos**: `decisoes/manto-xilomagia-tharin.md`, `temas/sementes.md`,
  `index.md`, `log.md` + cap. 20 (Livro 1).

## 2026-08-13 (protocolo — loop de escrita privada embutido)

- **Mini-INGEST (modo privado)** criado em `protocolo-ingest.md`: gatilho
  "cap. X pronto", passos leves (~15-20 min), tabela "obrigatório agora vs.
  espera o congelamento", semáforo de ideias, Definition of Done. INGEST
  completo renomeado para "INGEST completo (congelamento)".
- **Agentes atualizados**: `livro-writer.agent.md` (modo privado: Mini-INGEST
  por capítulo, avançar > aperfeiçoar, checkpoint de beat a cada ~6-10 caps)
  e `arquiteto-densidade.agent.md` (checkpoint leve em fronteira de beat,
  corrige o mapa para frente). `copilot-instructions.md` do repo Livro ganhou
  bloco "Modo de Escrita Privada (loop ativo)". `AGENTS.md` distingue os dois
  modos de INGEST.
- **Arquivos**: `protocolo-ingest.md`, `AGENTS.md`, `log.md` + repo Livro
  (`.github/copilot-instructions.md`, `.github/agents/livro-writer.agent.md`,
  `.github/agents/arquiteto-densidade.agent.md`).

## 2026-08-13 (estratégia — arquitetura de publicação do L1)

- **Nova decisão**: `decisoes/estrategia-publicacao-l1.md` — escrever o L1
  inteiro em privado → congelar canon → relançar (serial cap. 20+ com motor
  de aquisição novo + ebook completo) → áudio por último → self-publish antes
  de editora.
- **Pausa pública**: cap. 19 (sábado 15/08) encerra o Ato 1 (fim de temporada,
  não do livro).
- **Gargalo registrado**: aquisição (curva plana ~2 meses, ~15 seguidores,
  zero monetização). Fonte viva e completa:
  `Livro/.github/handoff/estado-estrategico.md`.
- **Arquivos**: `decisoes/estrategia-publicacao-l1.md`, `index.md`, `log.md`.

## 2026-08-12 (canon — Hoste da Purgação: um único vampiro)

- **Composição da Hoste (canon)**: a Hoste da Purgação reconstruída é
  **multirracial** — gornads, alguns lobisomens, canibais dos Clãs de
  Sangue e **um único vampiro**: o veterano do monte, o último verdadeiro
  Lorde Defunto. Por ser poderoso (a força de uma era de ouro num só
  corpo), pode ocupar **posição de destaque** na Hoste. Substituído o
  "vampiros (a confirmar)" em `conceitos/lordes-defuntos.md`,
  `conceitos/hicse.md`, `temas/sementes.md` e `temas/esquema-l1.md`.
- **Arquivos**: `conceitos/lordes-defuntos.md`, `conceitos/hicse.md`,
  `temas/sementes.md`, `temas/esquema-l1.md`, `log.md`.

## 2026-08-12 (canon — o último verdadeiro Lorde Defunto)

- **Unicidade do veterano (canon)**: dos veteranos da era de ouro de
  Gondor, apenas **UM** verdadeiro Lorde Defunto sobreviveu: **o veterano
  do monte em Gondor** (holdout recrutado pela Hoste de Hícse no L2). A
  "Comunidade" de Opium não tinha verdadeiros Lordes Defuntos — só
  neófitos e sobreviventes menores. "Eles não estão acabados" (Decian,
  cap. 10) refere-se à **rede da Comunidade**, não a outros veteranos.
  Corrigido em `conceitos/lordes-defuntos.md`.
- **Arquivos**: `conceitos/lordes-defuntos.md`, `log.md`.

## 2026-08-12 (canon — cronologia da "Comunidade" de Opium: pós-declínio)

- **Cronologia (canon)**: a "Comunidade" de Opium **NÃO existia no auge de
  Gondor** — na era de ouro os vampiros dominavam, não negociavam. É um
  fenômeno **pós-declínio**: nasceu depois da queda, quando os sobreviventes
  empurrados para Saramant tentaram a **coexistência** em vez da dominação.
  Corrigido em `conceitos/lordes-defuntos.md` (nota de cronologia) e
  `lugares/opium.md` ("ressurgimento" → "se estabelecesse ali").
- **Arquivos**: `conceitos/lordes-defuntos.md`, `lugares/opium.md`,
  `log.md`.

## 2026-08-12 (correção — Interregno: Gondor não dominou os ~950 anos)

- **Correção conceitual (canon)**: o Interregno **não foi um único domínio
  estrangeiro**. Foi um período longo de instabilidade no Reino —
  sucessões desastrosas, períodos em que o próprio Reino dominou outras
  nações (por tempos mais curtos), e retomadas. Gondor subjugou o Reino
  **apenas numa parcela menor** desse tempo, mas foi a dominação **mais
  longa e mais difícil de derrotar** (nação mais poderosa que as
  anteriores). A era de ouro dos vampiros também se limita à dominação
  gondoriana, não aos 950 anos.
- **Arquivos**: `lugares/gondor.md`, `temas/timeline.md`,
  `conceitos/lordes-defuntos.md`, `log.md`.

## 2026-08-12 (documentação — página de Gondor)

- **Nova página**: `lugares/gondor.md` — império estrangeiro que dominou o
  Reino no Interregno; era de ouro dos vampiros (Lordes Defuntos, festas,
  künerv); Guerra dos Vampiros; rebelião fracassada; Guerra do Grifo
  (Kraviam vence com antraz); estado atual pós-Grifo. Lacunas marcadas
  como "a definir": geografia exata, poder atual, política pós-Grifo. O
  monte do veterano (L2) fica em território gondoriano.
- **Arquivos**: `lugares/gondor.md`, `index.md`, `log.md`.

## 2026-08-12 (canon — distinção: comunidade de Khaine ≠ "Comunidade" de Gondor)

- **Distinção (canon)**: a **comunidade de Khaine** (origem da raça,
  proto-histórica, que desafiou Terbs) **NÃO é** a **"Comunidade"** de
  Gondor/Opium (facção moderna da era de Gondor, exterminada por Charles).
  São entidades distintas que compartilham o nome — e o sangue (todo
  vampiro é filho de Khaine). Notas de distinção adicionadas em ambas as
  seções de `conceitos/lordes-defuntos.md`; a prosa deve manter a
  separação para não virar confusão.
- **Arquivos**: `conceitos/lordes-defuntos.md`, `log.md`.

## 2026-08-12 (canon — ruínas divinas no monte; nome livre)

- **Ruínas (canon)**: o monte do veterano guarda **ruínas antigas** que
  **sugerem** a habitação dos deuses de Ornick — mais antigas que a era de
  ouro de Gondor. O veterano acampou nas ruínas da habitação divina
  ("pertença, não apoteose" tornada espacial). Renderização: sugestão, não
  exposição (alvenaria ciclópica, símbolos erodidos, santuário desabado).
- **Nome do monte (canon)**: **livre** — não precisa ecoar montes da
  Terra. A definir com o autor.
- **Arquivos**: `conceitos/lordes-defuntos.md`, `log.md`.

## 2026-08-12 (canon — o monte do veterano; eco de Heiser)

- **Local do veterano (canon)**: **monte ermo** (não pântano). Motivo
  registrado: **eco de Heiser** — monte = lugar dos deuses (assembleia
  divina; no universo, contraponto ao Limbo e ao zigurate de Etemenanki).
  O veterano entronizado no monte é um **deus caído no trono dos deuses**;
  a prosa do L2 deve tratar o monte como santuário usurpado, não cenário.
- **Pendente**: nome e detalhes do monte (a definir com o autor);
  possível página de lugar — Gondor ainda não tem página de lugar (lacuna
  conhecida).
- **Arquivos**: `conceitos/lordes-defuntos.md`, `log.md`.

## 2026-08-12 (canon — mecanismo de sobrevivência; correção "künerv")

- **Mecanismo de sobrevivência do veterano (canon)**: opção A pura —
  **torpor profundo** + presas humanas **raras** que cruzam o ermo (uma
  refeição a cada meses/anos); sem vínculo/estoque vivo. Local a definir
  (monte/pântano).
- **Sangue animal NÃO sustenta (canon)**: só sangue de seres conscientes
  alimenta vampiro — explica a morte por inanição dos vampiros de Saramant
  numa floresta cheia de caça (cap. 8).
- **Preço da adesão (canon)**: Lakand oferece o **próprio sangue** ao
  antigo (o caçador alimenta o caçado) — primeiro degrau da escada da
  queda (depois entregar outros; por fim Kate).
- **Correção de lore (canon 2026-08-12)**: "filhos de Khaine" = os
  **próprios vampiros**; o sangue das "festas regadas a sangue" era de
  **humanos simpatizantes** (gondorianos), e dessa relação nasceu o termo
  **künerv** (pejorativo para humanos). Corrigido em
  `conceitos/lordes-defuntos.md`, `conceitos/glossario.md` (künerv) e
  `capitulos/capitulo-07.md` (semente).
- **Arquivos**: `conceitos/lordes-defuntos.md`, `conceitos/glossario.md`,
  `capitulos/capitulo-07.md`, `log.md`.

## 2026-08-12 (canon — Lakand como recrutador; veterano resignado)

- **Decisão (canon)**: **Lakand** é o PoV que passa para o lado de Hícse
  no L2 e viaja a Gondor para arregimentar o veterano da era de ouro.
  Corrupção via **Mesmia** (mesma facção de Hícse — ambas servas
  comissionadas de Marduk) funilando-o para a Hoste. Detalhe aprovado: o
  veterano **não dá mais festas** — está **escondido e resignado** num
  lugar ermo (monte/pântano), poderoso pela idade, mas em baixa; Lakand
  lhe oferece **"voltar a ser importante"**.
- **Condições de ofício acordadas**: PoV limitado (Vilões se Aproximam);
  morte de Kate **fora** do PoV de Lakand (vista pelo PoV de Kate);
  holdout em Gondor (veterano que nunca saiu do império); Benjamim
  permanece o cérebro dos bastidores (arranja a missão; Lakand executa).
- **Pendente de decisão**: mecanismo de sobrevivência do veterano (como
  ele se mantém vivo sem sangue em lugar ermo) — opções em discussão com
  o autor (torpor + presa rara vs. vínculo/estoque vivo; implicação de
  canon: sangue animal sustenta ou não?).
- **Arquivos**: `personagens/lakand.md`, `conceitos/lordes-defuntos.md`,
  `log.md`.

## 2026-08-12 (canon — página dos Lordes Defuntos; ideia de PoV do recrutador no L2)

- **Nova página**: `conceitos/lordes-defuntos.md` — lore consolidada:
  origem da maldição de Khaine, filhos de Khaine/Khainekravira, era de ouro
  sob Gondor, Guerra dos Vampiros, rebelião fracassada, Comunidade de Opium
  exterminada por Charles, neófitos vs. verdadeiros Lordes Defuntos, regras
  do mundo (sol, inanição, künerv) e germinação potencial no L2 (Hoste de
  Hícse). Índice e `terbs.md` atualizados com o link.
- **Ideia do autor (juízo pendente — NÃO canon)**: no L2, um PoV que passe
  para o lado de Hícse e viaje até Gondor para arregimentar o veterano da
  era de ouro (opção A). Pendências apontadas: (a) identificar o PoV —
  candidatos fortes: Benjamim (sem arco de L2 registrado; pivô Terbs→Hícse)
  ou novo personagem dos Clãs de Sangue; (b) conciliar a geografia — canon
  atual diz que os vampiros foram empurrados para Saramant pós-rebelião;
  (c) risco estrutural: PoV novo rouba protagonismo perceptivo de Mário —
  recomenda-se PoV limitado, não co-líder.
- **Arquivos**: `conceitos/lordes-defuntos.md`, `conceitos/terbs.md`,
  `index.md`, `log.md`.

## 2026-08-12 (canon — origem dos vampiros; destino de Etwano)

- **Origem da maldição (canon)**: em tempos distantes, uma comunidade
  desafiou **Terbs publicamente**, liderada por um homem chamado **Khaine**.
  Terbs amaldiçoou a comunidade inteira; Khaine foi o **primeiro vampiro**.
  "Filhos de Khaine" / "Khainekravira" = todos os vampiros; o termo nasce
  do nome do primeiro transformado. Registrado em `conceitos/terbs.md`
  (Criações) e `conceitos/glossario.md` (Khainekravira). O gancho das
  "festas de Gondor" do cap. 7 (filhos de Khaine, época de ouro) agora tem
  definição canônica.
- **Etwano (canon)**: morto no combate da torre — morte **implícita** no
  texto (cap. 7 termina no meio da luta; cap. 10 mostra Charles e Decian
  descartando todos os corpos: "Esse é o último"). A queima é **solar**
  (corpos jogados pela janela; o sol os frita ao amanhecer), não fogo
  direto de Charles. Registrado em `capitulos/capitulo-07.md`.
- **Neófitos vs. Lordes Defuntos (canon implícito)**: os mortos da torre
  são "neófitos, recém-amaldiçoados ou simpatizantes" (fala do jardineiro,
  cap. 10) — **não** os verdadeiros Lordes Defuntos (veteranos da era de
  ouro de Gondor). A "Comunidade" sobrevive ("Eles não estão acabados",
  Decian, cap. 10). Base para a facção vampírica do L2 (Hoste de Hícse,
  "vampiros (a confirmar)").
- **Arquivos**: `conceitos/terbs.md`, `conceitos/glossario.md`,
  `capitulos/capitulo-07.md`, `capitulos/capitulo-10.md`, `log.md`.

## 2026-08-08 (canon — arquitetura híbrida do castelo + ativação dos rampillas por padrão de presa)

- **Arquitetura do castelo (canon)**: fortaleza híbrida de dois anéis —
  anel externo vegetal (paliçada/muralhas de tronco e resina, parte do
  jardim de Devour; portão de madeira com cravos de renanthao) + núcleo de
  pedra (torre, salão, calabouços). Cap. 0 ajustado (distinção visual),
  cap. 18 coerente (portão externo + portas internas). `lugares/castelo-devour.md`.
- **Ativação dos rampillas (canon)**: as plantas-espia detectam
  vibração/calor/sangue, mas os rampillas **só atacam padrão de presa**
  (quem foge, sangra, se move como caça). Quem vem em paz (nômades, Nolan
  com selo) passa. Kate desvia do padrão no cap. 0 (não corre, não sangra).
  Ajustes: cap. 0 (movimentação de Kate), cap. 17 (fala de Kate a Mário),
  cap. 18 (guardas não hesitam — autômatos aguardam comando de Devour).
- **Arquivos**: `Livro 1/{capitulo0,capitulo17,capitulo18}.md`,
  `conceitos/rampillas.md`, `lugares/castelo-devour.md`, `log.md`.

## 2026-08-08 (canon — filho de Devour morto por Kate vira dívida; confronto no cap. 17)

- **Cap. 0 (filiação explícita)**: o xamã que Kate mata é **filho de Devour**
  (linhagem d'Tirath) — dito de forma natural ("Meu pai" / "Seu pai... me
  deve entretenimento"), sem cliffhanger. Eco visual: olhos "carvão molhado"
  ligam à linhagem (e a Devour no cap. 17).
- **Cap. 17 (confronto)**: Devour sabe da clareira via plantas-espia
  (vibração/calor), confronta Kate no salão; ela confirma ("Ele me disse
  quem era. Não mudou nada."); Devour registra a dívida e não age.
- **Semente #14 (Dívida de Sangue)**: conta em aberto no L1 (Devour morre
  antes de cobrar); germinação L2 potencial via Ossan (irmão sobrevivente,
  asset de Nolan) ou peso moral de Kate. `temas/sementes.md`.
- **Arquivos**: `capitulos/capitulo-17.md`, `temas/sementes.md`, `log.md`.

## 2026-08-06 (arquitetura — separação de camadas: processo fora da bible)

- **Princípio**: Story Bible guarda fatos do mundo (canon); regras operacionais
  de ferramenta vivem nas skills/agentes. A regra de acentuação de tritongos é
  **processo** (workaround de TTS), então saiu de `conceitos/fonetica.md`.
- `conceitos/fonetica.md` → agora **só a tabela de pronúncia canônica dos nomes**;
  descrição/tags reajustadas (tool-agnostic).
- Fonte única da acentuação de tritongos: seção 3 da skill `preparar-audiochapter`
  (com aviso anti-duplicação). Agente e prompt atualizados para referenciar a
  skill, não o `fonetica.md`.
- `decisoes/regras-audiochapter-acentuacao-ditongos.md` → nota de separação.
- Caminho de saída corrigido também em `Livro/.github/prompts/audiochapter.prompt.md`
  → `Audiobook/Capítulo {número}/`.

## 2026-08-06 (canon — acentuação fonética: APENAS tritongos; script cap. 19 regenerado)

- **Regra corrigida**: a acentuação fonética NÃO é mais aplicada a ditongos
  decrescentes (ai, ei, oi, au, eu, ou) — só a **tritongos** (três vogais na
  mesma sílaba tônica, ex.: alcateia → alcatéia). A acentuação excessiva de
  ditongos poluía o script.
- **Arquivos**: `Livro/.github/skills/preparar-audiochapter/SKILL.md`,
  `conceitos/fonetica.md`, `decisoes/regras-audiochapter-acentuacao-ditongos.md`,
  `Livro/.github/agents/preparador-audio.agent.md`, `index.md`.
- **Script cap. 19 regenerado**: `Audiobook/Capítulo 19/narracao-minimax.txt`
  — acentos de ditongo revertidos; só nomes fonéticos (Lêikand, Devôr,
  Dagmár, Cressadár, rampíla) e remoção de hífens. Sem tritongos no texto,
  nenhuma acentuação da etapa 3 aplicada.
- **Caminho de saída corrigido** nos docs: `Audiobook/Capítulo {número}/`
  (antes: `Audiobook/O Estrangeiro e a Metrópole/`, desatualizado).

## 2026-08-06 (registro — pendências de publicação: cap. 3 áudio)

- Registrado em memória do repo (`/memories/repo/pendentes-publicacoes.md`):
  cap. 3 (publicado) com texto corrigido ("vembra") e **áudio pendente**
  (regravar a linha do chá, ainda diz "olmo"). Itens de 2026-08-01
  (caps. 12/19) marcados como "conferir áudio". Cap. 19 ainda não publicado.

## 2026-08-06 (canon — glossário: termo de produção "cairn")

- Verbete de produção no `conceitos/glossario.md`: "cairn" (taquigrafia de
  planejamento) → renderização em prosa "monte/marco de pedras". Regra: o
  estrangeirismo inglês nunca entra na prosa (POV ornickenho traduzido).

## 2026-08-06 (canon — semente "foram gente" + xamã Ossan, filho de Devour)

- **Semente #13 (Rampillas + Segregação)**: cada rampilla foi uma pessoa
  zumbificada; Nolan, idealizador da Segregação, comanda um exército de
  humanos zumbificados (eco temático). Plantio recomendado cap. 21 (via
  Ossan) ou cap. 25. Risco: não pregar. `temas/sementes.md`.
- **Xamã nomeado "Ossan" (Ossan d'Tirath, filho de Devour)**: ficha criada
  (`personagens/ossan.md`), index.md, esquema-l1 (cap. 21), rampillas.md e
  devour.md atualizados. Decisão de filiação: **alguns** xamãs eram filhos
  (linhagem d'Tirath monopolizava o ofício), não todos. Ossan = herdeiro
  despojado, asset de Nolan por sobrevivência.
- **Arquivos**: `temas/sementes.md`, `personagens/{ossan,devour}.md`,
  `temas/esquema-l1.md`, `conceitos/rampillas.md`, `index.md`.

## 2026-08-06 (canon — origem dos rampillas + xamãs de Devour)

- **Origem dos rampillas (canon)**: criados por **semente parasita no sistema
  nervoso de criaturas inteligentes** (tipicamente humanos) que as **zumbifica**
  — apagam-se consciência e vontade; sobra o autômato. Implicação moral: cada
  rampilla foi uma pessoa (Kate os matou nos caps. 0/19; Nolan agora os
  comanda). `conceitos/rampillas.md`, `personagens/devour.md`, glossario.
- **Xamãs da corte (canon)**: NÃO eram rampillas — xilomagos da corte de
  Devour (elite mística), conheciam o ritual da semente e a criação de itens
  encantados (manto de Tharin). Quase todos morrem no incêndio; **um
  sobrevive** e vira **asset de Nolan** (conhece o jardim/raiz-mestra) —
  cap. 21. Tensão: serviu a Devour, obedece a Nolan por sobrevivência.
  Nome/ficha pendentes.
- **Manto (precisão)**: "de origem rampilla" → "do domínio de Devour,
  criado por um xamã-xilomago (não rampilla)" — `decisoes/manto-xilomagia-tharin.md`.
- **Arquivos**: `conceitos/rampillas.md`, `personagens/devour.md`,
  `temas/esquema-l1.md` (cap. 21), `decisoes/manto-xilomagia-tharin.md`,
  `conceitos/glossario.md`.

## 2026-08-06 (canon — Nolan×Vonos, parteira-ama "Mira", leviantares; pendente: xamãs)

- **Nolan × Vonos travados como canon**: (a) ironia estrutural — Nolan, devoto
  de Vonos, trabalha contra o plano do deus (Mário como ferramenta do Estado
  vs. Mário como rei) sem perceber; (b) queda religiosa — o pacto com Terbs no
  fim do L1 é também o abandono do próprio deus. `personagens/nolan.md`,
  `temas/esquema-l1.md` (caps. 28 e Imagem Final).
- **Parteira-ama nomeada "Mira"**: ficha criada (`personagens/mira.md`),
  index.md e nolan.md atualizados; corrigido "olmo"→"vembra" que havia
  sobrado em `personagens/nolan.md` e `conceitos/rampillas.md`.
- **Leviantares (canon novo)**: criados pelos elohins a partir dos humanos
  moldados do material genético, para dar ordem a Ornick — por isso têm
  poderes de linha elemental; gnock = atrofia. `conceitos/cosmologia.md`.
- **Pendente (decisão do autor)**: os **xamãs** de Devour (um criou o manto de
  Tharin) — identidade (não rampillas? xilomagos da corte?) e destino (mortos
  no fogo? sobrevivente? fio para Kate/Nolan?).
- **Arquivos**: `personagens/{nolan,mira}.md`, `temas/esquema-l1.md`,
  `conceitos/{cosmologia,rampillas}.md`, `index.md`.

## 2026-08-06 (correção de canon — Nolan é devoto de Vonos, não ateu)

- **Correção**: Nolan NÃO é ateu — é **devoto de Vonos** (o deus da Verdade),
  de modo racional e institucional (crê como crê na lei: estrutura de ordem,
  não consolo; despreza a religiosidade popular/comercial). Reflete a cena do
  enterro de Dagmar: em vez de silêncio ateu, Nolan cumpre o **rito fúnebre
  de Vonos** — fórmula seca, trâmite, sem choro; o rito não consola (o Sinal
  falhou no prólogo).
- **Implicações (a explorar)**: (a) a devoção de Nolan colide com o plano de
  Vonos (Nolan quer Mário como ferramenta do Estado; Vonos quer Mário como
  rei) sem ele perceber; (b) o pacto com Terbs no fim do L1 é também um
  abandono do próprio deus.
- **Arquivos**: `temas/esquema-l1.md` (cap. 21), `personagens/nolan.md`,
  `personagens/dagmar.md`.

## 2026-08-06 (canon — "vembra" no lugar de "olmo" + flora de Ornick derivada da Terra)

- **Rename**: a planta abortiva agora é **vembra** (árvore nativa de Ornick,
  nome traduzido), substituindo "olmo" — o ulmeiro terrestre não é abortivo
  oral, e o nome fictício elimina o tropeço farmacológico sem puxar carga
  cultural (arruda) nem quebrar o mistério de Juleen. Aplicado em
  `Livro 1/capitulo3.md` (publicado), `personagens/dagmar.md`,
  `temas/esquema-l1.md` (parteira-ama), `temas/sementes.md` (#6).
- **Canon novo — flora derivada**: Ornick não é criação independente — os
  elohins transplantaram flora e fauna de origem terráquea após Babel.
  "Jardim-replicado": carvalhos/magnólias não são coincidência, são linhagem
  (bônus teológico: o Eu Sou vem reclamar a cópia). `conceitos/cosmologia.md`
  e `conceitos/glossario.md` (verbete "vembra").
- **Arquivos**: `Livro 1/capitulo3.md`, `personagens/dagmar.md`,
  `temas/esquema-l1.md`, `temas/sementes.md`, `conceitos/cosmologia.md`,
  `conceitos/glossario.md`.

## 2026-08-06 (canon — cap. 21: enterro simbólico, parteira-ama, raiz-mestra)

- **Enterro simbólico de Dagmar (cap. 21, POV Nolan)**: o incêndio de Lakand
  é a pira involuntária (corpo irrecuperável sob o colapso da torre). Nolan
  arranca o anel de prata do dedo morto e o deposita num **cairn de pedras
  enegrecidas** na borda da clareira — rito mudo, sem reza, sem catarse.
  Semente L2: o anel é a única herança da mãe para Saboc. `temas/esquema-l1.md`
  (cap. 21), `personagens/dagmar.md`, `personagens/nolan.md`.
- **Parteira-ama (nova, nome provisório "Mira" — confirmar)**: uma das
  parteiras do quarto do parto (cap. 18) sobrevive e vira ama de leite de
  Saboc. Testemunha silenciosa da ressurreição. Filho morto dela = só fundo.
- **Semente do veneno corrigida**: o "rampilla esperto" era contradição de
  canon (autômatos sem consciência individual — `conceitos/rampillas.md`).
  Substituído pela **parteira-ama**, que conhece ervas e reconhece o cheiro
  de olmo em Dagmar; Nolan anota mentalmente (reveal de Juleen no cap. 30).
- **Raiz-mestra em dois tempos**: observação dos rampillas congelando na fuga
  - descoberta da raiz na vistoria pós-incêndio (o fogo expôs o jardim
    secreto). Ironia: o fogo de Lakand entrega a Nolan o controle.
- **Arquivos**: `temas/esquema-l1.md`, `temas/sementes.md` (#6/#7),
  `conceitos/rampillas.md`, `personagens/{nolan,dagmar}.md`.

## 2026-08-06 (canon — ficha do Milagre + consulta teológica)

- **Criação**: `conceitos/milagre.md` — milagre como irrupção do Criador
  acima do Limbo (quebra de classe: elohim rearranjam, só o Eu Sou cria).
  Consulta ao Consultor Teológico com briefing da teologia do Conselho
  Divino (Heiser, Dt 32:8-9 / Sl 82) para calibrar a análise.
- **Pontos travados**:
  - A oração é **ocasião/testemunho, não gatilho** — causa, ocasião e sinal
    separados; o milagre excede o pedido (pede-se misericórdia, chega vida).
  - "Acima do Limbo" é **ontológico**, não posicional (Criador vs. criatura).
  - Custo é **testemunho, não pagamento**: "ela morre, e apesar disso o bebê
    vive" (não "ela morre para que o bebê viva"). Refinada a redação em
    `personagens/dagmar.md`.
  - "Milagre" é palavra de narrador/leitor; ornickenhos não têm vocábulo.
  - Milagre é **evento, não categoria** — irreprodutível, sem mecânica.
- **Reconciliação cosmológica**: "Javé não atua diretamente em Ornick"
  precisado como "não governa pelo sistema delegado, mas age (exceção
  soberana)" — `conceitos/cosmologia.md`.
- **Arquivos**: `conceitos/milagre.md` (novo), `conceitos/cosmologia.md`,
  `personagens/dagmar.md`, `index.md`.

## 2026-08-06 (INGEST — sincronização do cap. 19 com o texto final)

- **Correções de texto (cap. 19 publicado)**:
  - Estalagem do Vau **removida** — Mathias NÃO cita "trouxe alguém de
    volta" nem implora a Mário; é Mário quem inicia ("O que aconteceu com o
    bebê?" / "Traga ele aqui." / "Traga. Por favor."). Mathias obedece em
    silêncio.
  - Citações de Mário atualizadas ("Deixem ele perto de mim" → "Traga ele
    aqui.") em `capitulos/capitulo-19.md` e `personagens/mario.md`.
  - **Nolan** adicionado aos personagens do cap. 19 (fora de cena —
    segurando a mão de Dagmar) em `capitulos/capitulo-19.md`,
    `personagens/nolan.md` e `visuais/nolan.md`.
  - Kate: flashback da mãe parteira ("Você precisa saber, Kate...") +
    callback Cressadar (selos e casas da corte) registrados em
    `capitulos/capitulo-19.md` e `personagens/kate.md`.
- **Visuais**: entradas do cap. 19 criadas para Kate, Mário, Lakand, Mathias,
  Nolan (não aparece), Dagmar (pós-morte) e Devour (morte fora de cena).
- **Lugares**: `lugares/saramant.md` — incêndio florestal do cap. 19
  (ateado por Lakand, custo do faro, rampillas sobreviventes).
- **Conceitos**: `conceitos/daerunmeges.md` — `ultimo_capitulo: 19`.
- **LINT — verificações abertas**:
  - **Corpo de Dagmar**: deixado no andar de cima quando o castelo queima
    ("gelando no andar de cima"). A nota antiga de distribuição ("o comboio
    volta com o corpo de Dagmar") NÃO é confirmada pelo texto final —
    enterro em aberto (verificar cap. 21/22).
  - `personagens/nolan.md` não tinha entradas dos caps. 17-18 (adicionada a
    de 18-19; confirmar que os resumos dos capítulos cobrem as lacunas).
  - Proposta: criar `conceitos/milagre.md` (referenciado em capitulo-19.md,
    ainda sem ficha) — aguardando autorização.
- **Arquivos**: `capitulos/capitulo-19.md`, `personagens/{mario,kate,nolan,
dagmar,mathias}.md`, `visuais/{kate,mario,lakand,mathias,nolan,dagmar,
devour}.md`, `lugares/saramant.md`, `conceitos/daerunmeges.md`, `index.md`.

## 2026-08-04 (coerência — Lakand × Mário)

- **Lakand NÃO culpa Mário pela dizimação da alcateia** — se carregasse
  culpa/rivalidade, repetiria o arco de Decian (cap. 16). Luto silencioso,
  sem alvo, nunca nomeado.
- **Logística fechada**: Lakand não estava com a alcateia perseguidora
  (batedor em serviço). Foi ao encontro dela, encontrou o massacre (cap.
  15), rastreou Kate até Devour (cap. 17: sangue do ombro, marcas, cheiro
  de rampilla; rumor do cap. 16 converge). Esperou a janela (parto + fogo).
  Texto mantém o POV sem explicar ("Era suficiente") — canon só de apoio.
- **Arquivos**: `personagens/lakand.md` (nota de coerência),
  `capitulos/capitulo-19.md` (INGEST).

## 2026-08-04 (canon — forma daërunmege de Lakand + cena da confissão)

- **Decisão 2 (desmanche no calabouço)**: Lakand chega à cela em forma
  híbrida (fera); o homem volta quando ele diz "— Kate." (nome = primeiro
  som humano). Quieto, rápido — não compete com a ressurreição. Validado
  pelo Guardião (gatilho mais coerente = ele dizer o nome; o "franziu a
  testa" publicado já é micro-desmanche). Exige revisar a chegada no cap. 19
  publicado (1-2 parágrafos).
- **Decisão 3 (forma plena no cap. 20)**: 1ª aparição de Lakand em lobo
  pleno — carrega Mário pela floresta em chamas; vista pelo POV febril de
  Mário (impressionista). Coerente (Mário viu lobo pleno de Charles, cap. 7).
- **Decisão 4 (plantas-espia)**: confirmada — sentem vibração/calor, NÃO
  odor (devour.md); calor-ofusca-plantas + odor-ofusca-Lakand. Já era canon.
- **Regra "forma plena não fala" (decisão 1)**: **TRAVADA (2026-08-04).**
  Validada pelo Guardião (cap. 10: revertem à forma humana para conversar;
  cap. 15: híbrida fala, plena não). Registrada na taxonomia de
  `conceitos/daerunmeges.md`.
- **Confissão (cap. 24, POV Kate)**: colocação fechada — quietude antes da
  declaração "Ele é a chave... eu lidero" (alimenta-a causalmente). Foco na
  DEVASTAÇÃO, não no amor (já percebido no cap. 19). Fissura corporal:
  formigamento nas mãos (callback semente #11) como reflexo do desejo
  enterrado, NÃO paixão por Lakand. Dívida em aberto no L1.
- **Arquivos**: `conceitos/daerunmeges.md` (taxonomia de formas),
  `personagens/lakand.md`, `capitulos/capitulo-19.md` (INGEST),
  `temas/sementes.md` #12, `temas/esquema-l1.md` (cap. 24).

## 2026-08-03 (canon — incêndio do Castelo de Devour, cap. 19)

- **Decisão A (autoria do fogo)**: Lakand **ateou o fogo de propósito** —
  sozinho não vence os rampillas em combate; incendeia a toca (resina =
  combustível) e o castelo (tochas de óleo do salão) como ato **instintivo de
  desespero**. O caos cobre a libertação de Kate.
- **Decisão B (morte de Devour — híbrido)**: Lakand o **fere no salão** (o
  sangue nas mãos permanece canônico, preservando "matou um rei" e "mãos
  manchadas de sangue fresco"); o fogo **consome o corpo**. Fora de cena, só
  subtexto.
- **Decisão C (fogo descontrolado)**: vira incêndio florestal em Saramant
  (outono seco) — tensão na fuga; faro de Lakand inutilizado pela fumaça.
- **Decisão D (rampillas — opção a)**: ~uma dezena sobrevive (patrulhas de
  perímetro + toca secundária na borda de Saramant); inertes com a morte de
  Devour. Nolan os reúne via **raiz-mestra subterrânea** (sobrevive ao fogo;
  raiz profunda rebrota após fogo). Castelo de pedra chamuscado = base militar.
  Opção (b) "nenhum" rejeitada (quebraria o L2).
- **Decisão E (Mathias — poder de fogo)**: ficha criada
  (`personagens/mathias.md`). Fogo nas armas = treino padrão dos Espadas da
  Lei (origem na linhagem militar Addorbek); na fuga, contra-fogo/firebreak +
  escudo de calor, com **limite estrito** (não apaga, não domina fumaça,
  alcance curto, exaustão/queimaduras). Cena no **cold-open do cap. 21**
  (POV Nolan).
- **Arquivos atualizados**: `personagens/{devour,lakand,mathias}.md` (mathias
  = novo), `conceitos/rampillas.md` (fogo + toca secundária, `ultimo_capitulo`
  19), `insights/nolan-controla-rampillas.md` (raiz-mestra decidida),
  `temas/sementes.md` #7, `temas/esquema-l1.md` (caps. 20-21),
  `lugares/castelo-devour.md` (pós-incêndio), `capitulos/capitulo-19.md`
  (INGEST), `index.md` (Mathias).

## 2026-08-01 (canon — mecânica da Voz)

- **Correção de canon**: a Voz NÃO possuí Mário pontualmente. No cap. 12 ela
  o **capacitou permanentemente** a falar ornickenho (dom de falar, além do
  dom de entender do cap. 4). Mário é fluente, sem sotaque, desde então.
- **Correção aplicada**: `Livro 1/capitulo12.md` — possessão momentânea
  reescrita como capacitação (primeira frase perfeita = momento do dom).
- **Correção aplicada**: `Livro 1/capitulo19.md` — removido trecho do
  "sotaque que ele nunca perdia" (contradizia o canon); adicionada nota de
  publicação (Substack já publicado — corrigir).
- **Criação**: `insights/a-voz-capacita-nao-possui.md` — canon completo.
- **Atualização**: `personagens/mario.md` — seção "Mecânica da Voz — Dons de
  Línguas" + crise do cap. 20 ("falo sem ter aprendido").
- **Correção de POV (canon)**: "dom" é linguagem do narrador/leitor; Mário
  NÃO atribui identidade divina à Voz — lê a capacitação como delírio que se
  instalou na língua. Cap. 12 e ficha atualizados.
- **Correção de POV (canon)**: Mário não conhece o termo "ornickenho" — usa
  "a língua deles". "Ornickenho" só em POV/fala de nativos. Cap. 12 corrigido;
  regra registrada na ficha de Mário.

## 2026-08-01 (correção de canon — relação Kate × Nolan)

- **Correção de canon**: Kate **NÃO serve a Nolan**. Ela foi treinada por
  Gaviorn'l e Cressadar como "arma definitiva de Terbs" para atacar a
  Metrópole (cap. 5) e depois descartada. Corrigidos:
  - `Livro 1/capitulo19.md` — âncora do brasão: "Cressadar lhe ensinara os
    selos e as casas da corte para o ataque que fora deixado de lado"
    (em vez de "servira sob aquela ordem")
  - `personagens/kate.md` — Personalidade, Papel na História e Relações
    (Nolan = estranho/independente; Gaviorn'l = mentor; Benjamim = clérigo
    ativo de Terbs)
- **Consequência**: Nolan vê Kate como "a caçadora sem lealdade" (cap. 18) —
  corretamente, pois ela nunca foi leal a ele.

## 2026-08-01 (correção de canon)

- **Correção de canon**: NÃO existe "mãe de criação" de Kate. A mãe era
  **parteira**; Kate a chama de "escrava" (cap. 8) e "vagabunda" (cap. 5)
  como julgamento do ofício, não como fato. Corrigidos:
  - `Livro 1/capitulo11.md` — "sua antiga mãe de criação" → "sua mãe"
  - `Livro 1/capitulo19.md` — "Sua mãe de criação a levava" → "Sua mãe"
  - `personagens/kate.md` — motivação profunda enriquecida (ódio pelo ofício
    de parteira = rejeição da vida servil da mãe)
- **Consequência para a semente #11**: o ódio pela mãe parteira é a segunda
  raiz do desejo enterrado de Kate. No L2, aceitar filhos de Mário implica
  transcender o desprezo de classe pela mãe.

## 2026-08-01

- **Semente**: Desejo enterrado de Kate por filhos — registrada em
  `temas/sementes.md` (#11) e na ficha `personagens/kate.md`. Plantio no
  cap. 8 (formigamento nas mãos), reforço contextual no cap. 19, germinação
  no L2 (Kate aceita ter filhos de Mário — abandono da violência como motor
  de salvação).

## 2026-07-31 (2ª operação)

- **Decisão**: Glossolalia invertida — Mário ora "Eu Sou" em ornickenho no
  cap. 19 (`decisoes/glossolalia-invertida-oracao-cap19.md`). Texto canônico
  da oração definido com apoio do Consultor Teológico.
- **Criação**: Insight "Eu Sou" — nome de Deus em Ornick
  (`insights/eu-sou-nome-de-deus.md`). "Javé" reservado para revelação futura.
- **Decisão de arco**: Efeito sanfona — Mário lembra de orar mas deixa de
  orar (cessacionismo teimoso); a Voz confronta Mário e assume a autoria da
  glossolalia (a escrever).
- **Atualização**: `capitulos/capitulo-19.md` — adicionadas sementes 6 e 7
  (glossolalia; Mathias→Nolan) e o momento da oração no resumo.
- **Atualização**: `temas/sementes.md` — nova semente #10 (glossolalia).
- **Atualização**: `personagens/mario.md` — (ver seção cap. 19).

## 2026-07-31

- **Criação**: INGEST do Capítulo 19 — O Bebê (`capitulos/capitulo-19.md`).
  Break Into 2 (~38-40%), POV Kate. Milagre do bebê, escolha de Kate,
  fuga com Lakand.
- **Decisão**: Chekhov's Gun do manto de xilomagia de Tharin — Opção 1,
  Kate recupera no cap. 20 (`decisoes/manto-xilomagia-tharin.md`).
  Geografia validada: cabana ~3 km de Devour, no caminho da fuga.
- **Decisão (revisão)**: Morte de Devour por Lakand — subtexto, nunca
  anunciada em diálogo (reduz competição de clímax). Âncora da entrada de
  Lakand no caos ("Ela não perguntou como ele entrara").
- **Atualização**: `personagens/devour.md` — morte por Lakand (não por
  ordem de Nolan); nota de coerência.
- **Atualização**: `personagens/lakand.md` — cap. 19 (mata Devour, guia a
  fuga, semente "eu perdi").
- **Atualização**: `personagens/kate.md` — cap. 19 (testemunha o milagre,
  Mário vira arma).
- **Atualização**: `personagens/mario.md` — cap. 19 (Voz age através dele,
  ressuscita o bebê).
- **Atualização**: `temas/sementes.md` — nova semente #9 (manto de xilomagia).

## 2026-07-27

- **Decisão**: Regras de acentuação fonética (tritongos/ditongos decrescentes) e extração rigorosa de narração para Minimax — registrada em `decisoes/regras-audiochapter-acentuacao-ditongos.md`.
- **Atualização**: `Livro/.github/skills/preparar-audiochapter/SKILL.md` — reescrita completa: extração de narração com tabela de casos, acentuação de tritongos/ditongos decrescentes, regras de hífen, tags de tempo.
- **Atualização**: `conceitos/fonetica.md` — adicionada seção "Acentuação Fonética de Tritongos e Ditongos Decrescentes" com tabela de substituição e regras de ouro.
- **Criação**: `Livro/.github/agents/preparador-audio.agent.md` — agente especializado para pipeline de áudio Minimax.
- **Atualização**: `Livro/.github/prompts/audiochapter.prompt.md` — referência atualizada para a skill e regras fonéticas.

## 2026-07-26

- **Insight**: Recompensa de Genocydo atrai mercenários — registrado em `insights/recompensa-genocydo-atrai-mercenarios.md`. Justificativa para mercenários na Estalagem do Vau (cap. 18).
- **Criação**: Ficha de [Alavria](lugares/alavria.md) — nação estrangeira, patrono Renath, colonizada por nação do Sucontinente. Invade a Metrópole no final do L1.
- **Criação**: Ficha de [Renath](conceitos/renath.md) — elohim patrono de Alavria, servo comissionado de Marduk. Agenda imperial (anexar o Reino de Genocydo).
- **Criação**: Insight [Nolan controla rampillas](insights/nolan-controla-rampillas.md) — após morte de Devour, Nolan descobre mecanismo de controle dos autômatos.
- **Atualização**: `conceitos/glossario.md` — adicionado verbete "Alavria"; rampillas atualizados como autômatos sem emoção própria.
- **Atualização**: `personagens/devour.md` — adicionada seção "Natureza dos Rampillas" (autômatos) e "Pós-Morte" (Nolan assume controle).
- **Atualização**: `personagens/koda.md` — adicionada seção "Alavria" com detalhes sobre Renath, Sucontinente e refém Joachin.
- **Atualização**: `temas/sementes.md` — adicionada semente #7: Nolan e o Controle dos Rampillas (plantio no L1, germinação no L2).
- **Atualização**: `index.md` — adicionados links para Alavria e Renath.

## 2026-07-24

- **Inicialização**: Repositório criado na branch `feat/llm-wiki`.
- **Estrutura**: Diretórios do bundle OKF v0.1 criados.
- **Configuração**: AGENTS.md, protocolo-ingest.md, copilot-instructions.md criados.
- **Ingestão**: Fichas de 8 personagens convertidas para formato OKF.
- **Ingestão**: Capítulo 0 — Prólogo ingerido. Resumo em capitulos/capitulo-00.md.
  Personagens atualizados: Nolan, Kate, Genocydo, Benjamim.
  Visuais atualizados: Nolan, Kate, Genocydo, Benjamim.
- **LINT**: Contradição (Nolan × óculos) resolvida — ficha canônica corrigida,
  Nolan usa óculos (canônico).
- **Ingestão**: Material do `.github/storybible/` ingerido. Novos conceitos:
  cosmologia, Marduk, Vonos, Terbs, Hícse, Sinal, Segregação, Glossário.
  Novo tema: Tom e Voz Narrativa.
- **Ingestão**: Personagens secundários — Devour, Koda, Charles, Decian,
  Gaviorn'l, Gunad, Lupe'i, Nuh d'Teraghar, Valinor.
- **Ingestão**: Temas — Timeline de Ornick, Mapa de Sementes Cross-Livro.
- **Ingestão**: Lote final — Arcos por Livro, Esquema do L2, Riscos Estruturais,
  Dicionário Fonético. Todo o material do `.github/storybible/` foi ingerido.
- **Ingestão**: Capítulo 1 — O Sonho ingerido. Resumo em capitulos/capitulo-01.md.
  Personagem atualizado: Mário (primeiro teste de fé: falha).
  Visuals atualizados: Mário (óculos confirmado, sangue nas mãos).
  Semente: Vicent Tanässer (morto no sonho).
- **Ingestão**: Capítulo 2 — A Travessia ingerido.
- **Ingestão**: Capítulo 3 — A Conspiração ingerido. Resumo em capitulos/capitulo-03.md.
  Personagens atualizados: Nolan (arquiteto da Segregação, conspira com Koda),
  Dagmar (chá de olmo), Koda (primeira abordagem a Nolan).
  Visuals atualizados: Nolan (cinzas, óculos, sorriso).
  Conceito atualizado: Segregação (autoria de Nolan).
  Semente: chá de cascas de olmo (Juleen) — **causa** da morte de Dagmar.
- **Ingestão**: Capítulo 4 — Opium ingerido. Resumo em capitulos/capitulo-04.md.
  Personagem atualizado: Mário (curado, tradução automática, capturado).
  Visuals atualizados: Mário (trapos, pés descalços, duas luas).
  Sementes: Mesmia (1º altar), Opium (chacina), tradução automática.
- **Ingestão**: Capítulo 5 — A Selvagem ingerido. Resumo em capitulos/capitulo-05.md.
  Personagens atualizados: Kate (arma de Terbs, frustração), Gaviorn'l (aviso do Rohdis).
  Visuals atualizados: Kate (saia de couro, suor).
- **Ingestão**: Capítulo 6 — O Jogo ingerido. Resumo em capitulos/capitulo-06.md.
  Personagens atualizados: Nolan (leu Llyfr, falhou com Genocydo), Genocydo (recusa).
  Visuals atualizados: Nolan (xadrez, casa de Koda).
  Sementes: luas azuis (Tristan e Nevëilla), Nolan leu Llyfr original.
- **Ingestão**: Capítulo 7 — Os Lordes Defuntos ingerido. Resumo em capitulos/capitulo-07.md.
  Personagens atualizados: Mário (apunhalado, testemunha transformação), Charles (revelação).
  Visuals atualizados: Mário (ferimento no ombro, sangue).
- **Ingestão**: Capítulo 8 — A Caverna ingerido. Resumo em capitulos/capitulo-08.md.
  Personagens atualizados: Kate (frustração, Charles), Lakand (revelação).
  Visuals atualizados: Kate (caverna, farrapos).
- **Ingestão**: Capítulo 9 — O Diário Perdido ingerido.
  Personagens atualizados: Nolan (Bíblia de Kraviam), Layla (infiltrada, falha).
  Visuals atualizados: Nolan (jantar, jardins).
- **Ingestão**: Capítulo 10 — A Carga ingerido.
  Personagens atualizados: Mário (carga, curado), Charles (revelado), Decian (hesitação).
  Visuals atualizados: Mário (sapatos de morto, atadura).
- **Ingestão**: Capítulo 11 — Os Nômades ingerido.
  Personagens atualizados: Kate (Theodore, nômades, Estruzzo).
  Visuals atualizados: Kate (adagas, sangue de Estruzzo).
- **Ingestão**: Capítulo 12 — A Jaula ingerido.
  Personagens atualizados: Mário (fala ornickenho), Lakand (primeiro diálogo), Decian (cuidado).
  Visuals atualizados: Mário (jaula, fogueiras).
- **Ingestão**: Capítulo 13 — A Sala Secreta ingerido.
  Personagens atualizados: Nolan (a razão não basta), Nuh (apoteose), Valinor (recusa), Lupe'i (informante).
  Visuals atualizados: Nolan (sala secreta, candelabro).
- **Ingestão**: Capítulo 14 — O Encontro ingerido.
  Personagens atualizados: Kate (Mário surge, uivo de guerra).
  Visuals atualizados: Kate (vigília, clareira noturna).
- **Ingestão**: Capítulo 15 — A Queda ingerido.
  Personagens atualizados: Mário (culpa, capturado), Kate (mata lobisomem, captura Mário).
  Visuals atualizados: Mário (culpa, pulsos amarrados), Kate (sangue, corda).
  Tae-Tabor morto.
- **Ingestão**: Capítulo 16 — A Travessia ingerido.
- **Ingestão**: Capítulo 17 — Devour ingerido.
  Personagens atualizados: Kate (costelas quebradas, 1º diálogo), Devour (intimação).
  Visuals atualizados: Kate (cela, desarmada).
  Inquiridores: intimação enviada a Devour.
  Visuals atualizados: Mário (trapos, pés descalços, duas luas).
  Sementes: Mesmia (1º altar), Opium (chacina), tradução automática.
