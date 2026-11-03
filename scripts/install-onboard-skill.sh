#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"
SOURCE_ROOT="$REPO_ROOT/skills/installable"
TARGET_ROOT="${HERMES_HOME:-${HOME}/.hermes}"

if [ ! -d "$SOURCE_ROOT" ]; then
  echo "ERRO: pasta de skills instaláveis não encontrada em: $SOURCE_ROOT" >&2
  exit 1
fi

installed=0
for dir in "$SOURCE_ROOT"/*/; do
  name="$(basename "$dir")"
  if [ ! -f "$dir/SKILL.md" ]; then
    echo "AVISO: $name sem SKILL.md, ignorada" >&2
    continue
  fi
  mkdir -p "$TARGET_ROOT/skills/$name"
  cp -f "$dir/SKILL.md" "$TARGET_ROOT/skills/$name/SKILL.md"
  echo "✓ $name -> $TARGET_ROOT/skills/$name"
  installed=$((installed + 1))
done

if [ "$installed" -eq 0 ]; then
  echo "ERRO: nenhuma skill instalada" >&2
  exit 1
fi

echo ""
echo "$installed skill(s) instalada(s)."
echo "Próximos passos:"
echo "1. no Hermes, rode /reload-skills (ou reinicie a sessão)"
echo "2. carregue a skill: /skill seutimeia-second-brain-onboard"
echo "3. diga: 'vamos montar o segundo cérebro'"
