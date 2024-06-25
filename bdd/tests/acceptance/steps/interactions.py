"""
A module for interactions in the bdd.tests.acceptance.steps package.
"""

from behave import use_step_matcher, when
from behave.runner import Context
from selenium.webdriver.remote.webelement import WebElement

from bdd.tests.acceptance.page_models.base_page import BasePage
from bdd.tests.acceptance.page_models.new_post_page import NewPostPage

use_step_matcher("re")


@when('I click on the "(.*)" link')
def step_impl(context: Context, link_text: str) -> None:
    base_page: BasePage = BasePage(context.driver)
    links: list[WebElement] = base_page.navigation
    if matching_links := [link for link in links if link.text == link_text]:
        matching_links[0].click()
    else:
        raise RuntimeError


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context: Context, content: str, field_name: str) -> None:
    new_post_page: NewPostPage = NewPostPage(context.driver)
    new_post_page.form_field(field_name).send_keys(content)


@when("I press the submit button")
def step_impl(context: Context) -> None:
    new_post_page: NewPostPage = NewPostPage(context.driver)
    new_post_page.submit_button.click()
