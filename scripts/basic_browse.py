from pathlib import Path
from playwright.sync_api import sync_playwright


def run() -> None:
    screenshots_dir = Path("screenshots")
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        # Navigate to the Wikipedia page for the 2025 NFL Draft
        page.goto("https://en.wikipedia.org/wiki/2025_NFL_draft")

        # Assert on the page title (typically "2025 NFL Draft - Wikipedia")
        title = page.title()
        assert "2025 NFL" in title and "Wikipedia" in title
        print(f"Page title: {title}")

        # Additionally, assert the main heading text for robustness
        heading_text = page.get_by_role("heading", name="2025 NFL Draft").text_content()
        # Wikipedia's displayed casing is usually "2025 NFL draft" (lowercase d), so compare case-insensitively
        assert heading_text and "2025 nfl draft" in heading_text.lower()
        print(f"Main heading: {heading_text}")

        # Save a screenshot of the page
        page.screenshot(path=str(screenshots_dir / "wikipedia_2025_nfl_draft.png"))

        context.close()
        browser.close()


if __name__ == "__main__":
    run()
