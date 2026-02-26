from src.core.base_page import BasePage


class HomePage(BasePage):
    SIGNUP_LOGIN_LINK = "a[href='/login']"

    def open(self, base_url: str):
        self.page.goto(base_url, wait_until="domcontentloaded")
        return self

    def go_to_signup_login(self):
        self.page.click(self.SIGNUP_LOGIN_LINK)
