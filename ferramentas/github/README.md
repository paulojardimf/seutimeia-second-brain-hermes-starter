# GitHub

## Papel
Fonte canônica da memória operacional versionada.

## Uso típico
- hospedar o segundo cérebro
- publicar playbooks e skills sanitizadas
- versionar diário, contexto e projetos
- manter espelhos de `AGENTS.md`, `CLAUDE.md`, `CHANGELOG.md`

## Credenciais e segurança
- token fica em `~/.hermes/.env`
- não colocar PAT, SSH key, cookie ou secret no repositório
- preferir push canônico: `status` → `add` → `commit` → `pull --rebase` → `push`

## O que documentar
- repositório canônico
- política de branches
- padrão de commit
- o que pode virar repo público e o que deve permanecer privado
