"""
A module for content in the bdd.tests.acceptance.steps package.
"""

from typing import Any

from behave import step, then, use_step_matcher
from behave.runner import Context

from bdd.tests.acceptance.page_models.base_page import BasePage

use_step_matcher("re")


@then("There is a title shown on the page")
def step_impl(
    context: Context, *args: tuple[Any, ...], **kwargs: dict[str, Any]
) -> None:
    base_page: BasePage = BasePage(context.driver)
    assert base_page.title.is_displayed()


@step('The title tag has content "(.*)"')
def step_impl(context: Context, content: str) -> None:
    base_page: BasePage = BasePage(context.driver)
    assert base_page.title.text == content
