from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

URL = "https://en.wikipedia.org/wiki/2025_NFL_draft"


def fetch_rendered_html(
    url: str,
    wait_selector: str | None = None,
    wait_until: str = "load",
) -> str:
    """Use Playwright to render a page and return the final HTML.

    - wait_selector: optional CSS selector to wait for before capturing content.
      Handy for dynamic pages—e.g., a table or heading you rely on.
    - wait_until: readiness for navigation ("load", "domcontentloaded", "networkidle").
      Default is "load" which is sufficient for Wikipedia.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()
        response = page.goto(url, wait_until=wait_until)
        if not response or not response.ok:
            raise RuntimeError(
                f"Navigation failed: status={getattr(response, 'status', None)}"
            )
        if wait_selector:
            page.wait_for_selector(wait_selector, state="visible")

        html = page.content()
        context.close()
        browser.close()
        return html


html = fetch_rendered_html(URL, wait_selector="h1")
soup = BeautifulSoup(html, "html.parser")