import os
import pytest
from playwright.sync_api import Page
import allure

from tasks.login_tasks import LoginTasks
from tasks.user.public_api_tasks import PublicApiTasks
from tasks.user.sidebar_tasks import SidebarTasks
from utils.decorators.tags_decorator import frontend_tags


@pytest.fixture
def setup(page: Page):
    login_tasks = LoginTasks(page)
    sidebar_tasks = SidebarTasks(page)

    login_tasks.navigate()
    login_tasks.login(os.environ["USER_EMAIL"], os.environ["USER_PASSWORD"])

    sidebar_tasks.validate_login_success()
    sidebar_tasks.click_connections_button()
    sidebar_tasks.click_public_api_button()

    yield page


@pytest.mark.sanity()
@pytest.mark.regression()
@frontend_tags(suite="Public Api")
@allure.title("Credential Generation Success")
def test_credential_generation_success(setup: Page) -> None:
    public_api_tasks = PublicApiTasks(setup)

    public_api_tasks.check_public_api_page()
    public_api_tasks.generate_credentials()


@pytest.mark.sanity()
@pytest.mark.regression()
@frontend_tags(suite="Public Api")
@allure.title("Delete Credentials Success")
def test_delete_credentials_success(setup: Page) -> None:
    public_api_tasks = PublicApiTasks(setup)

    public_api_tasks.check_public_api_page()
    public_api_tasks.delete_credentials()


@pytest.mark.sanity()
@pytest.mark.regression()
@frontend_tags(suite="Public Api")
@allure.title("Generate Bearer Token From Api Docs")
def test_public_api_response_success(setup: Page) -> None:
    public_api_tasks = PublicApiTasks(setup)

    public_api_tasks.check_public_api_page()
    public_api_tasks.generate_credentials()
    public_api_tasks.generate_bearer_token()
