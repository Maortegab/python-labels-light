import os
import re
from playwright.sync_api import expect, Page
import allure

from pages.user.quotation_page import QuotationPage
from utils.helpers.take_ss_and_attach import take_ss_and_attach


class QuotationTasks:
    def __init__(self, page: Page):
        self.page = page

        self.quotation_page = QuotationPage(page)

    @allure.step("Enter postal codes")
    def type_postal_codes(
        self, postal_code_origin: str, postal_code_destiny: str
    ) -> None:
        expect(self.quotation_page.page_title_text).to_be_visible()

        self.quotation_page.postal_code_origin_input.type(postal_code_origin)
        self.page.locator(
            f"(//span[contains(text(), '{postal_code_origin}')])[1]"
        ).click()

        self.quotation_page.postal_code_destiny_input.type(postal_code_destiny)
        self.page.locator(
            f"(//span[contains(text(), '{postal_code_destiny}')])[1]"
        ).click()

        take_ss_and_attach(self.page, name="Type postal codes")

    @allure.step("Enter package dimensions")
    def type_package_dimensions(
        self,
        length: str = "10",
        width: str = "10",
        height: str = "10",
        weight: str = "1",
    ):
        self.quotation_page.package_length_input.type(length)
        self.quotation_page.package_width_input.type(width)
        self.quotation_page.package_height_input.type(height)
        self.quotation_page.package_weight_input.type(weight)

        take_ss_and_attach(self.page, name="Type package dimensions")

    @allure.step("Click quote button")
    def click_quote_button(self):
        self.quotation_page.quote_button.click()

    @allure.step("Validate rates")
    def validate_rates(self):
        expect(self.quotation_page.total_rates_text).to_be_visible(
            timeout=int(os.environ["RATES_TIMEOUT"])
        )

        total_rates_string = re.search(
            r"\d+", self.quotation_page.total_rates_text.text_content() or ""
        )

        if total_rates_string:
            total_rates_number = int(total_rates_string.group())

            total_rates_in_container = self.quotation_page.rates_container.locator(
                ":scope > *"
            ).count()

            assert int(total_rates_number) == total_rates_in_container

            take_ss_and_attach(self.page, name="rates")

    @allure.step("Make quotation")
    def make_quotation(
        self,
        postal_code_origin: str,
        postal_code_destiny: str,
        length: str = "10",
        width: str = "10",
        height: str = "10",
        weight: str = "1",
    ):
        self.type_postal_codes(postal_code_origin, postal_code_destiny)
        self.type_package_dimensions(length, width, height, weight)
        self.click_quote_button()
        self.validate_rates()
