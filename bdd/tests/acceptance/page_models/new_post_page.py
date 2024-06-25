"""
A module for new post page in the bdd.tests.acceptance.page models package.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from bdd.tests.acceptance.locators.new_post_page import NewPostPageLocators
from bdd.tests.acceptance.page_models.base_page import BasePage


class NewPostPage(BasePage):
    @property
    def url(self) -> str:
        return f"{super().url}/post"

    @property
    def form(self) -> WebElement:
        return self.driver.find_element(*NewPostPageLocators.NEW_POST_FORM)

    @property
    def submit_button(self) -> WebElement:
        return self.driver.find_element(*NewPostPageLocators.SUBMIT_BUTTON)

    def form_field(self, name: str) -> WebElement:
        return self.form.find_element(By.NAME, name)
