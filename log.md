# Log de Atualizações

## 2026-09-18 (checkpoint de beat — fecho do bloco "Jogos e Diversão", caps. 21-28)

- **Anti-slop em lote** nos 8 capítulos fechados (21-28): **153 mudanças em
  120 linhas**, medido por `git diff --word-diff` (o "85" do relatório inicial
  dos agentes era contagem agrupada e **não se reproduz**); ~**794 palavras**
  cortadas (20.129 → 19.335, contagem oficial nos arquivos — a soma por
  capítulo pelo diff dá −798, diferença de ±4 por tokenização). Por capítulo
  (mudanças/linhas/palavras finais): 21 14/12/2.263 · 22 6/5/2.486 · 23
  38/27/2.397 · 24 26/24/2.266 · 25 21/13/2.226 · 26 36/30/3.162 · 27
  8/6/2.199 · 28 4/3/2.336. **Os dois mais contaminados são o 26** (maior
  perda: −222 palavras) **e o 23** (maior número de intervenções: 38, e −215
  palavras) — a formulação "o 26 foi o mais contaminado" era imprecisa.
  Muleta dominante do bloco: a construção **"como quem..."** (11 cortadas
  aqui, 17 sobraram → passe curto em 2026-09-18, bullet abaixo). Verificação
  mecânica: zero `*`, zero marcadores `(* ...)`, zero `---` nos 8 arquivos.
  Lista completa das 153 mudanças: relatório `anti-slop-21-28-revisao.md`
  (workspace da sessão, não versionado) ou `git diff bd6af8a^ bd6af8a` no
  repo do livro.
- **Passe curto "como quem..." (2026-09-18, mesmo checkpoint)**: das 17
  ocorrências remanescentes, **15 cortadas** e **2 mantidas com motivo** —
  `capitulo21.md:105` (a fórmula fica: caracteriza palavras decoradas e fora
  do controle de Mário, e ficou única depois que o par duplicado do cap. 23
  saiu) e `capitulo27.md:61` ("como quem puxa água de um poço": a imagem do
  puxão de poço não tem substituto sem perder a metáfora). Duas cirurgias
  resolveram defeito junto: `capitulo22.md:89` ("como quem inventaria" →
  "inventariando" — o verbo era *inventariar*, não *inventar*) e
  `capitulo23.md:47` (`Ela falava como quem recita um mapa.` → `A voz dela era
  mapa.`, que preserva o eco com `capitulo23.md:71`, "a voz não era mapa, era
  negociação"). **−25 palavras** no bloco (21 −3 · 22 −10 · 23 −4 · 25 −2 ·
  26 −3 · 27 −3); zero Markdown/travessão introduzido; zero `(* ...)` tocado.
  **Saldo da muleta no livro inteiro: 21** — as 2 mantidas acima + **19 fora
  do bloco** (caps. 0-20; concentração no **cap. 18 = 5** e cap. 15 = 3) →
  candidato a passe próprio, de preferência no congelamento.
- **⏳ Decisão pendente do autor (`capitulo23.md:47`)**: a linha ficou `A voz
  dela era mapa.`; se o autor preferir o verbo de fala explícito, alternativas
  são `Ela falava o mapa de cor.` ou o corte seco do beat.
- **Régua de % remedida**: coluna **Palavras** conferida arquivo por arquivo;
  coluna **% Real** recalculada (na ocasião, acumulado ÷ 115.000). Cinco
  linhas antigas estavam defasadas (caps. **5, 13, 16, 18 e 20**) e foram
  corrigidas; as linhas 21-28 já estavam certas. A hipótese de "drift uniforme
  ÷100.678" foi descartada (essa divisão não existe em nenhum arquivo). Cap.
  28: **2.336 palavras** após o anti-slop (o INGEST do capítulo registrou
  2.352 — medição anterior às cirurgias). Coluna **% Plan** segue parada em
  "~38-40%" do cap. 20 em diante — realinhar no congelamento.
- **Régua de % ADOTADA (2026-09-18, decisão do autor)**: a coluna **% Real**
  passou a ser **acumulado real ÷ 137.500** — a régua de *planejamento*
  (rebaseline de 2026-09-12), no lugar do denominador nominal de 115.000, que
  **inflava a posição em ~10 pontos**. Denominador refeito nas linhas 0-28 do
  `esquema-l1.md` (cabeçalho e nota de réguas atualizados) e linha obsoleta do
  `temas/arco-stc.md` corrigida. Efeito imediato: o cap. 28 sai de "~64,6%"
  para **~54,0%**. Motivo: as bandas do STC (Jogos até ~68%, Ponto Central no
  cap. 36 com ≈91.800-95.200 palavras acumuladas) só fecham nesta régua — a
  régua velha criava pressão para apressar os caps. 29-35.
- **Margem de palavras conferida**: acumulado até o cap. 28 = **74.301**
  palavras. Para o cap. 36 chegar em ~94.000, faltam ~19.700 em 8 capítulos =
  **~2.460/capítulo**; a média real do bloco 21-28 foi 2.417/capítulo →
  **no ritmo, sem necessidade de compressão nem folga para esticar**.
- **Passe de fechos — régua do autor gravada (2026-09-18)**: as quatro
  definições de corte (A/B/C/D: intenção, quando usar, risco) e o **checklist
  de 3 perguntas** foram gravados em `.github/prompts/passe-fechos.prompt.md`
  (repo do livro), com uma **emenda**: a pergunta 2 ("mudou de POV? favoreça
  A/B") não vale automaticamente neste livro, onde o POV gira em quase todo
  capítulo — vale como **escalada** (favorece A/B só quando o capítulo que sai
  deixa perigo ou dilema em aberto). O material **confirma** o mapa do bloco
  21-28 (A=2, B=0, C=2, D=4) e **dá nome ao zero B**: B é o corte da pergunta
  "quem o personagem vai escolher ser" — sem decisão em cena, não existe B
  (mesmo ferimento do risco estrutural #1). Registrado também o **risco do
  Corte C**: no instante do corte, a consequência tem de ser simples e
  visível.
- **Candidato a Corte B no cap. 31** (marca gravada no `esquema-l1.md`): a
  fissura de Kate comporta B se o fecho cortar **na pergunta** (ela vai
  admitir?), em vez de depois do pensamento abafado (D). É troca do ponto de
  corte, não reescrita — decisão do autor pendente. A marca do **Corte C no
  cap. 29** ganhou a exigência acima.
- **Passe de fechos** (3ª parte do checkpoint): mapa dos caps. 21-28 —
  C-D-D-D-C-A-A-D (**A=2, B=0, C=2, D=4**). Alertas registrados: freada de
  três D seguidos (22-23-24); 25 fecha sem gancho; **zero cortes B** no bloco;
  "norte" sela os fechos de 22, 23, 24 e 26; "E" arremata 21, 24, 26 e 27;
  **Mário reativo em 26-28** (risco estrutural #1) → decisão devolvida a ele
  no cap. 30 e no cap. 33. Regra de fecho para 29-35 gravada no esquema (fora
  do fecho: "norte", "escuro", "silêncio"; não abrir o fecho com "E").
- **Mapa corrigido para frente** (`temas/esquema-l1.md`): nota de réguas no
  topo; linhas 5-20 da tabela; notas do Movimento 3; marcas de abertura/corte
  nos blocos dos caps. 29, 30, 31, 33 e 36 (beat "Kate mede ferramentas"
  realocado ao 36); semente #20 (trono) acrescentada à linha dos Inquiridores;
  arco de Kate e Lakand atualizados.
- **Ponteiros corrigidos**: `capitulos/capitulo-26.md` (a rebelião consolida
  no **cap. 31**, não em "29+"); `capitulos/capitulo-25.md` (beat pendente
  resolvido: realocado ao **cap. 36**); `temas/sementes.md` (#4 Layla — o cap.
  23 não tem menção, o fio passa pelo 24 e pelo 29; numeração nova a partir de
  **#21**, com Etemenanki = #21).
- **Fila para o congelamento**: 17 pontos de polimento linguístico anotados,
  respiro do cap. 26 (o concentrador do bloco: 3.162 palavras, 7 eventos, 6
  sementes) e endurecimento da coluna Nolan (os caps. 22, 24 e 29 usam o mesmo
  molde "chegar-examinar-decidir").
- **Payoffs do bloco**: todos entregues; a semente do trono foi executada um
  capítulo antes do previsto (28, em vez de 29).

## 2026-09-18 (canon 3 — Mini-INGEST do cap. 28: "Não Apodreceu"; janela de checkpoint do bloco Jogos)

- **Capítulo fechado**: `Livro 1/capitulo28.md` (POV Kate, beat Jogos e
  Diversão, **~64,5%** do L1, **2.352 palavras**). Sem marcadores `(* ...)`
  restantes. **Título "Não Apodreceu"** proposto no INGEST — vetável pelo
  autor.
- **Canon novo (cap. 28)**:
  (1) **Vara de Ofício — alcance, não intensidade**: o fuste graduado mede
  **até onde o som chega**; cravar fundo **encurta** o raio (regra fixada com
  o autor). O som derruba quem está de joelhos ou deitado; não derruba quem
  tem preparação.
  (2) **Timbre irmão**: o som da vara e o tom do diapasão são **irmãos**
  (mesmo renanthao); só o treino separa os dois — Kate aprendeu no **Rohdis**
  (varas batidas no aço da armadura de Gaviorn'l).
  (3) **O fio não cobra a ferida de Kate** (semente #19, plantio executado no
  28, não no 29): corte no antebraço esquerdo, sangue e ardência, pele
  vermelha normal → o Inquiridor: "Não apodreceu... é uma gnock?".
  (4) **Registro acima da execução**: o escriba (sem manto escuro, colar de
  pedra azul, bolsa e rolo) não luta, escreve atrás e manda: **"Ela não
  apodrece. Precisamos enquadrá-la."** — Kate é caso a medir, não alvo a
  matar.
  (5) **Rotina das três caixas** na recolha (água da bacia métrica; Revólver
  de Auditoria; diapasão limpo com pano, na sequência, em silêncio de
  ritual) + os próprios mortos alinhados **pela cabeça**, sem pesar.
  (6) **Vocabulário de ofício**: "Em eixo." / "Falta assentar." (aferição,
  não acordo).
  (7) **Composição de patrulha**: 5 varas + 1 escriba.
  (8) **"Sua frequência é conhecida"** + **"Ele terá o trono. Vonos
  garante."** — a Ordem declara o objetivo de fundo e não recua (semente
  #20). O capítulo fecha **em Kate**, que guarda as palavras sem entendê-las.
- **Sementes**: #19 atualizada (plantio executado; correção da previsão que
  apontava o cap. 29) · **#20 nova** ("O Trono do Estrangeiro — a Ordem
  afirma") · #8 (Plantio 6, cap. 28) · #9 (primeiro uso do manto de xilomagia
  na prosa — a carga finita começa a queimar).
- **Visuais**: `visuais/kate.md`, `visuais/mario.md`, `visuais/lakand.md`
  (seção "## Capítulo 28 — Não Apodreceu"). Nolan não aparece no capítulo —
  `visuais/nolan.md` não foi tocado.
- **Fronteira 28→29**: o 27 fechava com as vozes do cerco morrendo uma a uma;
  o 28 abre exatamente nesse som (continuidade confirmada). Como o 27, o
  fecho do 28 é **misto** (fuga + informação), não desastre puro — o gancho
  do 29 é o terreno com os **corpos de Inquiridores** e **Mário fora de
  alcance**, com Nolan deduzindo "Não foi Kate. Foi Mário." O 28 mistura
  fuga e informação, e deixa em aberto para o passe de fechos o fato de Kate
  **não converter em decisão** o que ouviu (ela só guarda).
- **Desvios vs. o bloco do esquema** (mapa corrigido para frente, nunca o
  texto): (a) o capítulo **não termina no escriba** — fecha em Kate; (b) o
  beat "não é fardo" aterrissou na caverna e o "se jogou no chão" é narrado
  **fora do campo de visão** de Kate; (c) Kate mata **três** Inquiridores
  (por trás, jugular, estocada de baixo), não dois em corpo a corpo. Nota de
  execução registrada em `temas/esquema-l1.md` (bloco do cap. 28).
- **Passo 7 — contador de checkpoint**: bloco **Jogos e Diversão (caps.
  21-28) = 8 capítulos sem checkpoint** → **oferecido ao autor** (Arquiteto
  de Densidade leve nas fronteiras de beat + **anti-slop em lote** +
  **passe de fechos**). A janela já estava aberta desde 2026-09-11 para os
  caps. 21-27 (7 caps) e permanece pendente de decisão.
- **Arquivos**: `capitulos/capitulo-28.md` (novo),
  `conceitos/inquiridores-sinal.md` (seção "A patrulha em operação"),
  `personagens/inquiridor.md` (escribas, identificação, tabela de aparições),
  `conceitos/glossario.md` (Vara de Ofício; "Em eixo"/assentar),
  `temas/sementes.md` (#8, #9, #19, #20), `temas/esquema-l1.md` (tabela +
  nota de execução), `index.md` (caps. 27 e 28 repostos na sequência),
  `log.md`.

## 2026-09-18 (canon 2 — plant aplicado no cap. 24; carroça consertada em Tronk)

- **Decisões do autor (mesmo dia, complemento)**: (1) o veículo do retorno é a
  **carroça consertada** — e o conserto é **na Feira de Tronk** (carroceiros e
  forja; cruzamento da estrada da Mina com a **estrada para o sul**, o ponto
  onde a volta começa); (2) **plant aprovado e aplicado**.
- **Prosa alterada**: `Livro 1/capitulo24.md:53` — entrou "Era o que restara da
  carruagem que trouxera Dagmar da Metrópole: a caçamba, a capota comida pelo
  fogo." Uma frase; sem Markdown; sem travessão na narração.
- **Distâncias registradas**: Metrópole → castelo = 6 dias (cap. 19); o
  assentamento do cap. 24 a 3 dias ao norte de Saramant; Tronk a 2 dias do
  assentamento (cap. 23:165); **Tronk → Metrópole ≈ 11 dias**.
- **Arquivos**: `decisoes/carruagem-vira-carroca-cap24.md` (conserto em Tronk,
  distâncias, plant marcado como aplicado),
  `decisoes/nolan-retorna-metropole-juleen-rampillas.md`,
  `capitulos/capitulo-24.md`, `temas/esquema-l1.md`, `log.md`; prosa:
  `Livro 1/capitulo24.md`.

## 2026-09-18 (canon — a carruagem vira a carroça do cap. 24; Mira e Saboc retornam à Metrópole)

- **Pergunta do autor (2026-09-18)**: (1) a viagem de Nolan da Metrópole ao
  castelo de Devour é de carruagem? (2) Depois do incêndio, Mira volta com
  ele dentro da carruagem ou fica como está, na mula com Saboc no colo?
- **Verificado no texto**: carruagem **confirmada** nos caps. 17 e 19 (Dagmar
  dentro; cocheiro contratado na última hora; seis dias de viagem). Depois do
  incêndio (cap. 20) a carruagem **desaparece do texto**; o cap. 24 traz
  **carroça** de roda empenada e lona chamuscada, com Mira **na mula**. O
  séquito vai para o **norte** (cap. 22) — a "volta" só existe a partir do
  cap. 29 (planejado).
- **Decisões do autor**: (1) a carruagem **virou a carroça do cap. 24**
  (degradação pelo incêndio: capota comida pelo fogo, roda empenada, lona
  chamuscada); (2) Mira **fica na mula** na marcha ao norte; (3) Mira e Saboc
  **retornam com Nolan à Metrópole** (caps. 29-32) — o esquema já exigia
  Saboc fisicamente com Nolan (Noite Escura).
- **Novo arquivo**: `decisoes/carruagem-vira-carroca-cap24.md`.
- **Plant opcional na prosa** (não aplicado — aguarda o autor): uma cláusula
  ligando a carroça à carruagem — cap. 22 (vistoria: "contando perdas,
  medindo o que servia") ou cap. 24 (descrição do veículo).
- **Ponto aberto**: transporte do retorno à Metrópole — a carroça consertada
  (recomendado, sem objeto novo) ou veículo trazido da Metrópole por Mathias.
- **Pendente**: Mini-INGEST do **cap. 28** (escrito; `capitulos/` vai até o
  `capitulo-27.md`) — próximo capítulo só começa depois dele. **[FECHADO em
  2026-09-18: ver a entrada "canon 3" no topo — cap. 28 = "Não Apodreceu".]**
- **Arquivos**: `decisoes/carruagem-vira-carroca-cap24.md`,
  `decisoes/nolan-retorna-metropole-juleen-rampillas.md`,
  `capitulos/{capitulo-22,capitulo-24}.md`, `visuais/{nolan,mira}.md`,
  `personagens/{mira,dagmar}.md`, `temas/esquema-l1.md`, `log.md`.

## 2026-09-11 (protocolo — lente Scene/Sequel no F3 + gatilho do checkpoint)

- **F3 expandido** (`conceitos/checklist-capitulo.md`): Teste de Ação e
  Reação (Swain) agora cobre a anatomia completa — cena = objetivo → conflito
  → desastre; sequel = reação → dilema → decisão; "com que unidade o capítulo
  fecha?"; decisão adiada >2 caps vira dívida registrada. Princípio: **marca
  dívida, não defeito**.
- **Mini-INGEST passo 5** (`protocolo-ingest.md`): checagem de fronteira
  agora anota o fecho (decisão/desastre) e o que ele exige do próximo.
- **Mini-INGEST passo 7 (novo)**: contador de checkpoint — ≥6 caps desde o
  último checkpoint registrado → **oferecer ao autor** o checkpoint leve do
  Arquiteto. Lacuna fechada: a regra existia em três lugares, mas sem gatilho
  de disparo (nenhum checkpoint registrado até hoje).
- **Referências sincronizadas**: `Livro/.github/copilot-instructions.md`
  (Modo de Escrita Privada), `.github/agents/livro-writer.agent.md`,
  `.github/agents/arquiteto-densidade.agent.md` (Pêndulo Ação vs. Reação).
- **Janela aberta**: bloco Jogos 21-27 = 7 caps sem checkpoint → oferecer o
  checkpoint leve (próximos marcos: Movimento 3, caps. 32-35; Ponto Central,
  cap. 36).
- **Arquivos**: `conceitos/checklist-capitulo.md`, `protocolo-ingest.md`,
  `log.md` + repo Livro (3 arquivos).

## 2026-09-11 (Mini-INGEST — cap. 27 fechado)

- **Cap. 27 ("O Cerco", título provisório) COMPLETO**: 2.050 palavras (POV Mário). `capitulos/capitulo-27.md` criado (Resumo/Personagens/Eventos/Sementes e Conexões); visuais de Mário, Kate e Lakand atualizados; sementes #1 e #10 marcadas como executadas; tabela de progresso do `esquema-l1.md` atualizada e **ressincronizada** no mesmo dia (palavras medidas nos arquivos; % = acumulado ÷ 115.000: cap. 26 = 3.245/~60,4%; cap. 27 = 2.050/~62,2%).
- **Canon**: fase escolar (colégio) já registrada na entrada anterior de 2026-09-11; o confronto da Voz saiu como planejado (língua + corpo + "Por que só agora?" + silêncio).
- **Fronteira**: cap. 27 → cap. 28 ok (vozes do cerco morrem uma a uma = chegada dos Inquiridores de madrugada; sem contradições com o Mini-INGEST do cap. 26).
- **Decisões do autor (mesmo dia)**: "Vermes de Vidro" RETIRADOS do plano (nota estrutural atualizada); tabela de progresso ressincronizada (palavras medidas; % = acumulado ÷ 115.000) — correção: os valores antes atribuídos aos caps. 25/26 estavam trocados (25 = 2.314; 26 = 3.245). Beat "mede uma ferramenta" esclarecido (percepção de Mário sobre Kate medir as pessoas como ferramentas) — **registrado em `insights/kate-mede-ferramenta.md`** (decisão do autor, 2026-09-11); realocação a decidir no checkpoint de beat.
- **Pendente**: passe anti-slop (aguardando decisão do autor).
- **Arquivos**: `capitulos/capitulo-27.md`, `visuais/{mario,kate,lakand}.md`, `temas/sementes.md`, `temas/esquema-l1.md`, `log.md`.

## 2026-09-11 (canon — fase escolar de Mário na morte de Lucas: colégio)

- **Decisão (autor)**: quando Lucas morreu, Mário estava no **ensino médio** — ainda não na faculdade; o Direito (e o método de jurista) veio depois. A inadequação da morte de Lucas fica pura: na época, ele tinha a palavra, não a ferramenta.
- **Aplicado na prosa (cap. 27, confissão)**: "que era das leis" → "que acabou no direito"; "um problema de retórica" → "Como se tudo se resolvesse na conversa"; "aula de direito civil" → "aula de história".
- **Ficha**: `personagens/mario.md` ganhou o bullet "Fase escolar (canon 2026-09-11)".
- **Arquivos**: `Livro 1/capitulo27.md`, `personagens/mario.md`, `log.md`.

## 2026-09-10 (Resoluções pós-varredura — rascunho cap. 22, beat da pregação, Ponto Central, inquiridor)

- **Rascunho do cap. 22 excluído pelo autor**: referência morta limpa em `capitulos/capitulo-21.md`; o trecho (amanhecer/Mina) permanece absorvido na abertura do cap. 23.
- **Beat "Mário prega sem cura e falha" — plano refeito**: não é capítulo próprio; a cadeia final é cap. 23 (recebe sem pedir) → cap. 25 (cura intencional: funciona e expõe a fissura "Você só quer vencer") → cap. 26 (segunda pregação: oposição, reconhecimento, fuga). A "falha" é de comunhão, não de poder. Textos atualizados: `capitulos/capitulo-23.md` (Fronteira), `conceitos/milagre.md`, `temas/esquema-l1.md`.
- **Ponto Central resolvido: cap. 36** ("A Tomada da Mina de Quartzo", PoV Mário), ~68% — a "~55%" do esquema e o "~34-35" do outline/arco-stc eram estimativas antigas; o plano cap-a-cap tem o cap. 36. Jogos e Diversão = caps. 21-35.
- **`personagens/inquiridor.md` corrigido (canon 2026-09-06)**: linha do cap. 7 restaurada (Nolan QUER os Inquiridores capturando qualquer Souhma; impostor morre na aferição) e linha do cap. 13 precisada (Kenod — competição de oferta).
- **Re-ingest do cap. 25 (executado na mesma data)**: `capitulos/capitulo-25.md` realinhado ao manuscrito final; a seção do cap. 25 no `esquema-l1` corrigida e a do **cap. 26 ganhou os bullets da segunda pregação/oposição**; `index.md`, `visuais/{kate,lakand,mario}.md` e a nota da "cura intencional" em `conceitos/milagre.md` atualizados — a oposição/carroceiro fica só no cap. 26 (revisão 2026-08-30).

## 2026-09-10 (F13 — Teste Anti-Slop; piloto de calibração no cap. 26)

- **Novo teste no protocolo de sessão**: `conceitos/checklist-capitulo.md`
  ganhou o **F13 — Teste Anti-Slop** (caça ao "gosto de IA"). Roda no
  congelamento ou sob pedido — **não** por capítulo no modo privado.
- **Piloto de calibração no cap. 26** (POV Kate): os tiques reais do material
  são de **densidade de muleta** — símiles "como quem/como se" (16 na
  narração), fórmula "a voz saiu + adjetivo" (8×), filtro "sentiu" (~12×),
  abstrações como sujeito ("o ar mudou", "o peso das palavras", "o tempo
  parou"), finais de cena sumariando a emoção (3). Tiques genéricos de
  tradução ("engoliu em seco" etc.) = zero no material.
- **Falsos positivos preservados**: "formigamento nas mãos" (semente #11);
  diálogos-padrão de personagem não são muleta.
- **Passe oficial criado (repo do Livro)**: subagente `Editor Anti-Slop`
  (`.github/agents/editor-anti-slop.agent.md`) + comando `passe-anti-slop`
  (`.github/prompts/passe-anti-slop.prompt.md`); no ciclo de revisão, roda
  entre a coerência e o linguístico.
- **Atualização (decisão do autor, mesma data)**: o passe passa a **rodar a
  cada capítulo fechado** no modo privado (cirurgia local, na janela do
  Mini-INGEST — ou estacionado em lote, a pedido); não espera o congelamento.
  No congelamento permanece só a varredura final leve. Sincronizados: F13,
  `protocolo-ingest.md` (DoD + exceção), guardrails e modo do Livro, agente e
  prompt do passe.
- **Arquivos**: `conceitos/checklist-capitulo.md`, `protocolo-ingest.md`,
  `log.md`.

## 2026-09-10 (Sincronização de numeração — esquema-l1.md)

- **Numeração das seções de detalhe alinhada aos arquivos do livro** (numeração
  nova): todos os labels foram re-numerados (+1 a partir do antigo cap. 2) —
  Jogos e Diversão: caps. 21-36; Movimento 1: 21-22; Movimento 2: 23-31;
  Movimento 3: 32-35; Ponto Central: cap. 36; tabela de notas estruturais idem.
- **Referências cruzadas atualizadas**, incluindo correções canônicas:
  vembra / Miram→Rastro → cap. 24; revelação Juleen (enforcamento) → cap. 32;
  "Saramant é cinza" → cap. 26; decreto "prenda. Vivo." → cap. 18; fluência em
  ornickenho + desejo de Lakand (A Jaula) → cap. 13; "veio da Terra" (aferição)
  → cap. 3; Javé: caps. 21-30 não usam, reveal no cap. 31.
- **Cabeçalho**: lista de capítulos escritos atualizada para 0-26; nota de
  sincronização adicionada; aviso de numeração antiga (Vilões em diante)
  reformulado.
- **Pendências sinalizadas ao autor**: "pacifismo do cap. 2" (→3);
  "Mário prega sem cura e falha" (→24; sem capítulo canônico correspondente na
  sequência atual); linha "O arco de Kate" da tabela (beats de 25/28 podem
  pertencer ao cap. 26); conteúdo do cap. 27 ainda com Cristálides (decisões de
  2026-09-07 pendentes de aplicação na seção).
- **Arquivos**: `temas/esquema-l1.md`, `log.md`.

## 2026-09-10 (Varredura completa de numeração — storybible)

- **Repositório inteiro sincronizado à numeração nova** (+1 a partir do antigo
  cap. 2; caps. 0-1 inalterados): `capitulos/` (títulos, frontmatter e refs),
  `visuais/`, `lugares/`, `temas/`, `personagens/`, `conceitos/`, `insights/`,
  `decisoes/` e `index.md`.
- **Arquivos renomeados** (numeração nos nomes): `decisoes/glossolalia-invertida-oracao-cap19.md`
  → `...-cap20.md`; `decisoes/cartas-cap23-versao-b.md` → `...-cap24-versao-b.md`;
  `decisoes/eu-sou-sermao-feira-tronk-cap24.md` → `...-cap25.md`;
  `decisoes/oposicao-pregacao-cap24-para-cap26.md` → `...-cap25-para-cap26.md`
  (links de entrada atualizados).
- **Correções canônicas aplicadas na varredura**: enforcamento de Juleen →
  cap. 32 (não 31); revelação vembra/Mira → cap. 24; confissão "Saramant é
  cinza" → cap. 26; decreto "prenda. Vivo." → cap. 18.
- **Notas históricas**: entradas anteriores deste log mantêm a numeração da
  época (ver nota de 2026-09-03); paths de arquivos renomeados foram
  atualizados para não quebrar links.
- **Pendências sinalizadas**: "Mário prega sem cura e falha" sem capítulo
  canônico correspondente; `Livro 1/rascunho-capitulo22.md` citado mas
  inexistente; divergência do Ponto Central (34-35 vs. 36) entre `outline` e
  `esquema`; linha do cap. 7 na tabela de `personagens/inquiridor.md` (canon
  invertido em 2026-09-06).
- **Arquivos**: todos os acima + `index.md`, `log.md`.

## 2026-09-05 (Geografia de Ornick — filosofia hegralista + reconciliação da Academia)

- **Filosofia hegralista registrada a partir da fonte** ("Geografia geral de
  Ornick.docx"): hegralismo = o "humanismo" de Ornick, fundado por
  **Garun-thor Hegral**, berço na ilha de **Vitysh**; igualdade das raças
  conscientes + união em civilizações fortes para sobreviver num mundo
  dominado pelos deuses e por criaturas monstruosas; sobrevivência pela
  **sabedoria**. Hegralianos = "os da ilha de Vitysh" (cuidado com a vida e
  o lucro); no Reino, via Lupe'i, abraçados por intelectuais anti-Segregação.
  Novo verbete **Humanistas** (leviantares anti-Segregação em Gus).
- **Reconciliação da Academia dos Artífices** (fonte vs. aplicação 2026-09-05):
  a Academia oficial do Reino fica na **Metrópole** (miniatura do Castelo do
  Saber, em Vitysh — a maior de Ornick); em **Gus** existe o **embrião de
  nova Academia**, para onde migraram os melhores professores hegralianos
  fugindo da opressão de Genocydo (desmantelamento do cap. 7). É de lá que
  Kate arregimenta. Novo verbete **Castelo do Saber**.
- **Arquivos**: `conceitos/glossario.md` (Hegralismo, Hegralianos,
  Humanistas, Academia Metrópole/Gus, Cidadela de Gus, Castelo do Saber),
  `personagens/lupei.md`, `insights/nolan-sufoca-boatos-sinal.md`,
  `temas/esquema-l1.md`, `log.md`.

## 2026-09-05 (rodada de canon aplicada — final do L1 / Alavria)

- **Morte de Genocydo**: agora morre por um **alavriano** (infiltrado do
  destacamento), não pelo Lakand (esquema atualizado). Beat do Lakand em aberto.
- **Alavria no L1 = destacamento oculto** (infiltrados + força de choque) que
  entra via portão de Koda na incursão de Kate; mata Genocydo e tenta tomar a
  cidade por dentro; **aniquilado pela ação divina** ("estilo premonição",
  eco do sonho do cap. 1 — exceção deliberada ao guardrail do milagre). No L2,
  Alavria prepara incursão frontal de revide.
- **Mário é coroado também por medo** do deus que causou a carnificina
  (legitimidade envenenada → solo do L2).
- **Kate arregimenta em Gus** (hegralianos da Academia dos Artífices +
  convertidos; infiltrados de Alavria entre eles) e bole o cerco.
- **Portão**: Koda executa a abertura (por Alavria); Nolan crê liderar (o golpe
  dele); Lupe'i fora.
- **Transporte de Mário**: Clãs de Sangue o entregam a Genocydo (sem
  Inquiridores); Caixão de Tortura.
- **Valinor**: morre defendendo a Metrópole da incursão de Kate.
- **Arquivos**: `lugares/alavria.md`, `conceitos/glossario.md` (+ verbetes
  Hegralianos, Academia dos Artífices, Cidadela de Gus), `index.md`,
  `personagens/valinor.md`, `conceitos/renath.md`,
  `insights/nolan-controla-rampillas.md`, `temas/esquema-l1.md` (final),
  `insights/nolan-sufoca-boatos-sinal.md`, `log.md`.
- **Em aberto**: beat do Lakand no final; reconciliação do beat de resgate
  (Gus/Clãs); colaterais da carnificina divina; grau de consciência de Nolan
  no portão (enquadramento recomendado aplicado no esquema).

## 2026-09-05 (canon L1 — Koda consuma a traição; infiltrados de Alavria na invasão de Kate)

- **Koda trai no L1 (consumação)**: a traição de Koda se consuma no L1 — ele
  facilita a entrada dos infiltrados de Alavria durante a invasão de Kate à
  Metrópole (portão aberto no festival). Descoberta continua no L2 (Gunad).
- **Infiltrados de Alavria entre os hegralianos de Gus**: alguns hegralianos
  que Kate arregimenta na Cidadela de Gus (de Lupe'i) são agentes de Alavria;
  usam a invasão de Kate para matar Genocydo e tomar a Metrópole por dentro.
- **Insight ampliado**: `insights/nolan-sufoca-boatos-sinal.md` — seção
  "Camada Koda/Alavria (objetivos em camadas)" + "Pontos de coerência em
  ABERTO" (quem mata Genocydo, timing da invasão, invasão externa vs. por
  dentro, consciência de Lupe'i, coroação de Mário, atualização de
  `alavria.md`).
- **Arquivos**: `personagens/koda.md` (consumação + numeração corrigida 3→4,
  6→7, 13→14), `insights/nolan-sufoca-boatos-sinal.md`, `log.md`.

## 2026-09-05 (insight — Nolan sufoca boatos do Sinal + correção de numeração)

- **Insight registrado** (amarelo/estrutural, destino: revisão caps. 4-17 no
  congelamento do L1): objetivo ativo do Ato 1 de Nolan de sufocar os boatos
  sobre a falha do Sinal (controle da narrativa do divino). Origem: comentário
  do autor no cap. 0 L17 + investigação 2026-09-05.
- **Correção de numeração na ficha de Nolan**: `personagens/nolan.md` (seção
  Arco Narrativo) usava a numeração antiga; ajustada +1 para os arquivos
  atuais (3→4, 6→7, 9→10, 13→14, 16→17, 18→19, 19→20, 21→22).
- **Arquivos**: `insights/nolan-sufoca-boatos-sinal.md` (novo),
  `personagens/nolan.md`, `log.md`.

## 2026-09-05 (decisão — Sinal permanentemente instável, não mudo)

- **Correção de canon do Sinal de Vonos**: o Sinal NÃO emudeceu nem cessou.
  Ficou **permanentemente instável** — a frequência de Mário ocupou o canal
  e embaralhou a leitura (Vonos não foi cortado nem se calou). Milagres
  agudizam o embaralhamento, com **reverberação em Kate** (influência de
  Hícse). Vocabulário canônico: "perdeu o eixo", "não firma a leitura",
  "vem embaralhado/corrompido", "vacilou".
- **Falas de personagens corrigidas** (Benjamim, hegraliano, Nolan, Escriba,
  Inquiridor): descrevem instabilidade real, não mudez — sem mentira/engano.
- **Arquivos**: `conceitos/sinal-de-vonos.md` (Versão B),
  `capitulos/capitulo-00.md` (resumo), `decisoes/sinal-permanentemente-instavel.md`
  (novo), `log.md`. Texto do livro: `Livro 1/capitulo0.md` (L3, L15, L21,
  L29, L39), `Livro 1/capitulo3.md` (L50), `Livro 1/capitulo4.md` (L19, L21, L25).

## 2026-09-03 (Reestruturação — novo cap. 2 + cena do tribunal + micro-objetivo)

- **Reestruturação completa da numeração**: Novo capítulo 2 ("O Inquérito") inserido entre os antigos caps. 1 e 2. Toda a numeração deslocada em +1 (antigo cap. 2 → cap. 3, antigo cap. 3 → cap. 4, etc.). Capítulos 4-25 da numeração antiga agora são caps. 5-26.
- **Novo cap. 2 criado**: Mário na Terra após a morte do rapaz. Aula de Direito (raciocínio abdutivo — caso de omissão contratual). Inquiridor observa Mário na faculdade. Porta de Lucas (frieza familiar). Caderno "Regras do Absurdo" (micro-objetivo verbalizado). Voz progride para sussurro acordado. Sequestro.
- **Cena do tribunal inserida no cap. 4 (Nolan vs. hegraliano)**: Nolan condena um hegraliano ao Gerikhad. O hegraliano acusa: "O Sinal se apagou. Vonos emudeceu. Até ele não aguenta mais olhar para o que você fez deste reino." Nolan não tem resposta. A fala ecoa nele.
- **Sementes de micro-objetivo inseridas**: Caps. 5 (duas luas — "preciso entender as regras"), 8 (vampiros/lobisomens — "se é loucura, por que tem regras?"), 11 (cura de Decian — "dois tipos de cura"), 13 (fluência em ornickenho — "se produz resultados, pode ser testada").
- **Arquivos**: `Livro 1/capitulo2.md` (novo), `Livro 1/capitulo3.md` (ajustado), `Livro 1/capitulo4.md` (cena do tribunal), `Livro 1/capitulo5.md` (semente), `Livro 1/capitulo8.md` (semente), `Livro 1/capitulo11.md` (semente), `Livro 1/capitulo13.md` (semente), `storybible/capitulos/capitulo-02.md` (novo INGEST), `storybible/temas/esquema-l1.md` (tabela atualizada), `storybible/temas/arco-stc.md` (atualizado), `storybible/temas/outline.md` (atualizado), `storybible/index.md` (atualizado), `storybible/log.md`.

- **Capítulo 25 finalizado (Mini-INGEST)**: PoV Kate, segundo discurso público de Mário em vila próxima a Ornick. Debate com carroceiro (argumentação filosófica — fato vs. conclusão), reconhecimento como Souhma, divisão da multidão, acusação de Saramant, Lakand trucida acusador, mercenário oferece recompensa e captura Mário, Kate fere mercenário, fuga, discussão na estrada, confissão de Lakand ("Saramant é cinza"), discussão sobre Theodore, Kate reafirma Mário como instrumento.
- **Sementes plantadas**: Carroceiro humilhado → informante dos caçadores (cap. 26); Mário questiona violência de Kate (eco no cap. 35); Lakand confessa Saramant por Kate (dívida do L1); Lakand acusa Kate sobre Theodore (afastamento); Recompensa por Mário reconhecida → caçadores no cap. 26.
- **Visuais atualizados**: `visuais/kate.md`, `visuais/mario.md`, `visuais/lakand.md` — cap. 25 adicionado.
- **Personagem atualizado**: `personagens/lakand.md` — confissão "Saramant é cinza" movida do cap. 24 para o cap. 25.
- **Arquivos**: `capitulos/capitulo-25.md` (novo), `visuais/kate.md`, `visuais/mario.md`, `visuais/lakand.md`, `personagens/lakand.md`.

## 2026-08-31 (decisão — "Eu Sou" ancorado no sermão da Feira de Tronk, cap. 24)

- **"Eu Sou" ancorado no clímax do sermão (decisão formal)**: Mário prega
  por iniciativa própria na Feira de Tronk usando "Deus" como ponte
  linguística. Consultor Teológico confirmou: em ornickenho, "deus" é
  categoria funcional (nome + domínio) — o povo ouviria "mais um deus do
  Limbo". A solução: ancorar o nome "Eu Sou" no clímax ("Porque ele é Deus.
  O Eu Sou. O que está acima do Limbo, acima dos deuses que pedem sangue."),
  ecoando palavra por palavra a oração do cap. 19. "Javé" permanece
  reservado para o cap. 30 (canon 2026-08-10).
- **Arquivos**: `Livro 1/capitulo24.md` (linha 83 — ancoragem aplicada),
  `decisoes/eu-sou-sermao-feira-tronk-cap25.md` (novo), `log.md`.

## 2026-08-30 (decisão — Nolan retorna à Metrópole; caçada via rampillas)

- **Nolan retorna à Metrópole para matar Juleen (decisão formal)**: recebe a
  carta de resposta de Layla sobre a vembra e decide voltar para resolver
  pessoalmente. O retorno é o custo na corrida (Inquiridores ganham
  vantagem).
- **Caçada via rampillas (sentidos à distância)**: Nolan deixa rampillas no
  encalço de Mário e observa à distância através deles (o mecanismo que
  Devour usava — "extensão do corpo"). O cap. 31 (observação) ganha
  mecanismo concreto. A cena mais fria do livro: Nolan enforcando Juleen
  enquanto "vê" Mário sobreviver à tempestade de quartzo.
- **Ossan opera os sentidos (não ensina)**: Nolan é leviantar, não xilomago;
  a dependência mantém a tensão; Ossan pode filtrar ou sabotar o que Nolan
  vê — bomba-relógio do L2.
- **Mecanismo com limitações**: percepção, não diálogo; alcance limitado
  pela raiz-mestra; foco dividido.
- **O enforcamento (cap. 31, POV Nolan — correção 2026-08-30)**: o
  enforcamento foi inicialmente registrado no cap. 30, mas o cap. 30 é POV
  Kate (o batismo) — não pode ser mostrado num capítulo cujo POV está no
  assentamento. Movido para o cap. 31, que abre com o enforcamento e segue
  para a observação via rampillas. Nolan chega com rampillas; Conselho o
  censura, ele ignora; rampillas trazem Juleen; Nolan não permite que a
  matem — ele mesmo quer fazer. A cena da acusação de humana (canon
  2026-08-30) acontece aqui.
- **Arquivos**: `decisoes/nolan-retorna-metropole-juleen-rampillas.md`
  (novo), `temas/esquema-l1.md` (caps. 28, 30, 31), `personagens/ossan.md`,
  `personagens/juleen.md`, `conceitos/rampillas.md`, `log.md`.

## 2026-08-30 (revisão cap. 23 — 3ª rodada do fluxo por capítulo, concluída)

- **Cap. 23 revisado (POV Nolan — "O Rastro")**: Guardião (Solicita reescrita
  focada — o bloco da vembra violava a decisão 08-19 que o movia para o
  cap. 25; resolvido: o cap. 25 é POV Kate, então a vembra fica no 23),
  Arquiteto (Aprovado com ajustes — carta a Koda diferenciada da carta ao
  Rei; joelho condensado; pontuação), Revisor (Aprovado com correções — 1
  crítico de modo verbal, 11 médios, 13 leves).
- **Correções aplicadas (lote final)**: carta a Koda abre com "Como escrevi
  ao Rei..." (elimina a duplicação verbatim); travessão na carta ao Rei →
  vírgulas; "não vire dívida nem pese nos cofres" (subjuntivo); pontuação
  de diálogo ("orgulhosa." / "Nolan disse."); "Nolan virou-se e acenou"
  (sujeito explícito); "A pele ao redor" (redundância); "Isso tornava ainda
  mais verdadeiro o que ele reconhecera" (sintaxe); "mente analítica exigia
  mais uma confirmação... dar como real" (período de 50 palavras cortado);
  "foi adormecendo aos poucos" (gerúndio passivo); "a carroça sobrevivera"
  (vírgula emendada); "O mundo que deixara para lá do Cran" (sintaxe);
  "Ela lhe devia um favor" (pronome); "título do homem que os humanos
  esperavam" (antecedente); "confundi-lo com vembra" (elipse); "saltado aos
  olhos" (idiomatismo); "não teria exército" (tempo verbal); "depois de ter
  nascido morto" (particípio).
- **Arquivos**: `Livro 1/capitulo23.md` (correções), `capitulos/capitulo-23.md`
  (atualizado), `log.md`.

## 2026-08-30 (revisão cap. 23 — 3ª rodada do fluxo por capítulo)

- **Cap. 23 revisado (POV Nolan — "O Rastro")**: Guardião (Solicita reescrita
  focada — o bloco da vembra violava a decisão 08-19 que o movia para o
  cap. 25; resolvido: o cap. 25 é POV Kate, então a vembra fica no 23),
  Arquiteto (pendente — ver abaixo), Revisor (pendente — ver abaixo).
- **Decisão do autor (cartas versão B)**: Nolan não pede a revogação da
  recompensa a Genocydo. Carta ao Rei semeia a dúvida (sem se expor); carta
  a Koda usa o argumento da dívida (a língua do Mestre da Moeda); carta a
  Layla investiga a vembra. Ver `decisoes/cartas-cap24-versao-b.md`.
- **Correções aplicadas no texto**: cartas reescritas (versão B); "Souhma"
  ancorado no assentamento (a velha murmura o termo — Nolan o ouve e o
  guarda); erros crassos corrigidos (Chavama → Chamava; "apontou com o
  norte" → "apontou para o norte"; "não tenha saltado" → "não tenham
  saltado"; "ao invés" → "em vez de"; "confundí-los" → "confundi-los");
  travessões na narração → vírgulas (3 ocorrências); hífen no diálogo →
  travessão; "Nolan disse—" → "Nolan disse —"; "A ficha estava caindo" →
  "A engrenagem encaixava"; parágrafo Genocydo destrinchado (antecedente
  claro).
- **Cena Nolan/Juleen (canon novo)**: no enforcamento (cap. 30), Nolan acusa
  Juleen de ser humana; ela se defende (é leviantar de casta baixa); Nolan
  não quer escutar — o preconceito beirando a loucura, espiral descendente
  que o levará a Cressadar e Terbs no fim do L1.
- **Arquivos**: `Livro 1/capitulo23.md` (correções), `capitulos/capitulo-23.md`
  (atualizado), `temas/esquema-l1.md`, `temas/sementes.md`,
  `personagens/{mira,mathias,juleen}.md`, `decisoes/cartas-cap24-versao-b.md`
  (novo), `log.md`.

## 2026-08-30 (decisões — cartas do cap. 23 versão B; vembra no 23; cena Nolan/Juleen)

- **Cartas do cap. 23 (versão B — decisão do autor)**: Nolan **não pede** a
  revogação da recompensa a Genocydo. Em vez disso: **a Genocydo** (versão
  censurada) informa que o Estrangeiro é real e **semeia a dúvida** ("se um
  mercenário o matar antes de aprendermos o segredo da cura, perdemos a
  chance") — sem pedir nada, sem se expor. **A Koda** (versão completa) usa
  o argumento da **dívida**: se um mercenário pegar Mário, a recompensa
  prometida vira dívida e os cofres sofrem — a língua do Mestre da Moeda.
  **A Layla** (investigação da vembra). Genocydo não revoga; Nolan joga o
  jogo longo em duas frentes sem expor a conspiração.
- **Vembra no cap. 23 (correção da decisão 08-19)**: a decisão 08-19 moveu a
  revelação da vembra para o cap. 25, mas o cap. 25 é **POV Kate** — a
  revelação não pode ser clímax de um capítulo que não a conhece. A vembra
  fica no cap. 23 (Mira comenta despretensiosamente; Nolan liga os pontos;
  carta a Layla). Misatribuição dos caps. 21-22 preservada; a fissura chega
  no 23 e fermenta até o 30.
- **Cena Nolan/Juleen (canon novo 2026-08-30)**: no enforcamento (cap. 30),
  Nolan acusa Juleen de ser **humana**. Ela se defende: é **leviantar** de
  casta baixa. Nolan **não quer escutar** — o preconceito beirando a
  loucura, espiral descendente que o levará, no fim do L1, a se aliar a
  Cressadar e Terbs (impensável para o Nolan do início). A verdade não o
  abranda: a classe absorve a raça (a periferia é impura, humana OU
  leviantar de casta baixa).
- **Arquivos**: `temas/esquema-l1.md` (caps. 21, 23), `temas/sementes.md`
  (#6), `personagens/mira.md`, `personagens/mathias.md`,
  `personagens/juleen.md`, `decisoes/cartas-cap24-versao-b.md` (novo),
  `log.md`.

## 2026-08-29 (revisão cap. 22 — 2ª rodada do fluxo por capítulo)

- **Cap. 22 revisado (POV Kate — "O Assentamento")**: Guardião (aprovado com
  ressalvas leves — símile da carta e "vocabulário" destoam do filtro de
  Kate; redundância das mães no pitch; Tae-Tabor confirmado no canon),
  Arquiteto (aprovado com ajustes — pitch condensado; justificativa dupla do
  riacho cortada; plantio do Souhma funcional), Revisor (aprovado com
  correções — 1 crítico de formatação: travessão na narração → parênteses;
  ~10 médios: sintaxe, redundâncias, desvios de voz; ~15 leves).
- **Correções aplicadas (24)**: travessão do parágrafo 4 → parênteses;
  "as mães dizem aos filhos" (2ª ocorrência) → "As mães da região não
  mentem: a Mina acaba com as pessoas"; "vocabulário para aprender" →
  "não tinha como aprender"; "espera uma carta que não chega" → "espera
  algo que não vem"; "Mário, seu nome, não é?" → "Mário, não é esse o seu
  nome?"; "Se lembrarão" → "Vão se lembrar"; "como ele fosse" → "como se
  ele fosse"; "já não era mais" → "já não era"; "atrasou" → "adiou";
  "inspirasse o que precisava inspirar" → "fizesse o que precisava fazer";
  entre outros.
- **Decisão de voz (registrada)**: "Mário, não é esse o seu nome?" mantém a
  tática retórica de Kate (usar o nome para criar intimidade na negociação)
  sem soar como se ela não soubesse o nome.
- **Arquivos**: `Livro 1/capitulo22.md` (correções), `log.md`.

## 2026-08-29 (decisão de processo — revisão por capítulo com os 3 agentes)

- **Mudança de fluxo (decisão do autor)**: durante a escrita privada do L1,
  cada capítulo fechado passa agora por **revisão em cascata** antes do
  Mini-INGEST: Guardião de Coerência → Arquiteto de Densidade → Revisor
  Linguístico. O congelamento continua com revisão cruzada final (consistência
  de voz entre capítulos, arco, sementes), mas o trabalho pesado é feito por
  capítulo. Motivação: qualidade da prosa (Le Guin), economia narrativa
  (Assis Brasil — cena vs. sumário) e erros crassos que se perdem no volume.
- **Modelo dos agentes**: frontmatters atualizados para
  `DeepSeek: DeepSeek V4 Flash 0731 (openrouter)` (sem sufixo batch — o
  modelo batch não roda em subagentes interativos).
- **1ª rodada executada (cap. 21)**: Guardião (aprovado com ressalvas —
  misatribuição de Dagmar como leitura de Nolan; "ninguém mais conseguia
  ler"; deslize temporal da parteira), Arquiteto (aprovado com ajustes —
  vistoria condensada; metáfora do arquivo mental variada; parágrafo
  Genocydo destrinchado), Revisor (aprovado com correções — "Eu o segurei";
  pleonasmos; redundâncias). Correções aplicadas no texto.
- **Falso positivo do Guardião (registro para memória)**: o Guardião
  interpretou "Ossan d'Tirath" como nome do pai e sugeriu renomear o filho —
  mas o canon registrado (`personagens/ossan.md`) confirma que Ossan d'Tirath
  É o filho de Devour (o pai é Devour). A correção foi revertida. Lição:
  validar sugestões de renomeação de personagens contra a storybible antes
  de aplicar.
- **Arquivos**: `Livro 1/capitulo21.md` (correções), `log.md`.

## 2026-08-28 (Mini-INGEST cap. 24 — "A Feira de Tronk")

- **Cap. 24 fechado (POV Mário)**: dias de caminhada; Lakand força Mário a comer; Feira de Tronk; briga por dívida; homem esfaqueado; **cura intencional** (ato de vontade, sem a Voz — contraste com cap. 22); pregação em quatro movimentos (evangelho correto em oposição à Voz); conversão genuína; carroceiro volta ("feiticeiro") — primeira hostilidade aberta; Kate intervém, Lakand se posiciona, curado se coloca na frente; descoberta da Metrópole (ilha no Cran, Muro Interno, Mina, dívida hereditária); mulher da barraca dá moedas (primeiro gesto de graça); gancho: Mário sente que Kate o observa "como quem mede uma ferramenta".
- **Canon duro**: cura intencional (primeira por ato de vontade, sem a Voz); Souhma aplicado a Mário (Kate já conhecia o termo — cap. 22:135); Metrópole = ilha no Cran + Muro Interno + Mina devora devedores + dívida hereditária; "Os deuses cobravam. Mas não davam." (generalização do POV de Mário, parcialmente errada); Kate não se ajoelha (eco cap. 22:129).
- **Arquivos**: `capitulos/capitulo-24.md` (criado), `visuais/mario.md`, `visuais/kate.md`, `visuais/lakand.md`, `temas/esquema-l1.md` (tabela), `log.md`.

## 2026-08-22 (canon — raridade da cura + tensão cessacionismo resolvida)

- **Raridade da cura (canon):** magia ornickenha não tem classe de cura — fere, nunca conserta. Kate pensa "magia feria, magia matava, magia nunca tinha consertado nada" (cap. 22). A cura da criança é salto de classe para os refugiados — por isso se ajoelham.
- **Iniciativa humana vs. milagre (canon — tensão resolvida):** Mário NUNCA opera milagre por iniciativa teológica. Cap. 22: ele não decide curar — é **movido** por compaixão desesperada antes de escolher. Reação de **choque, não vitória** — olha para as mãos como quem não reconhece o que elas fizeram. Cessacionismo preservado: ele **recebe** (cap. 22) e depois **tenta produzir** (cap. 23) e falha. Contraste receber vs. produzir = fio teológico do arco.
- **Arquivos**: `capitulos/capitulo-22.md` (trechos do cap. 22), `conceitos/milagre.md` (2 seções novas), `temas/esquema-l1.md` (bullet cap. 22), `log.md`.

## 2026-08-22 (Mini-INGEST cap. 22 — versão final revisada)

- **Cap. 22 fechado (POV Kate — "O Assentamento")**: dias de caminhada para o norte; jejum de Mário (desespero teológico, não disciplina); Lakand deslocado; **pitch da Mina em duas fases (revisão 2026-08-21/22 — canon)**: mapa → recusa de Mário à guerra ("não vou ser o estopim de nada") → Kate recalcula e vende **cura/esperança** (isca por omissão). Kate usa o nome de Mário pela primeira vez. Sétimo dia: assentamento de refugiados; cura da criança paralítica; Lakand pergunta "com magia?" (frame de magia/feitçaria, não milagre). Pessoas se ajoelham; Mário recua. Kate recalibra o desprezo em "potencial" ("sofrimento e esperança na medida certa viram aço"). Tique do pulso. Mário não ora, não come.
- **Canon duro**: pitch da Mina = cura como isca (mentira por omissão de Kate); Kate não conhece "milagre" — enquadra como cura/magia; Lakand fala pela primeira vez pós-endurecimento (cap. 22, não cap. 24) — o cap. 24 não repete o "primeiro som"; o gancho "se a cura cessasse, as palavras dele morriam junto" prepara o cap. 23.
- **Arquivos**: `capitulos/capitulo-22.md` (atualizado), `visuais/kate.md`, `visuais/mario.md`, `visuais/lakand.md`, `personagens/lakand.md` (1ª fala), `temas/esquema-l1.md` (bullet revisto), `index.md`, `log.md`.

- **Cap. 21 fechado (POV Nolan — "A Pira Involuntária")**: cold-open da fuga
  das chamas (Mathias salva Nolan/Saboc; o choque do vivo), luto frio (marco
  de pedras + rito fúnebre de Vonos), misatribuição (humanos adoeceram a
  esposa — a pista da vembra fica para o cap. 25), Mira = ama de leite,
  fundação da base (raiz-mestra exposta pelo fogo; Ossan como asset;
  "foram gente"), click de Mathias ("um deus acima do Limbo" por categoria),
  partida para possuir Mário (não matá-lo).
- **Canon duro**: Nolan controla os rampillas (~uma dezena) via raiz-mestra;
  o anel de Dagmar fica no marco (única herança para Saboc — L2); castelo de
  Devour vira base de Nolan; Nolan parte para o norte (rota de Mário/Kate).
- **Arquivos**: `capitulos/capitulo-21.md` (criado), `visuais/nolan.md`,
  `visuais/mathias.md`, `temas/esquema-l1.md` (tabela), `index.md`, `log.md`.

## 2026-08-19 (decisão — fio vembra move p/ cap. 25; concorrentes p/ cap. 28)

- **Revelação de Mira (vembra) move do cap. 21 para o cap. 25** (POV Nolan):
  vira o clímax/clifhanger do cap. 25, somado à delegação (carta a Layla).
  O cap. 21 fecha mais enxuto (fundação raiz/Ossan + click de Mathias +
  partida, sem a pista do veneno). Mira comenta a vembra de forma
  **despretensiosa** (comentário solto, sem intenção) na estrada da caçada;
  é Nolan quem liga os pontos (nota privada até o cap. 30). A misatribuição
  dos caps. 21-24 fica mais pura (cegueira sem a fissura da vembra).
- **"Os concorrentes chegam" move do cap. 25 para o cap. 28**: a dedução
  da recompensa de resgate ("prenda, vivo" — canon cap. 17) fecha no local
  da emboscada, onde Nolan confronta os Inquiridores e lê a evidência
  física. Cap. 25 fica com 3 movimentos: confirmação do milagre, certeza
  política (carta a Koda), revelação de Mira + delegação.
- **Arquivos**: `temas/esquema-l1.md` (caps. 21, 25, 28), `temas/sementes.md`
  (#6), `personagens/mira.md`, `log.md`.

## 2026-08-17 (canon — cap. 20 fechado; manto visto pelo POV; trecho movido p/ cap. 22; sync da mecânica da Voz)

- **Manto de Tharin (POV)**: cena do cap. 20 reescrita — Mário, dono do PoV, não viu o enterro (cap. 5, POV Kate); agora ELE VÊ Kate desenterrar a cova do mocambo queimado e tirar o manto dos ombros do corpo de Tharin (pragmatismo sem culpa). Resolve a dúvida do autor sobre o manto "enterrado sozinho" — o manto estava COM Tharin (ver `decisoes/manto-xilomagia-tharin.md`).
- **Trecho do amanhecer/Mina MOVIDO do cap. 20**: cap. 20 termina em "E adormeceu." (fecho no protesto/Jó). O trecho (riacho, mãos, pitch da Mina) vai para a abertura de um capítulo depois do 21 (o 21 é POV Nolan) — salvo em rascunho do cap. 22 (excluído em 2026-09-10; conteúdo absorvido no cap. 23); POV a decidir (Mário ou Kate — o pitch é o plano dela, ironia dramática).
- **"não conseguiu transformar em oração" descartado**: Mário não oraria nessa situação (está irado com Deus); a linha atual ("transformou o pouco de suas forças em lágrimas secas, em silêncio, em febre") é mais coerente.
- **Parágrafo do controle teológico removido** ("O controle era o vício dele") — autor: explicava demais; Mário ainda não pode nomear o caco; a acusação de Jó opera sem autoconsciência.
- **Identificação de Deus confirmada (fecha pendente 2026-08-16)**: Mário reconhece a Voz como Deus no cap. 20 (prova inequívoca: orou + ressuscitou) e responde com RAIVA. No cap. 26, a Voz dá a "enquadrada" em Mário por causa dessa raiva (confronto com os dois argumentos de ação oculta — ver `temas/esquema-l1.md` cap. 26).
- **Sync da mecânica da Voz (fecha pendentes anteriores)**: `decisoes/glossolalia-invertida-oracao-cap20.md` (Mecânica da Voz → ditado na mente + própria voz, sem possessão; distinção do cap. 12), `capitulos/capitulo-12.md` (fluência habilitada, não possessão), `capitulos/capitulo-19.md` (Mário LEMBRA do ditado; testemunha consciente).
- **Arquivos**: `Livro 1/capitulo20.md`, rascunho do cap. 22 (excluído em 2026-09-10; absorvido no cap. 23), `decisoes/glossolalia-invertida-oracao-cap20.md`, `capitulos/capitulo-12.md`, `capitulos/capitulo-19.md`, `log.md`.
- **Mini-INGEST cap. 20 (2026-08-17)**: `capitulos/capitulo-20.md` criado; visuais Mário/Kate/Lakand atualizados; tabela do esquema atualizada; fronteira p/ cap. 21 (Nolan) ok.

## 2026-08-16 (canon — ódio racial de Nolan: cristaliza na misatribuição, não na verdade)

- **Resolução da pergunta do autor (semente #6)**: o ódio racial de Nolan
  (L2, "agora pessoal") cristaliza na MISATRIBUÇÃO (caps. 18-25 — os humanos
  mataram Dagmar), não na descoberta do cap. 30. A verdade (Juleen,
  leviantar de casta baixa dos burgos periféricos) NÃO dissolve o ódio:
  luto sem fechamento; ódio sobrevive à justificativa (cena do cap. 30
  mostra o "não foram os humanos" redirecionando, não abrandando); classe
  absorve raça (a periferia é impura, humana ou leviantar). Juleen
  permanece leviantar — humana validaria a Segregação.
- **Arquivos**: `temas/sementes.md` (#6), `temas/esquema-l1.md` (cap. 21),
  `log.md`.

## 2026-08-16 (canon — caps. 21-25: agenda oculta de Mário — provar os dogmas)

- **Agenda oculta (canon)**: nos Jogos (caps. 21-25), Mário prega buscando
  conversões, mas o motor é **provar que os dogmas dele estão certos** — no
  limite, que **Deus está errado e ele certo**, sem verbalizar. A pregação é
  a acusação contra Deus (inação na morte de Lucas) em forma de tribunal;
  cada convertido é um veredito. Tentativa de resolver as coisas do JEITO
  ERRADO — o cap. 26 desnuda isso.
- **Registrado em**: `temas/esquema-l1.md` (nota de arco do cap. 20),
  `temas/sementes.md` (#10), `personagens/mario.md`, `log.md`.

## 2026-08-16 (canon revisto — cap. 20: identificação irada; função do cap. 26 muda)

- **Decisão do autor (comentário do lote)**: Mário IDENTIFICA a Voz como Deus
  JÁ no cap. 20 — não como confissão, mas como acusação (eco de Jó). A Voz
  permanece em silêncio até o cap. 26, que passa a desnudar a raiva.
- **Cap. 20 reescrito**: oscilação → identificação irada (a palavra "É Deus"
  pousa; a resposta é raiva pela inação na morte de Lucas; segura os dogmas
  como escudo e não ora); final → "sabia de quem; o que não sabia era como
  continuar falando com ele" + "a raiva contra Deus".
- **Canon atualizado**: estado intermediário (2026-08-16) REVERTIDO para
  identificação irada em `personagens/mario.md`, `conceitos/milagre.md`,
  `temas/sementes.md` (#10), `temas/esquema-l1.md` (caps. 20 e 26).
- **Efeito sanfona revisto**: deixar de orar vira recusa irada, não cegueira
  cessacionista; Mário continua fazendo o que a teologia manda sem a relação.
- **Arquivos**: `Livro 1/capitulo20.md`, `personagens/mario.md`,
  `conceitos/milagre.md`, `temas/sementes.md`, `temas/esquema-l1.md`,
  `log.md`.

## 2026-08-16 (lote de comentários do autor — cap. 20: protesto sobre Lucas; culminação Jó; delírio sem 'por culpa')

- **Delírio**: removido "por culpa" (Mário ainda não pode nomear o caco de
  vidro — a teologia foi construída por culpa, mas ele não sabe disso).
- **Acusação reescrita**: o protesto agora é contra a INação da Voz na morte
  de Lucas (não o garoto do cap. 1); "a fé nunca foi necessária, então não
  foi a minha fé que faltou para o Lucas: você podia ter agido, e não agiu";
  culmina em "Você é Deus? Por que está sendo tão cruel comigo? Não parece
  justo." (eco de Jó).
- **Final do cap. 20**: a pergunta suprimida deixou de ser "quem é você?"
  (já gritada na acusação) e virou "o nome que ele não conseguia dizer em
  oração".
- **Canon novo (mario.md)**: frieza de Mário com pais/irmã após Lucas (no
  fundo, os culpa por terem deixado Lucas entrar nas drogas); beira da
  apostasia no cap. 20, mas é eleito — não vai até o fim; eco de Elias e Jó.
- **PENDENTE (decisão do autor)**: comentário sobre Mário identificar Deus
  com a Voz JÁ no cap. 20 (reverteria o estado intermediário registrado em
  2026-08-16). Não aplicado — aguarda decisão; afeta a oscilação, o final e
  a função do cap. 26.
- **Arquivos**: `Livro 1/capitulo20.md`, `personagens/mario.md`, `log.md`.

## 2026-08-16 (correção — delírio do cap. 20: Lucas ≠ rapaz do cap. 1)

- **Erro corrigido (canon)**: o delírio do cap. 20 e as notas do esquema
  (cap. 20) e da ficha do Mário conflavam a morte de Lucas com a cena do
  cap. 1 (a cobrança de dívida de droga). Correção: a hesitação/recusa da
  Voz foi com o RAPAZ da rua (cap. 1 — "não há protocolo para milagres");
  a Voz NUNCA pediu que Mário agisse por Lucas, Mário não viu o corpo do
  irmão, e Lucas morreu ANTES do castelo de dogmas (a teologia foi
  construída depois, por culpa). A sombra de Lucas = inadequação, não
  recusa.
- **Cap. 20 corrigido**: delírio reescrito (o rapaz da cobrança morre nos
  braços de Mário, "valeu... por tentar"; o rosto dele vira o de Lucas no
  eco da droga); acusações "com o Lucas, você pediu" → "com aquele rapaz".
- **Arquivos**: `Livro 1/capitulo20.md`, `temas/esquema-l1.md`,
  `personagens/mario.md`, `log.md`.

## 2026-08-16 (canon — cap. 26: fim da moldura de esquizofrenia sobre a Voz; correção de confluência)

- **Cap. 26 (canon)**: confirmado como o momento em que o fio 1 fecha —
  Mário deixa de ler a Voz como delírio privado (o corpo inteiro como prova
  externa); o fio 2 (a Voz é Deus) segue aberto (cessacionismo); o fio 3
  (o sonho é real) fecha no L2 (gravura). Registrado em
  `temas/esquema-l1.md` (cap. 26), `personagens/mario.md`,
  `conceitos/milagre.md`.
- **Correção (mesma confluência)**: no cap. 20, a passagem do recuo de
  identificação dizia "um irmão na calçada" — corrigido para "um rapaz
  na calçada" (o cap. 1, não Lucas).
- **Arquivos**: `Livro 1/capitulo20.md`, `temas/esquema-l1.md`,
  `personagens/mario.md`, `conceitos/milagre.md`, `log.md`.

## 2026-08-16 (canon — cap. 20: estado intermediário da Voz; Nolan × Dagmar; click da Bíblia; Juleen)

- **Cap. 20 (Livro 1) — agência total + estado intermediário**: a lembrança
  febril passa a cobrir a cadeia inteira da Voz (pergunta, ordem, mão,
  toque, oração — "nada tinha sido dele"); a acusação ganha "Eu nunca fui
  necessário"; inserido o recuo de identificação em estado intermediário
  ("É Deus... não pode ser... o Deus que eu conheço não age assim... não
  sei o que pensar") por custo volicional (jogar fora o castelo de dogmas);
  a pergunta suprimida do final agora é explícita ("quem é você?").
  Preserva a germinação do cap. 26 (a Voz confronta exatamente a
  resistência).
- **Nolan × Dagmar (canon)**: entre o cap. 18 e a pista da vembra (cap.
  21), a explicação de Nolan é a ideologia — contato com humanos na viagem
  (eco do pai, prostituta humana; origem da Segregação). Misatribuição
  cristaliza o ódio racial do L2; a verdade (Juleen) inverte a Segregação:
  o inimigo estava dentro. `temas/sementes.md` #6, `temas/esquema-l1.md`
  (cap. 21), `personagens/nolan.md`.
- **Click do cap. 21 (canon)**: com a Bíblia de Kraviam (o "livro de
  Genocydo"), por CATEGORIA (um deus fora do Conselho), não por leitura —
  Nolan não lê a Bíblia (cap. 13). Distinguido do diário (semente #15).
  Execução: Mathias plano + reinterrogação; Mira como 2ª testemunha; Nolan
  arquiva a teologia (erro de catálogo = Kate). `temas/sementes.md` #10,
  `temas/esquema-l1.md`, `personagens/mathias.md`.
- **Juleen (canon)**: aia de Dagmar, leviantar de casta baixa dos burgos
  periféricos (não humana — a inversão temática exige). Ficha criada em
  `personagens/juleen.md`.
- **Mário (canon)**: estado intermediário registrado na ficha e no
  `conceitos/milagre.md` (POV: renderiza a oscilação, nunca confirma).
- **Arquivos**: `Livro 1/capitulo20.md`, `temas/sementes.md`,
  `temas/esquema-l1.md`, `personagens/{juleen,mario,nolan,mathias}.md`,
  `conceitos/milagre.md`, `index.md`, `log.md`.

## 2026-08-15 (canon — Genocydo/Kraviam: Química, cristão nominal, língua)

- **Formação e língua de Kraviam (canon)**: instruído em **Química na Terra**
  (explica o antraz/Guerra do Grifo e o "pó letal" do cap. 6); cristão
  **nominal** (não fiel); aprendeu ornickenho **com os Guenayer** — por
  esforço humano, NÃO por milagre (contraste com Mário, que recebeu a língua
  da Voz no cap. 12). Registrado em `personagens/genocydo.md`.
- **Arquivo**: `personagens/genocydo.md`, `log.md`.

## 2026-08-15 (auditorias: Lakand, Genocydo, Benjamim, gornads)

- **Genocydo (aplicado)**: 5 falas ajustadas (fresta de ansiedade na fala;
  sem autodiagnóstico lúcido; ameaça de estoque → súplica obsessiva),
  gramática (3) e travessões U+2015→U+2014 no cap. 6.
- **Lakand (decisão B)**: evolução registrada na ficha — falante só com Kate
  antes do endurecimento; cap. 12 = única confissão (âncora do L2).
- **Gornads (política por casta)**: quebrado = casta baixa (Tharin);
  Gaviorn'l régio; Estruzzo guerreiro fluente (lidera após Gaviorn'l). 3
  falas ajustadas.
- **Benjamim**: nenhum erro de linha; semente #17 (cena de manipulação em
  ação) registrada.
- **Estruzzo**: semente #18 (presença/liderança) registrada.
- **Arquivos**: caps. 0, 5, 6, 11; `temas/tom-e-voz.md`,
  `personagens/lakand.md`, `temas/sementes.md`, `log.md`, agente
  `livro-writer`.

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
  cap. 19 (`decisoes/glossolalia-invertida-oracao-cap20.md`). Texto canônico
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
