#!/usr/bin/env python3
"""Gera o bloco "Mapa da pasta" nos README e confere os links relativos.

Uso:
  python3 -I scripts/gerar-mapas-de-pasta.py [RAIZ] [--check] [pasta ...]

Sem pastas, processa as pastas de primeiro nível. O bloco fica entre
<!-- mapa-da-pasta:inicio --> e <!-- mapa-da-pasta:fim -->; o resto do README
nunca é alterado. --check só confere links e lista pastas sem README.
"""
import os, re, sys

M0, M1 = '<!-- mapa-da-pasta:inicio -->', '<!-- mapa-da-pasta:fim -->'
SKIP = {'.git', 'node_modules', '__pycache__'}


def desc(p):
    sk = os.path.join(p, 'SKILL.md')
    if os.path.exists(sk):
        m = re.search(r'^description:\s*(.+)$', open(sk, encoding='utf-8').read(), re.M)
        if m:
            return m.group(1).strip().strip('"\'')[:140]
    rd = os.path.join(p, 'README.md')
    if os.path.exists(rd):
        lines = [l.strip() for l in open(rd, encoding='utf-8') if l.strip()]
        for l in lines[1:]:
            if not l.startswith(('#', '-', '|', '<!--', '>')):
                return l[:140]
    return os.path.basename(p)


def title(p):
    for l in open(p, encoding='utf-8', errors='ignore'):
        l = l.strip()
        if l.startswith('#'):
            return re.sub('`', '', l.lstrip('# ')).strip()
    return os.path.basename(p)


def rows(d):
    out = []
    for e in sorted(os.listdir(d)):
        p = os.path.join(d, e)
        if e == 'README.md' or e in SKIP or e.startswith('.'):
            continue
        if os.path.isdir(p):
            has = os.path.exists(os.path.join(p, 'README.md'))
            n = sum(len(f) for _, _, f in os.walk(p))
            link = f'[`{e}/`](./{e}/README.md)' if has else f'`{e}/`'
            out.append(f'| {link} | {desc(p)} | {n} arquivo(s) |')
        elif e.endswith('.md'):
            out.append(f'| [`{e}`](./{e}) | {title(p)} | arquivo |')
        else:
            out.append(f'| [`{e}`](./{e}) | arquivo de apoio | arquivo |')
    return out


def apply(root, d):
    path = os.path.join(root, d)
    r = rows(path)
    f = os.path.join(path, 'README.md')
    if not r:
        return
    up = os.path.relpath(os.path.join(root, 'README.md'), path)
    blk = (f'{M0}\n## Mapa da pasta (`{d}/`)\n\n| Caminho | O que é | Tamanho |\n|---|---|---|\n'
           + '\n'.join(r) + f'\n\nVoltar ao [README raiz]({up}).\n{M1}\n')
    t = open(f, encoding='utf-8').read() if os.path.exists(f) else f'# {d}/\n'
    t = re.sub(re.escape(M0) + '.*?' + re.escape(M1) + '\n?', '', t, flags=re.S).rstrip('\n') + '\n\n' + blk
    open(f, 'w', encoding='utf-8').write(t)


def check(root):
    bad = 0
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP]
        if d != root and 'README.md' not in files and not os.path.relpath(d, root).startswith('skills/'):
            print('SEM README:', os.path.relpath(d, root))
        for f in files:
            if f.endswith('.md'):
                p = os.path.join(d, f)
                for m in re.findall(r'\]\((?!http|#|mailto)([^)\s#]+)', open(p, encoding='utf-8', errors='ignore').read()):
                    if not os.path.exists(os.path.normpath(os.path.join(d, m))):
                        bad += 1
                        print('LINK QUEBRADO:', os.path.relpath(p, root), '->', m)
    return bad


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    root = os.path.abspath(args[0]) if args else os.getcwd()
    folders = args[1:] or sorted(x for x in os.listdir(root) if os.path.isdir(os.path.join(root, x)) and x not in SKIP and not x.startswith('.'))
    if '--check' not in sys.argv:
        for x in folders:
            apply(root, x)
    sys.exit(1 if check(root) else 0)
