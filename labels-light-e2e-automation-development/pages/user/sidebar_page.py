import os
from playwright.sync_api import Locator, Page


class SidebarPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.email_text = page.locator(
            f"//div[contains(text(), '{os.environ["USER_EMAIL"]}')]"
        )
        self.admin_page_button: Locator = page.locator("css=#administrador")
        self.logout_button: Locator = page.locator(
            "xpath=(//button[@type='submit'])[1]"
        )
        self.connections_button: Locator = page.locator(
            "xpath=//div[@id='conexiones']//button"
        )
        self.public_api_button: Locator = page.locator(
            "xpath=//a[contains(@href, 'applications')]"
        )
        self.config_button: Locator = page.locator(
            "xpath=//div[@id='configuraciones']//button"
        )
        self.address_templates_button: Locator = page.locator(
            "xpath=(//a[contains(@href, 'address_templates')])[1]"
        )
