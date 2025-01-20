from playwright.sync_api import Locator, Page


class PublicApiPage:
    def __init__(self, page: Page):
        self.page = page

        self.api_title: Locator = page.locator(
            "xpath=(//div[contains(text(), 'API')])[2]"
        )
        self.generate_credentials_button: Locator = page.locator(
            "xpath=(//button[@name='button'])[2]"
        )
        self.api_key_text: Locator = page.locator(
            "xpath=(//div[@class='text-gray-900 text-sm font-normal leading-none'])[1]"
        )
        self.api_secret_key_text: Locator = page.locator(
            "xpath=(//div[@class='text-gray-900 text-sm font-normal leading-none'])[2]"
        )
        self.credentials_container: Locator = page.locator(
            "xpath=//div[@class='bg-white px-4 py-3 sm:flex sm:flex-col sm:px-6']"
        )
        self.credentials_container_close_button: Locator = page.locator(
            "xpath=//button[contains(@data-action,'#close')]"
        )
        self.credentials_card_options_button: Locator = page.locator(
            "xpath=(//button[contains(@data-action, '#toggle')])[8]"
        )
        self.credentials_card_delete_button: Locator = page.locator(
            "xpath=//div[contains(text(), 'Eliminar')]"
        )
        self.credentials_card_see_credentials_button: Locator = page.locator(
            "xpath=//div[contains(text(), 'Ver credenciales')]"
        )
        self.blank_state_title: Locator = page.locator(
            "xpath=//div[contains(text(), 'Aún no has creado una aplicación')]"
        )
        self.api_docs_link: Locator = page.locator(
            "xpath=(//a[contains(@href, 'api-docs')])[2]"
        )
