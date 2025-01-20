from playwright.sync_api import Page

from pages.admin.sidebar_page import SidebarPage


class SidebarTasks:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.sidebar_page = SidebarPage(page)

    def click_users_button(self):
        self.sidebar_page.users_page_button.click()
