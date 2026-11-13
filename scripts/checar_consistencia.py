#!/usr/bin/env python3
"""Teste 4 do plano-teste-processo: checklist automático de consistência
entre a storybible e o livro. Somente leitura: não altera nenhum arquivo.

Uso: python3 checar_consistencia.py [--sb DIR] [--lv DIR]

Níveis:
  ❌ falha bloqueante (código de saída 1)
  ⚠️ pendência aberta, registrada pelo próprio processo
  ❓ candidato que pede olhar humano (não é erro automático)
  ℹ️ informativo
"""
import argparse
import os
import re
import sys
import unicodedata

ESTADO = 'docs/handoff/estado-estrategico.md'
HIST = {'log.md'}  # histórico: menções antigas são esperadas
META_RE = re.compile(r'^decisoes/(plano-teste-processo|teste-processo-[^/]*)\.md$')
ORDER = [str(i) for i in range(67)] + ['epílogo']
TOK = re.compile(r'[^\W\d_]+')
MIDCAP = re.compile(r'(?:(?<=[^\W\d_] )|(?<=, ))([^\W\d_]+)')
BT = re.compile(r'`((?:Livro 1/|\.\./)?[^`\s]+\.md)`')
MDL = re.compile(r'\]\(([^)\s#]+\.md)(?:#[^)]*)?\)')
PH = re.compile(r'XX|AAAA|NN|capituloN|\$|\[|[*<>{}…]|\.\.\.')
GH = re.compile(r'\.github/[\w./-]+')
DEFORM = re.compile(r'[^\W\d_]\?[^\W\d_]')
INTENT = re.compile(r'nunca|não exist|nao exist|antig|migrad|histór|removid|ponteiro|não há', re.I)


def fold(s):
    s = unicodedata.normalize('NFD', s)
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn').lower().strip()


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def md_files(root):
    out = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in ('.git', 'node_modules')]
        for f in fn:
            if f.endswith('.md'):
                rel = os.path.relpath(os.path.join(dp, f), root)
                if not rel.startswith('docs/arquivo/'):  # skills arquivadas, fora de uso
                    out.append(rel)
    return sorted(out)


def sortkey(k):
    return ORDER.index(k) if k in ORDER else 999


def compact(keys):
    nums = sorted(int(k) for k in keys if k.isdigit())
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(str(nums[i]) if i == j else f'{nums[i]}–{nums[j]}')
        i = j + 1
    if any(not k.isdigit() for k in keys):
        out.append('epílogo')
    return ', '.join(out)


def fm_of(t):
    if t.startswith('---'):
        parts = t.split('---', 2)
        if len(parts) >= 3:
            return parts[1]
    return ''


def split_names(s):
    s = re.sub(r'[\[\]]', '', s)
    return {fold(x) for x in re.split(r'\s*(?:,|\+|/| e )\s*', s) if x.strip()}


def ficha_nome(k):
    return f'capitulo-{int(k):02d}.md' if k.isdigit() else 'epílogo'


# --- carregamento ------------------------------------------------------------

def parse_schedule(sb):
    t = read(os.path.join(sb, 'temas/esquema-l1.md'))
    m = re.search(r'## Progressão por Capítulo \(Escritos\)(.*?)(?=\n## )', t, re.S)
    if not m:
        sys.exit('não achei a tabela "Progressão por Capítulo" no esquema')
    rows, dups = {}, []
    for line in m.group(1).splitlines():
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 6 or cells[0] not in ORDER:
            continue
        if cells[0] in rows:
            dups.append(cells[0])
        rows[cells[0]] = cells
    return rows, dups


def livro_chapters(lv):
    d = os.path.join(lv, 'Livro 1')
    res = {}
    for f in os.listdir(d):
        m = re.fullmatch(r'capitulo(\d+)\.md', f)
        if m:
            res[str(int(m.group(1)))] = os.path.join(d, f)
        elif f == 'prologo.md':
            res['0'] = os.path.join(d, f)
        elif f == 'epilogo.md':
            res['epílogo'] = os.path.join(d, f)
    return res


def fichas(sb):
    d = os.path.join(sb, 'capitulos')
    res = {}
    for f in os.listdir(d):
        m = re.fullmatch(r'capitulo-(\d+)\.md', f)
        if m:
            res[str(int(m.group(1)))] = os.path.join(d, f)
    return res


def first_unrevised(lv):
    m = re.search(r'revisão manual, a partir do cap\. (\d+)', read(os.path.join(lv, ESTADO)))
    return int(m.group(1)) if m else None


def build_chars(sb):
    d = os.path.join(sb, 'personagens')
    return {fold(os.path.splitext(f)[0]) for f in os.listdir(d) if f.endswith('.md')}


def build_vocab(sb):
    v = set()
    for rel in md_files(sb):
        if META_RE.match(rel):
            continue
        v.update(fold(w) for w in TOK.findall(read(os.path.join(sb, rel))))
    return v


# --- verificações ------------------------------------------------------------

def check_ficha(k, path):
    t = read(path)
    nome = os.path.basename(path)
    msgs = []
    if 'type: Chapter' not in fm_of(t):
        msgs.append(('❌', f'{nome}: frontmatter sem "type: Chapter"'))
    heads = [fold(h) for h in re.findall(r'^##\s+(.+)$', t, re.M)]
    falta = []
    if not any(h.startswith('resumo') for h in heads):
        falta.append('Resumo')
    if not any(h.startswith('personagens') for h in heads):
        falta.append('Personagens')
    if not any(h.startswith('evento') for h in heads):
        falta.append('Eventos')
    if not any('semente' in h or 'conex' in h for h in heads):
        falta.append('Sementes/Conexões')
    if falta:
        msgs.append(('❌', f'{nome}: ingest incompleto, faltam seções: {", ".join(falta)}'))
    m = re.search(r'^## Pendências para o autor[ \t]*$(.*?)(?=^## |\Z)', t, re.M | re.S)
    npend = len(re.findall(r'^\s*- ', m.group(1), re.M)) if m else 0
    if npend:
        msgs.append(('⚠️', f'{nome}: {npend} pendência(s) aberta(s) para o autor'))
    elif m:
        msgs.append(('⚠️', f'{nome}: seção "Pendências para o autor" vazia (os itens podem ter ficado em outra seção)'))
    return msgs


def check_ingest(lvch, fich, fu):
    msgs, pend = [], []
    esperados = [k for k in lvch if k != 'epílogo' and fu and int(k) < fu]
    for k in sorted(set(lvch) | set(fich), key=sortkey):
        if k in fich and k not in lvch:
            msgs.append(('❌', f'{ficha_nome(k)} sem capítulo correspondente no livro'))
        if k in lvch and k not in fich:
            if k in esperados:
                msgs.append(('❌', f'cap. {k} revisado, mas sem ingest (falta capitulos/capitulo-{int(k):02d}.md)'))
            else:
                pend.append(k)
        if k in fich:
            msgs += check_ficha(k, fich[k])
    if pend:
        msgs.append(('ℹ️', f'sem ingest, por desenho (ainda em revisão ou epílogo): caps. {compact(pend)}'))
    ok = sum(1 for k in esperados if k in fich)
    return f'revisados com ingest: {ok}/{len(esperados)} (esperados: caps. 0 a {fu - 1 if fu else "?"})', msgs


def check_schedule(sched, dups, lvch, fich, chars):
    msgs = []
    for d in dups:
        msgs.append(('❌', f'linha duplicada no esquema: cap. {d}'))
    existentes = set(lvch) | set(fich)
    for k in sorted(existentes, key=sortkey):
        if k not in sched:
            msgs.append(('❌', f'cap. {k} sem linha no esquema'))
    for k in sorted(set(sched) & set(fich), key=sortkey):
        beat, pov = sched[k][1], sched[k][2]
        if 'sem entrada' in beat.lower():
            msgs.append(('⚠️', f'cap. {k}: esquema marca "{beat}" (entrada própria pendente)'))
        m = re.search(r'^pov:\s*(.+?)\s*$', fm_of(read(fich[k])), re.M)
        if not m:
            msgs.append(('❌', f'{ficha_nome(k)}: ficha sem campo pov'))
            continue
        for nome in split_names(m.group(1)):
            if nome not in chars:
                msgs.append(('❌', f'cap. {k}: POV "{nome}" na ficha não tem arquivo em personagens/'))
        if 'confirmar' not in pov.lower() and split_names(pov) != split_names(m.group(1)):
            msgs.append(('❌', f'cap. {k}: POV divergente, esquema "{pov}" × ficha "{m.group(1)}"'))
    conf = [k for k in sched if 'confirmar' in sched[k][2].lower()]
    if conf:
        msgs.append(('ℹ️', f'POV "a confirmar" no esquema: caps. {compact(conf)}'))
    recalc = [k for k in sched if 'recalcular' in sched[k][4].lower()]
    if recalc:
        msgs.append(('ℹ️', f'% Real "a recalcular" em {len(recalc)} linhas (caps. {compact(recalc)})'))
    return f'capítulos verificados: {len(existentes)}; linhas no esquema: {len(sched)}', msgs


def check_paths(sb, lv):
    msgs, n = [], 0
    for name, root, other in (('storybible', sb, lv), ('livro', lv, sb)):
        for rel in md_files(root):
            if rel in HIST or META_RE.match(rel):
                continue
            t = read(os.path.join(root, rel))
            for rx in (BT, MDL):
                for m in rx.finditer(t):
                    p = m.group(1)
                    if p.startswith('http') or p.startswith('.github/') or PH.search(p):
                        continue
                    n += 1
                    # bases: pasta do documento, raiz do próprio repo, raiz do outro repo,
                    # e a pasta-pai (docs escrevem "Livro/..." e "storybible/..." a partir dela)
                    bases = (os.path.dirname(os.path.join(root, rel)), root, other, os.path.dirname(root))
                    # caminho com "/" inicial é relativo à raiz do repositório
                    if any(os.path.isfile(os.path.normpath(os.path.join(b, p.lstrip('/')))) for b in bases):
                        continue
                    ln = t.count('\n', 0, m.start()) + 1
                    # registros de decisão são fotografias do momento: caminho antigo vira aviso
                    historico = rel.startswith(('decisoes/', 'insights/', 'ideias-rejeitadas/'))
                    nivel = '⚠️' if historico else '❌'
                    sufixo = ' (registro histórico)' if historico else ''
                    msgs.append((nivel, f'{name}/{rel}:{ln} cita `{p}`, que não existe{sufixo}'))
    return f'referências verificadas: {n}', msgs


def check_github(sb, lv):
    msgs, n = [], 0
    for name, root in (('storybible', sb), ('livro', lv)):
        for rel in md_files(root):
            if rel in HIST or META_RE.match(rel):
                continue
            for ln, line in enumerate(read(os.path.join(root, rel)).splitlines(), 1):
                for m in GH.finditer(line):
                    p = m.group(0).rstrip('.')
                    n += 1
                    if os.path.exists(os.path.join(root, p)):
                        continue
                    if INTENT.search(line):
                        msgs.append(('ℹ️', f'{name}/{rel}:{ln} menciona `{p}` (inexistente; contexto de histórico ou negação)'))
                    else:
                        msgs.append(('❌', f'{name}/{rel}:{ln} aponta para `{p}`, caminho antigo que não existe'))
    return f'ocorrências de .github/ verificadas: {n}', msgs


def check_integrity(sb, lv):
    """Letra?letra: o "?" substituindo acento indica texto corrompido."""
    msgs, n = [], 0
    for name, root in (('livro', lv), ('storybible', sb)):
        for rel in md_files(root):
            if META_RE.match(rel) or (name == 'livro' and not rel.startswith('Livro 1/')):
                continue
            hits = DEFORM.findall(read(os.path.join(root, rel)))
            if hits:
                n += len(hits)
                lvl = '❌' if name == 'livro' else 'ℹ️'
                msgs.append((lvl, f'{name}/{rel}: {len(hits)} "?" no lugar de letra (ex.: {", ".join(sorted(set(hits))[:4])})'))
    return f'ocorrências de "?" entre letras: {n}', msgs


def check_names(lv, vocab):
    d = os.path.join(lv, 'Livro 1')
    lower, caps = set(), {}
    for f in sorted(os.listdir(d)):
        if not f.endswith('.md'):
            continue
        t = read(os.path.join(d, f))
        lower.update(fold(w) for w in TOK.findall(t) if w[0].islower())
        for m in MIDCAP.finditer(t):
            w = m.group(1)
            if not w[0].isupper() or len(w) < 4:
                continue
            if t[m.end():m.end() + 1] == '?':  # fragmento de palavra corrompida: vai para a seção 0
                continue
            c = caps.setdefault(fold(w), [0, w, None])
            c[0] += 1
            if c[2] is None:
                ln = t.count('\n', 0, m.start()) + 1
                ctx = t[max(0, m.start() - 50):m.end() + 50].replace('\n', ' ')
                c[2] = f'{f}:{ln} "…{ctx}…"'
    cand = sorted((v for k, v in caps.items() if k not in vocab and k not in lower), key=lambda v: -v[0])
    msgs = [('❓', f'"{w}" ({c}×) não aparece em nenhum arquivo da storybible: {ctx}') for c, w, ctx in cand[:60]]
    if len(cand) > 60:
        msgs.append(('ℹ️', f'… e mais {len(cand) - 60} candidatos'))
    return f'nomes distintos no livro (maiúscula fora do início de frase): {len(caps)}', msgs


# --- principal ---------------------------------------------------------------

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--sb', default=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
    ap.add_argument('--lv', default=os.path.join(os.path.dirname(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))), 'Livro'))
    a = ap.parse_args()
    sb, lv = a.sb, a.lv

    sched, dups = parse_schedule(sb)
    lvch, fich = livro_chapters(lv), fichas(sb)
    fu = first_unrevised(lv)
    chars = build_chars(sb)
    vocab = build_vocab(sb)

    print('# Checklist de consistência storybible ↔ livro')
    print(f'storybible: {sb}')
    print(f'livro: {lv}')
    print(f'primeiro capítulo ainda não revisado (estado estratégico): cap. {fu}')
    print(f'capítulos no livro: {len(lvch)} | fichas em capitulos/: {len(fich)} | linhas no esquema: {len(sched)}')
    print()

    secoes = [
        ('0. Integridade do texto', *check_integrity(sb, lv)),
        ('1. Ingest (ficha por capítulo revisado)', *check_ingest(lvch, fich, fu)),
        ('2. Esquema (linhas e POV)', *check_schedule(sched, dups, lvch, fich, chars)),
        ('3. Caminhos citados (.md) que não existem', *check_paths(sb, lv)),
        ('4. Caminhos .github/ antigos', *check_github(sb, lv)),
        ('5. Nomes no livro fora da storybible', *check_names(lv, vocab)),
    ]
    totais = {'❌': 0, '⚠️': 0, '❓': 0, 'ℹ️': 0}
    for titulo, resumo, msgs in secoes:
        print(f'## {titulo}')
        print(f'verificados: {resumo}')
        if not any(n == '❌' for n, _ in msgs):
            print('✅ nenhum problema bloqueante')
        for nivel, texto in msgs:
            print(f'  {nivel} {texto}')
            totais[nivel] += 1
        print()
    print(f'Total: ❌ {totais["❌"]} | ⚠️ {totais["⚠️"]} | ❓ {totais["❓"]} | ℹ️ {totais["ℹ️"]}')
    return 1 if totais['❌'] else 0


if __name__ == '__main__':
    sys.exit(main())
