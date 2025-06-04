#!/bin/sh
# Simple helper to switch README language
# Usage: ./switch_readme.sh [en|ja]
case "$1" in
  en)
    cp README.en.md README.md
    ;;
  ja)
    cp README.ja.md README.md
    ;;
  *)
    echo "Usage: $0 [en|ja]"
    exit 1
    ;;
esac
