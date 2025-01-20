import pytest
from playwright.sync_api import Page
from dotenv import load_dotenv


def pytest_configure():
    load_dotenv()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "viewport": {"width": 1920, "height": 1080}}

