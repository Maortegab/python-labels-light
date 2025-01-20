from playwright.sync_api import Locator, Page

from utils.constants.text_pages import TextPages


class ApiDocsPage:
    def __init__(self, page: Page):
        self.page = page
        self.text_pages = TextPages()

        self.page_title: Locator = page.locator(
            f"xpath=//h1[contains(text(), '{self.text_pages.API_DOCS_TITLE}')]"
        )
        self.test_request_button = page.locator(
            "xpath=(//button[contains(text(), 'Probar')])[1]"
        )
        self.client_id_input: Locator = page.locator("css=#clientId")
        self.client_secret_id_input: Locator = page.locator("css=#clientSecret")
        self.generate_bearer_token_button: Locator = page.locator(
            "xpath=(//button[@type='button'])[2]"
        )
        self.token_bearer_title: Locator = page.locator(
            "xpath=//h3[contains(text(), 'Token Bearer')]"
        )
