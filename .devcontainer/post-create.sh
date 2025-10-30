#!/usr/bin/env bash
set -euo pipefail

# Ensure apt is up-to-date and install Playwright browser dependencies
sudo apt-get update -y
sudo apt-get install -y \
  libatk1.0-0t64 libatk-bridge2.0-0t64 libcups2t64 libdrm2 libxkbcommon0 \
  libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2t64 libatspi2.0-0t64

# Set up Python virtual environment and install deps
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

# Install Playwright browsers
python -m playwright install

# Optional: small smoke check
python - <<'PY'
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://example.com")
    assert "Example" in page.title()
    context.close(); browser.close()
print("Playwright smoke check: OK")
PY

