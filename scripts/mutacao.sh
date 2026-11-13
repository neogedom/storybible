#!/usr/bin/env bash
# Teste de detecção do Teste 4: reintroduz, em cópias descartáveis, os problemas
# encontrados à mão e os problemas novos, e confere se o checklist os aponta.
# Os repositórios reais não são alterados.
set -u
DIR="$(cd "$(dirname "$0")" && pwd)"
SB="$(cd "$DIR/.." && pwd)"
LV="$(cd "$SB/../Livro" && pwd)"
CHK="$DIR/checar_consistencia.py"
BASE="$(mktemp -d)"
trap 'rm -rf "$BASE"' EXIT
pass=0; fail=0

fresh() {
  rm -rf "$BASE"; mkdir -p "$BASE"
  cp -r "$SB" "$BASE/sb"
  cp -r "$LV" "$BASE/lv"
}
run() { python3 "$CHK" --sb "$BASE/sb" --lv "$BASE/lv" 2>&1; }
check() {  # $1 nome, $2 regex esperada, $3 mínimo de ocorrências
  local out n
  out=$(run)
  n=$(printf '%s\n' "$out" | grep -c -E "$2")
  if [ "$n" -ge "$3" ]; then
    echo "PASS  $1  ($n ocorrência(s))"; pass=$((pass+1))
  else
    echo "FAIL  $1  (esperado >= $3, obtido $n)"; fail=$((fail+1))
  fi
}

# M1: caps. 34 a 38 sem ingest (problema encontrado à mão)
fresh; rm -f "$BASE/sb/capitulos/capitulo-3"{4,5,6,7,8}.md
check "M1 caps. 34-38 sem ingest" "revisado, mas sem ingest" 5

# M2: nome estranho fora da storybible (o caso "Iquize", encontrado à mão)
fresh; printf '\nEntão Iquize disse que a hora chegou.\n' >> "$BASE/lv/Livro 1/capitulo20.md"
check "M2 nome 'Iquize' fora do cânone" '"Iquize" \(' 1

# M3: caminho .github/ antigo em documento vivo (encontrado à mão)
fresh; printf '\nVeja `.github/agents/livro-writer.agent.md` para o fluxo.\n' >> "$BASE/lv/CLAUDE.md"
check "M3 caminho .github/ antigo em doc vivo" 'livro/CLAUDE\.md:[0-9]+ aponta para' 1

# M4: capítulo sem linha no esquema (encontrado à mão, no passado)
fresh; sed -i '/^| 40 /d' "$BASE/sb/temas/esquema-l1.md"
check "M4 cap. 40 sem linha no esquema" 'cap\. 40 sem linha no esquema' 1

# M5: POV divergente entre esquema e ficha
fresh; sed -i '/^| 34 /s/Mário/Kate/' "$BASE/sb/temas/esquema-l1.md"
check "M5 POV divergente cap. 34" 'cap\. 34: POV divergente' 1

# M6: caminho citado que não existe
fresh; printf '\nConsulte `../storybible/temas/inexistente.md`.\n' >> "$BASE/lv/CLAUDE.md"
check "M6 caminho citado inexistente" 'inexistente\.md' 1

# M7: "?" no lugar de acento num capítulo que estava limpo (corrupção do tipo encontrado hoje)
fresh; printf '\nA c?ncer da cidade.\n' >> "$BASE/lv/Livro 1/capitulo20.md"
check "M7 '?' no lugar de letra em cap. limpo" 'capitulo20\.md: [0-9]+ "\?" no lugar de letra' 1

# M8: seção "Pendências" do cap. 36 fica vazia, como aconteceu com os caps. 37 e 38
fresh; sed -i '/^## Pendências/,$ { /^- /d }' "$BASE/sb/capitulos/capitulo-36.md"
check "M8 seção Pendências vazia (cap. 36)" 'capitulo-36\.md: seção "Pendências' 1

echo
echo "resultado: $pass passaram, $fail falharam"
exit $fail
