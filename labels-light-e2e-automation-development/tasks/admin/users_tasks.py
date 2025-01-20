from typing import Dict, List
import re
from playwright.sync_api import Locator, Page

from pages.admin.users_page import UsersPage, UsersPageElements
from utils.helpers.take_ss_and_attach import take_ss_and_attach


class UsersTasks:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.users_page = UsersPage(page)

    def find_by_email(self, email: str) -> None:
        self.users_page.email_input_search.fill(email)
        self.users_page.email_button_search.click()

    def change_feature_flag_state(self, feature_flags: List[Dict[str, str]]):
        self.users_page.feature_flags_tab.click()
        
        for flag in feature_flags:
            ff: Locator = self.page.locator(
                UsersPageElements.get_feature_flag_by_value(flag["feature_flag"])
            )
            ff_current_state: Locator = self.page.locator(
                UsersPageElements.get_feature_flag_state(flag["feature_flag"])
            )

            current_state_text = ff_current_state.text_content()
            fixed_curr_state = re.sub(r"[^\x00-\x7F]+", "", current_state_text).strip()  # type: ignore

            assert (
                fixed_curr_state == flag["state"]
            ), f"Expected Feature Flag '{flag['feature_flag']}' state '{flag['state']}' but got '{fixed_curr_state}'"

            is_checked = ff.get_attribute("checked") is not None

            if (flag["action"] == "enable" and not is_checked) or (not flag["action"] == "enable" and is_checked):
                ff.click()

        self.users_page.feature_flags_save_button.click()

        take_ss_and_attach(self.page, name=f"feature flags setup: {feature_flags}")

    def setFeatureFlagsWith(self, feature_flags: List[Dict[str, str]]):
        self.change_feature_flag_state(feature_flags)
