import os
import pytest
import allure
from playwright.sync_api import Page

from tasks.login_tasks import LoginTasks
from tasks.user.sidebar_tasks import SidebarTasks
from utils.decorators.tags_decorator import frontend_tags


@pytest.mark.sanity()
@pytest.mark.regression()
@frontend_tags(suite="Logout")
@allure.title("Logout Success")
def test_logout_success(page: Page):
    login_tasks = LoginTasks(page)
    sidebar_tasks = SidebarTasks(page)

    login_tasks.navigate()
    login_tasks.login(os.environ["USER_EMAIL"], os.environ["USER_PASSWORD"])

    sidebar_tasks.validate_login_success()
    sidebar_tasks.click_logout_button()

    login_tasks.validate_logout()
