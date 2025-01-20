from playwright.sync_api import Page
import allure


def take_ss_and_attach(page: Page, name: str):
    png_bytes = page.screenshot(full_page=True)

    allure.attach(png_bytes, name, attachment_type=allure.attachment_type.PNG)
