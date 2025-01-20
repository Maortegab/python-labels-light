import os
from playwright.sync_api import Page, expect
import allure

from pages.login_page import LoginPage
from utils.helpers.take_ss_and_attach import take_ss_and_attach


class LoginTasks:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.login_page = LoginPage(page)

    @allure.step("Open browser and navigate to app")
    def navigate(self) -> None:
        self.page.goto(os.environ["BASE_URL"])

        take_ss_and_attach(self.page, name="navigate")

    @allure.step("Enter credentials and try login")
    def login(self, email: str, password: str) -> None:
        self.login_page.user_email_input.type(email)
        self.login_page.user_password_input.type(password)

        self.login_page.user_email_input.click()

        expect(self.login_page.sign_in_button).to_be_enabled()

        self.login_page.sign_in_button.click()

    @allure.step("Validate if login failed")
    def validate_login_failed(self) -> None:
        expect(self.login_page.login_failed_alert).to_be_visible()

        take_ss_and_attach(self.page, name="login-failed")

    @allure.step("Validate logout success")
    def validate_logout(self) -> None:
        expect(self.login_page.login_title_text).to_be_visible()

        take_ss_and_attach(self.page, name="logout-success")
