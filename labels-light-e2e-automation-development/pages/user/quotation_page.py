from playwright.sync_api import Page


class QuotationPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.page_title_text = page.locator(
            "xpath=(//div[contains(text(), 'Cotizar y crear envío')])[1]"
        )
        self.postal_code_origin_input = page.locator(
            "xpath=(//input[@name='postal_code_to'])[1]"
        )
        self.postal_code_destiny_input = page.locator(
            "xpath=(//input[@name='postal_code_to'])[2]"
        )
        self.package_length_input = page.locator("css=#parcel_length")
        self.package_width_input = page.locator("css=#parcel_width")
        self.package_height_input = page.locator("css=#parcel_height")
        self.package_weight_input = page.locator("css=#parcel_weight")
        self.quote_button = page.locator("xpath=//input[@value='Cotizar']")
        self.total_rates_text = page.locator("css=#filter-bar-span")
        self.loader_rate_container = page.locator(
            "xpath=//div[contains(@id, 'loader')]"
        )
        self.rates_container = page.locator(
            "xpath=(//div[contains(@id, 'quotation_') and contains(@id, '_new_rate')])[1]"
        )
