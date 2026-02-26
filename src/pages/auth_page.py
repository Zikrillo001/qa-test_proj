from src.core.base_page import BasePage


class AuthPage(BasePage):
    # Login form
    LOGIN_EMAIL = "input[data-qa='login-email']"
    LOGIN_PASSWORD = "input[data-qa='login-password']"
    LOGIN_BUTTON = "button[data-qa='login-button']"
    LOGIN_ERROR = "p:has-text('Your email or password is incorrect!')"

    # Signup form
    SIGNUP_NAME = "input[data-qa='signup-name']"
    SIGNUP_EMAIL = "input[data-qa='signup-email']"
    SIGNUP_BUTTON = "button[data-qa='signup-button']"
    SIGNUP_ERROR = "p:has-text('Email Address already exist!')"

    def login(self, email: str, password: str):
        self.page.fill(self.LOGIN_EMAIL, email)
        self.page.fill(self.LOGIN_PASSWORD, password)
        self.page.click(self.LOGIN_BUTTON)

    def signup(self, name: str, email: str):
        self.page.fill(self.SIGNUP_NAME, name)
        self.page.fill(self.SIGNUP_EMAIL, email)
        self.page.click(self.SIGNUP_BUTTON)

    def has_login_error(self) -> bool:
        return self.page.locator(self.LOGIN_ERROR).is_visible()

    def has_signup_error(self) -> bool:
        return self.page.locator(self.SIGNUP_ERROR).is_visible()
