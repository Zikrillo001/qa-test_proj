import sys
from pathlib import Path
import os
from datetime import datetime

import pytest
from playwright.sync_api import sync_playwright

# project root: .../automationexercise
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.config.settings import BASE_URL, HEADLESS, BROWSER  # noqa: E402


@pytest.fixture(scope="session")
def base_url():
    # plugin base_url fixture’ni override qilamiz (shuning uchun endi '' bo‘lmaydi)
    return BASE_URL


def _get_browser(p, name: str):
    name = (name or "chromium").lower()
    if name == "firefox":
        return p.firefox
    if name == "webkit":
        return p.webkit
    return p.chromium


@pytest.fixture()
def page():
    # Sync API: event loop running bo'lmasa ishlaydi (quyida pytest.ini bilan buni kafolatlaymiz)
    with sync_playwright() as p:
        browser_type = _get_browser(p, BROWSER)
        browser = browser_type.launch(headless=HEADLESS)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # fail bo'lsa screenshot saqlash
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("reports/screenshots", exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            name = f"{item.name}_{ts}.png"
            path = os.path.join("reports", "screenshots", name)
            page.screenshot(path=path, full_page=True)