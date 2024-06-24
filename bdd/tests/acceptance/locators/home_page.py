"""
A module for home page in the bdd.tests.acceptance.locators package.
"""

from selenium.webdriver.common.by import By

from bdd.tests.acceptance.locators.base_page import BasePageLocators


class HomePageLocators(BasePageLocators):
    NAVIGATION_LINK: tuple[str, str] = (By.ID, "blog-link")
