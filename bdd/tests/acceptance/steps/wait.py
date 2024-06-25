"""
A module for wait in the bdd.tests.acceptance.steps package.
"""

from typing import Any

from behave import given, use_step_matcher
from behave.runner import Context
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from bdd.tests.acceptance.locators.blog_page import BlogPageLocators

use_step_matcher("re")


@given("I wait for the posts to load")
def step_impl(
    context: Context, *args: tuple[Any, ...], **kwargs: dict[str, Any]
) -> None:
    try:
        WebDriverWait(context.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                BlogPageLocators.POSTS_SECTION
            )
        )
        print("Posts section is visible.")
    except TimeoutException as e:
        print("TimeoutException: Element not found within the specified time.")
        print("Page Source:", context.driver.page_source[:500])
        raise e
