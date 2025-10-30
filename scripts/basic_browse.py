from pathlib import Path
from playwright.sync_api import sync_playwright


def run() -> None:
    screenshots_dir = Path("screenshots")
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        page.goto("https://playwright.dev")
        title = page.title()
        assert "Playwright" in title
        print(f"Page title: {title}")

        page.screenshot(path=str(screenshots_dir / "home.png"))

        context.close()
        browser.close()


if __name__ == "__main__":
    run()
