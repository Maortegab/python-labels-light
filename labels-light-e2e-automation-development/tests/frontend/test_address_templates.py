import os
from playwright.sync_api import Page
import allure
import pytest

from tasks.login_tasks import LoginTasks
from tasks.user.address_templates_tasks import AddressTemplatesTasks
from tasks.user.sidebar_tasks import SidebarTasks
from utils.decorators.tags_decorator import frontend_tags


@pytest.fixture()
def setup(page: Page):
    login_tasks = LoginTasks(page)
    sidebar_tasks = SidebarTasks(page)

    login_tasks.navigate()
    login_tasks.login(os.environ["USER_EMAIL"], os.environ["USER_PASSWORD"])

    sidebar_tasks.validate_login_success()
    sidebar_tasks.click_config_button()
    sidebar_tasks.click_address_templates_button()

    yield page


@pytest.mark.sanity()
@pytest.mark.regression()
@frontend_tags(suite="Address Templates")
@allure.title("Address template creation")
def test_address_template_creation(setup: Page) -> None:
    address_templates_tasks = AddressTemplatesTasks(setup)

    address_templates_tasks.validate_page()
    address_templates_tasks.click_create_address_button()
    address_templates_tasks.fill_form()
    address_templates_tasks.validate_new_address_template()


@pytest.mark.sanity()
@pytest.mark.regression()
@frontend_tags(suite="Address Templates")
@allure.title("Delete address template")
def test_delete_address_template(setup: Page) -> None:
    address_templates_tasks = AddressTemplatesTasks(setup)

    address_templates_tasks.validate_page()
    address_templates_tasks.drop_address_template()
