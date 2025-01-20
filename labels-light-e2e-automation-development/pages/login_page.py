from playwright.sync_api import Locator, Page, expect


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page: Page = page

        self.user_email_input: Locator = page.locator("css=#user_email")
        self.user_password_input: Locator = page.locator("css=#user_password")
        self.sign_in_button: Locator = page.locator("css=#sign-in-button")
        self.login_failed_alert: Locator = page.locator("css=#toast-alert")
        self.login_title_text: Locator = page.locator(
            "xpath=//div[contains(text(), 'Inicia sesión')]"
        )
