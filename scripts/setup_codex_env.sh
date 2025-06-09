#!/bin/bash
# Simple setup script for Codex development
set -e

pip install -r requirements.txt
pre-commit install

echo "Codex environment is ready"
