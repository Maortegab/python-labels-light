import os
from playwright.sync_api import Page
import allure
import pytest

from tasks.login_tasks import LoginTasks
from tasks.user.sidebar_tasks import SidebarTasks
from utils.decorators.tags_decorator import frontend_tags


@pytest.mark.sanity()
@pytest.mark.regression()
@frontend_tags(suite="Login")
@allure.title("Login Success")
def test_login_success(page: Page) -> None:
    login_tasks = LoginTasks(page)
    sidebar_tasks = SidebarTasks(page)

    login_tasks.navigate()
    login_tasks.login(os.environ["USER_EMAIL"], os.environ["USER_PASSWORD"])

    sidebar_tasks.validate_login_success()


@pytest.mark.sanity()
@pytest.mark.regression()
@frontend_tags(suite="Login")
@allure.title("Login Failed")
def test_login_failed(page: Page) -> None:
    login_tasks = LoginTasks(page)

    login_tasks.navigate()
    login_tasks.login(
        os.environ["USER_EMAIL_NOT_VALID"], os.environ["USER_PASSWORD_NOT_VALID"]
    )
    login_tasks.validate_login_failed()
