import os
import pytest
from playwright.sync_api import Page
import pandas as pd
import allure

from tasks.admin.users_tasks import UsersTasks
from tasks.login_tasks import LoginTasks
from tasks.user.quotation_tasks import QuotationTasks
from tasks.user.sidebar_tasks import SidebarTasks as SidebarUserTasks
from tasks.admin.sidebar_tasks import SidebarTasks as SidebarAdminTasks
from utils.decorators.tags_decorator import frontend_tags

init_flags = [
    {"feature_flag": "quotation_card_v3", "state": "Opt Out", "action": "enable"},
    {"feature_flag": "shipping_history_v2", "state": "Beta", "action": "enable"},
]


@pytest.mark.sanity()
@frontend_tags(suite="Feature Flags")
@allure.title("Feature Flags Setup")
def test_feature_flags_setup(page: Page) -> None:
    login_tasks = LoginTasks(page)
    sidebar_user_tasks = SidebarUserTasks(page)
    sidebar_admin_tasks = SidebarAdminTasks(page)
    users_tasks = UsersTasks(page)

    login_tasks.navigate()
    login_tasks.login(os.environ["ADMIN_EMAIL"], os.environ["ADMIN_PASSWORD"])

    sidebar_user_tasks.click_admin_button()

    sidebar_admin_tasks.click_users_button()

    users_tasks.find_by_email(os.environ["USER_EMAIL"])
    users_tasks.setFeatureFlagsWith(init_flags)


@pytest.mark.sanity()
@pytest.mark.regression()
@frontend_tags(suite="Quotation")
@allure.title("Quotation Success")
def test_quotation(page: Page) -> None:
    login_tasks = LoginTasks(page)
    sidebar_tasks = SidebarUserTasks(page)
    quotation_tasks = QuotationTasks(page)

    login_tasks.navigate()
    login_tasks.login(os.environ["USER_EMAIL"], os.environ["USER_PASSWORD"])

    sidebar_tasks.validate_login_success()

    quotation_tasks.make_quotation("64000", "06000")


@pytest.mark.regression()
@frontend_tags(suite="Quotation")
@allure.title("Quotation Massive Success")
def test_quotation_massive(page: Page) -> None:
    login_tasks = LoginTasks(page)
    sidebar_tasks = SidebarUserTasks(page)
    quotation_tasks = QuotationTasks(page)

    login_tasks.navigate()
    login_tasks.login(os.environ["USER_EMAIL"], os.environ["USER_PASSWORD"])

    sidebar_tasks.validate_login_success()

    dataframe = pd.read_csv(f"{os.getcwd()}/data/archives/postal_codes.csv")

    for index, row in dataframe.iterrows():
        quotation_tasks.make_quotation(
            str(row["postal_code_origin"]),
            str(row["postal_code_destiny"]),
            str(row["length"]),
            str(row["width"]),
            str(row["height"]),
            str(row["weight"]),
        )

        page.reload()
