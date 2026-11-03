# GitHub

## Papel
Fonte canônica da memória operacional versionada.

## Uso típico
- hospedar o segundo cérebro
- publicar playbooks e skills sanitizadas
- versionar diário, contexto e projetos
- manter o `CHANGELOG.md` e a documentação técnica dos projetos

## Credenciais e segurança
- a credencial fica no cofre da empresa ou no `.env` do Hermes, nunca no repositório
- não colocar PAT, SSH key, cookie ou secret no repositório
- preferir push canônico: `status` → `add` → `commit` → `pull --rebase` → `push`

## O que documentar
- repositório canônico
- política de branches
- padrão de commit
- o que pode virar repo público e o que deve permanecer privado
