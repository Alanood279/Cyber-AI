#!/data/data/com.termux/files/usr/bin/bash
# Collect and clean data sources

cd "$(dirname "$0")/.."
python -m crawler.crawler
