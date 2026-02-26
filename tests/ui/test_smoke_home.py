import pytest
from playwright.sync_api import sync_playwright
from src.config.settings import BASE_URL, HEADLESS


@pytest.mark.smoke
def test_home_page_opens():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        page = browser.new_page()
        page.goto(BASE_URL, wait_until="domcontentloaded")

        assert "Automation Exercise" in page.title()

        browser.close()
