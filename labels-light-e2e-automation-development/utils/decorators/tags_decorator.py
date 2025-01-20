from functools import wraps
import allure
from allure_commons.types import Severity


def frontend_tags(suite: str):
    def decorator(func):
        @allure.parent_suite("Frontend")
        @allure.suite(suite)
        @allure.tag(suite)
        @allure.severity(Severity.CRITICAL)
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


def backend_tags(suite: str):
    def decorator(func):
        @allure.parent_suite("Backend")
        @allure.suite(suite)
        @allure.tag(suite)
        @allure.severity(Severity.CRITICAL)
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator
