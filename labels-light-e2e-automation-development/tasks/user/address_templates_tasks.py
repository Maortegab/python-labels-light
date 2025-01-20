from faker import Faker
from playwright.sync_api import expect, Page
import allure

from pages.user.address_templates_page import AddressTemplatesPage
from utils.helpers.take_ss_and_attach import take_ss_and_attach


class AddressTemplatesTasks:
    def __init__(self, page: Page):
        self.page = page
        self.postal_code: str = "64000"
        self.faker = Faker("es_MX")

        self.address_templates_page = AddressTemplatesPage(page)

    @allure.step("Validate address templates page")
    def validate_page(self):
        expect(self.address_templates_page.page_title).to_be_visible()

        take_ss_and_attach(self.page, name="Address Templates Page")

    @allure.step("Click create address button")
    def click_create_address_button(self) -> None:
        self.address_templates_page.create_address_button.click()

    @allure.step("Fill form")
    def fill_form(self) -> None:
        self.address_templates_page.street_input.type(f"{self.faker.street_address()}")
        self.address_templates_page.postal_code_input.type(self.postal_code)
        self.address_templates_page.get_postal_code_option(self.postal_code).click()
        self.address_templates_page.reference_input.last.type("Puerta negra")
        self.address_templates_page.name_input.last.type(
            f"{self.faker.first_name()} {self.faker.last_name()}"
        )
        self.address_templates_page.phone_input.last.type(self.faker.phone_number())
        self.address_templates_page.email_input.last.type(self.faker.email())
        self.address_templates_page.alias_input.last.type(self.faker.random_element())

        take_ss_and_attach(self.page, name="Form filled")

        self.address_templates_page.save_button.last.click()

    @allure.step("Validate new address template")
    def validate_new_address_template(self) -> None:
        self.address_templates_page.there_is_at_least_one_template()

        take_ss_and_attach(self.page, name="New address template")

    @allure.step("Delete address template")
    def drop_address_template(self) -> None:
        self.address_templates_page.address_template_card_options.first.click()
        self.address_templates_page.address_template_card_delete_button.first.click()
        self.address_templates_page.address_template_confirm_delete_button.click()

        expect(
            self.address_templates_page.address_template_blank_state_title
        ).to_be_visible()

        take_ss_and_attach(self.page, name="Delete address template")
