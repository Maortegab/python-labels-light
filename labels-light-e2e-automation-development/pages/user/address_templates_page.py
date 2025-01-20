from playwright.sync_api import expect, Locator, Page

from utils.constants.text_pages import TextPages


class AddressTemplatesPage:
    def __init__(self, page: Page):
        self.page = page
        self.text_pages = TextPages()

        self.page_title: Locator = page.locator(
            f"xpath=(//h1[contains(text(), '{self.text_pages.ADDRESS_TEMPLATES_TITLE}')])[1]"
        )
        self.create_address_button: Locator = page.locator(
            "xpath=(//button[@data-controller='drawer--drawer-component'])[1]"
        )
        self.street_input: Locator = page.locator("css=#street1_from_address")
        self.postal_code_input: Locator = page.locator("css=#postal_code_from_")
        self.reference_input: Locator = page.locator(
            "css=#address_template_address_attributes_reference"
        )
        self.name_input: Locator = page.locator(
            "css=#address_template_address_attributes_name"
        )
        self.phone_input: Locator = page.locator(
            "css=#address_template_address_attributes_phone"
        )
        self.email_input: Locator = page.locator(
            "css=#address_template_address_attributes_email"
        )
        self.alias_input: Locator = page.locator("css=#address_template_alias_name")
        self.save_button: Locator = page.locator(
            "xpath=//button[contains(text(), 'Guardar')]"
        )
        self.children_addreses_container: Locator = page.locator(
            "xpath=//div[contains(@id, 'addreses_container')]/./*"
        )
        self.address_template_card_options: Locator = page.locator(
            "xpath=//button[contains(@class, 'dropdown_address')]"
        )
        self.address_template_card_delete_button: Locator = page.locator(
            "xpath=//div[contains(text(), 'Eliminar')]"
        )
        self.address_template_confirm_delete_button: Locator = page.locator(
            "xpath=//button[contains(text(), 'Sí, eliminar')]"
        )
        self.address_template_blank_state_title: Locator = page.locator(
            "xpath=//h3[contains(text(), 'Aún no tienes direcciones guardadas')]"
        )

    def get_postal_code_option(self, postal_code: str) -> Locator:
        xpath = f"xpath=(//span[contains(text(), '{postal_code}')])[1]"

        return self.page.locator(xpath)

    def there_is_at_least_one_template(self) -> bool:
        expect(self.children_addreses_container).to_have_count(1)
