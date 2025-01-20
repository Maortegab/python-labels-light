from playwright.sync_api import expect, Page
import allure

from pages.user.sidebar_page import SidebarPage
from utils.helpers.take_ss_and_attach import take_ss_and_attach


class SidebarTasks:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.sidebar_page = SidebarPage(page)

    @allure.step("Validate login success")
    def validate_login_success(self):
        expect(self.sidebar_page.email_text).to_be_visible()

        take_ss_and_attach(self.page, name="login-success")

    @allure.step("Click admin page button")
    def click_admin_button(self):
        self.sidebar_page.admin_page_button.click()

    @allure.step("Click logout button")
    def click_logout_button(self):
        self.sidebar_page.logout_button.click()

        take_ss_and_attach(self.page, name="click-logout-button")

    @allure.step("Click connections button")
    def click_connections_button(self) -> None:
        self.sidebar_page.connections_button.click()

    @allure.step("Click public api button")
    def click_public_api_button(self) -> None:
        self.sidebar_page.public_api_button.click()

    @allure.step("Click config button")
    def click_config_button(self) -> None:
        self.sidebar_page.config_button.click()

    @allure.step("Click address templates button")
    def click_address_templates_button(self) -> None:
        self.sidebar_page.address_templates_button.click()
