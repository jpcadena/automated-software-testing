"""
A module for home page in the bdd.tests.acceptance.page models package.
"""

from selenium.webdriver.remote.webelement import WebElement

from bdd.tests.acceptance.locators.home_page import HomePageLocators
from bdd.tests.acceptance.page_models.base_page import BasePage


class HomePage(BasePage):
    @property
    def url(self) -> str:
        return f"{super().url}/"

    @property
    def blog_link(self) -> WebElement:
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)
