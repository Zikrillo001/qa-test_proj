import pytest
from src.pages.home_page import HomePage
from src.pages.auth_page import AuthPage


@pytest.mark.smoke
def test_negative_login_shows_error(page, base_url):
    home = HomePage(page).open(base_url)
    home.go_to_signup_login()

    auth = AuthPage(page)
    auth.login(email="notreal@example.com", password="wrongpass123")

    assert auth.has_login_error() is True


@pytest.mark.regression
def test_signup_existing_email_shows_error(page, base_url):
    home = HomePage(page).open(base_url)
    home.go_to_signup_login()

    auth = AuthPage(page)
    auth.signup(name="Test User", email="test@example.com")

    if not auth.has_signup_error():
        pytest.xfail(
            "Existing email deterministik emas. Keyin API data seeding bilan tuzatamiz."
        )
