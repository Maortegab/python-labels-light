from playwright.sync_api import Locator, Page


class SidebarPage:
    def __init__(self, page: Page) -> None:
        self.users_page_button: Locator = page.locator(
            "xpath=//div/a[contains(@href, '/users')]"
        )
