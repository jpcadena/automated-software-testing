"""
A module for interactions in the bdd.tests.acceptance.steps package.
"""

from behave import use_step_matcher, when
from behave.runner import Context
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

use_step_matcher("re")


@when('I click on the link with id "(.*)"')
def step_impl(context: Context, link_id: str) -> None:
    link: WebElement = context.driver.find_element(By.ID, link_id)
    link.click()
