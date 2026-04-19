#!/bin/bash
set -euo pipefail

# Only run in Claude Code remote (web) sessions
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Pull latest changes from the working branch
git fetch origin
git pull origin "$(git rev-parse --abbrev-ref HEAD)" --ff-only || true

# Install poppler-utils for pdftotext (PDF reading in papers/)
if ! command -v pdftotext &>/dev/null; then
  apt-get install -y -q poppler-utils 2>/dev/null || true
fi
