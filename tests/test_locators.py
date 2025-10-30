from playwright.sync_api import Page


def test_click_get_started(page: Page) -> None:
    page.goto("https://playwright.dev")
    page.get_by_role("link", name="Get started").click()
    assert "docs/intro" in page.url
