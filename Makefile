# Simple helpers to use the venv without manual activation

VENV = .venv
PY = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest

.PHONY: setup browsers run test clean

setup:
	python3 -m venv $(VENV)
	$(PY) -m pip install --upgrade pip
	$(PIP) install -r requirements.txt

browsers:
	$(PY) -m playwright install

run:
	$(PY) scripts/scrape_parse.py

test:
	$(PYTEST) -q

clean:
	rm -rf $(VENV) artifacts screenshots __pycache__ .pytest_cache
