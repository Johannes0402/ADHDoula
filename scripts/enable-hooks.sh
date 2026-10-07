#!/bin/sh
# Zet de pre-commit hook van deze repo aan (eenmalig per clone).
# Zie README.md, sectie Pre-commit hook.
cd "$(dirname "$0")/.." || exit 1
git config core.hooksPath scripts/git-hooks
echo "core.hooksPath staat op scripts/git-hooks"
