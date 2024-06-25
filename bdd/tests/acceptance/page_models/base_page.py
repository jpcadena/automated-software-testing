"""
A module for base page in the bdd.tests.acceptance.page models package.
"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from bdd.tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver

    @property
    def url(self) -> str:
        return "http://127.0.0.1:5000"

    @property
    def title(self) -> WebElement:
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self) -> list[WebElement]:
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)
