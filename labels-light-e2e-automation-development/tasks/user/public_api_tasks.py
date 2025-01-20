import os
from playwright.sync_api import Page, expect
import allure

from pages.user.api_docs_page import ApiDocsPage
from pages.user.public_api_page import PublicApiPage
from utils.helpers.take_ss_and_attach import take_ss_and_attach


class PublicApiTasks:
    def __init__(self, page: Page):
        self.page = page

        self.public_api_page = PublicApiPage(page)

    @allure.step("Validate page")
    def check_public_api_page(self):
        expect(self.public_api_page.api_title).to_be_visible()

        take_ss_and_attach(self.page, name="public-api-view")

    @allure.step("Generate API credentials")
    def generate_credentials(self) -> None:
        if self.public_api_page.generate_credentials_button.is_visible():
            self.public_api_page.generate_credentials_button.click()

            expect(self.public_api_page.credentials_container).to_be_visible()

            self.public_api_page.credentials_container_close_button.click()

            take_ss_and_attach(self.page, name="credentials")
        else:
            self.public_api_page.credentials_card_options_button.click()
            self.public_api_page.credentials_card_delete_button.click()

            expect(self.public_api_page.blank_state_title).to_be_visible()

            self.public_api_page.generate_credentials_button.click()

            expect(self.public_api_page.credentials_container).to_be_visible()

            self.public_api_page.credentials_container_close_button.click()

            take_ss_and_attach(self.page, name="credentials")

    @allure.step("Delete API credentials")
    def delete_credentials(self) -> None:
        self.public_api_page.credentials_card_options_button.click()
        self.public_api_page.credentials_card_delete_button.click()

        expect(self.public_api_page.blank_state_title).to_be_visible()

        take_ss_and_attach(self.page, name="credentials-deleted")

    @allure.step("Make request")
    def generate_bearer_token(self) -> None:
        self.public_api_page.credentials_card_options_button.click()
        self.public_api_page.credentials_card_see_credentials_button.click()

        api_key = self.public_api_page.api_key_text.text_content().strip()
        api_secret_key = self.public_api_page.api_secret_key_text.text_content().strip()

        os.environ["API_KEY"] = api_key
        os.environ["API_SECRET_KEY"] = api_secret_key

        with self.page.context.expect_page() as new_page_info:
            self.public_api_page.api_docs_link.click()

        new_page = new_page_info.value

        api_docs_page = ApiDocsPage(new_page)

        new_page.wait_for_load_state("domcontentloaded")
        expect(api_docs_page.page_title).to_be_visible()

        api_docs_page.test_request_button.click()

        api_docs_page.client_id_input.type(os.getenv("API_KEY") or "")
        api_docs_page.client_secret_id_input.type(os.getenv("API_SECRET_KEY") or "")

        api_docs_page.generate_bearer_token_button.click()

        expect(api_docs_page.token_bearer_title).to_be_visible()

        take_ss_and_attach(new_page, name="api-docs")
