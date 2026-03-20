from .BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # We intentionally use a 'broken' selector to test healing
        self.user_field = "[data-test='username-WRONG']"
        self.pass_field = "[data-test='password']"
        self.login_btn = "[data-test='login-button']"

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login_as_standard_user(self):
        # Pass a description so the AI knows what it is looking for
        self.fill_with_healing(self.user_field, "standard_user", "The login username input field")
        self.fill_with_healing(self.pass_field, "secret_sauce", "The login password input field")
        self.click_with_healing(self.login_btn, "The login submit button")