from playwright.sync_api import Locator, Page

class UsersPageElements:
    EMAIL_BUTTON_SEARCH = 'input[type="submit"]'
    EMAIL_INPUT_SEARCH = "id=email_or_id"
    FEATURE_FLAGS_SAVE_BUTTON = 'xpath=//button[@name="button"]'
    FEATURE_FLAGS_TAB = "id=tab-feature_flags"

    @staticmethod
    def get_feature_flag_by_value(value):
        return f'//input[@value="{value}"]'

    @staticmethod
    def get_feature_flag_state(value):
        return f'xpath=//input[@value="{value}"]/following::span[1]'
    

class UsersPage:
    def __init__(self, page: Page) -> None:
        self.page: Page = page

        self.email_button_search: Locator = page.locator(
            UsersPageElements.EMAIL_BUTTON_SEARCH
        )
        self.email_input_search: Locator = page.locator(
            UsersPageElements.EMAIL_INPUT_SEARCH
        )

        self.feature_flags_save_button: Locator = page.locator(
            UsersPageElements.FEATURE_FLAGS_SAVE_BUTTON
        )

        self.feature_flags_tab: Locator = page.locator(
            UsersPageElements.FEATURE_FLAGS_TAB
        )
