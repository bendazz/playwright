# Playwright tutorial (Python)

Learn Playwright — a fast, reliable headless browser automation library — using Python. This repo is a hands-on walkthrough with a tiny script and real tests you can run locally right now.

## Quick start

These commands set up an isolated Python environment, install Playwright and test tooling, download browsers, and run everything.

```bash
# 1) Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Download browsers (Chromium, Firefox, WebKit)
python -m playwright install

# 4) Run the example script (takes a screenshot to ./screenshots/home.png)
python scripts/basic_browse.py

# 5) Run the tests
pytest -q
```

Expected output: tests should pass, and you'll see a screenshot saved under `screenshots/home.png`.

## What’s in this repo

```
.
├─ scripts/
│  └─ basic_browse.py       # Minimal script: launch → navigate → assert → screenshot
├─ tests/
│  ├─ test_example.py       # Title assertion using the built-in page fixture
│  └─ test_locators.py      # Using accessible locators and URL assertion
├─ requirements.txt         # Python deps (playwright, pytest, pytest-playwright)
└─ README.md                # This tutorial
```

## Your first script, line by line

`scripts/basic_browse.py` demonstrates the core Playwright flow:

1) Start Playwright and launch a browser headlessly.
2) Create a fresh context and page (clean session).
3) Navigate, make an assertion, and save a screenshot.
4) Close cleanly.

Key ideas:
- Headless by default: great for CI and speed. Set `headless=False` when debugging locally.
- Deterministic waits: Playwright waits for navigation and element readiness under the hood.
- Clean isolation: new contexts avoid test flakiness due to shared state.

## Writing tests with pytest-playwright

The `pytest-playwright` plugin provides a ready‑to‑use `page` fixture so you can write tests like:

```python
def test_homepage_title(page):
		page.goto("https://playwright.dev")
		assert "Playwright" in page.title()
```

Another example using accessible locators and a URL check:

```python
def test_click_get_started(page):
		page.goto("https://playwright.dev")
		page.get_by_role("link", name="Get started").click()
		assert "docs/intro" in page.url
```

Run them with:

```bash
pytest -q
```

### Headed mode and debugging

Run tests with a visible browser window and slow‑mo for easier debugging:

```bash
pytest --headed --slowmo 300
```

Or temporarily change the script to `p.chromium.launch(headless=False)`.

### Tracing and diagnostics

Record a trace to debug failures visually:

```bash
# Run tests and record traces for all tests
pytest --tracing on

# After the run, open the trace viewer (replace path with actual output)
python -m playwright show-trace test-results/<test-name>/trace.zip
```

Playwright also supports videos and screenshots per test via context options.

## Locator best practices

- Prefer role-based and accessible locators: `get_by_role()`, `get_by_label()`, `get_by_placeholder()`.
- Use `locator()` with stable attributes or test IDs rather than brittle CSS selectors.
- Avoid text selectors if the copy is likely to change, unless you control the content.

Examples:

```python
page.get_by_role("button", name="Submit").click()
page.get_by_label("Email").fill("user@example.com")
page.get_by_test_id("cart-count").text_content()
```

## Running in CI

Playwright is designed for CI. Since browsers are installed via `python -m playwright install`, add that step to your CI job before running tests. On Ubuntu you may need OS packages for headless browsers (this container already installs them):

```bash
sudo apt-get update
sudo apt-get install -y libatk1.0-0t64 libatk-bridge2.0-0t64 libcups2t64 libdrm2 libxkbcommon0 \
	libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2t64 libatspi2.0-0t64
```

## Prefer JavaScript/TypeScript instead?

The concepts are identical. If you later want the Node version:

```bash
npm init -y
npm i -D @playwright/test
npx playwright install
npx playwright test
```

The test API looks very similar (`test`, `expect`, `page` fixtures).

---

Happy testing! If you’d like, we can extend this with API testing, file uploads, downloads, tracing-by-default, or a GitHub Actions workflow.