#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"
SOURCE_DIR="$REPO_ROOT/skills/installable/seutimeia-second-brain-onboard"
TARGET_ROOT="${HERMES_HOME:-${HOME}/.hermes}"
TARGET_DIR="$TARGET_ROOT/skills/seutimeia-second-brain-onboard"

if [ ! -f "$SOURCE_DIR/SKILL.md" ]; then
  echo "ERRO: skill de onboarding não encontrada em: $SOURCE_DIR" >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"
cp -f "$SOURCE_DIR/SKILL.md" "$TARGET_DIR/SKILL.md"

echo "✓ Skill instalada em: $TARGET_DIR"
echo ""
echo "Próximos passos:"
echo "1. abra uma nova conversa no Hermes dentro deste diretório clonado"
echo "2. rode /reload-skills (ou reinicie a sessão, se necessário)"
echo "3. carregue a skill: /skill seutimeia-second-brain-onboard"
echo "4. diga: 'vamos iniciar meu second brain'"
