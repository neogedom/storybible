# Protocolo INGEST — Finalização de Capítulo

## Quando executar

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
