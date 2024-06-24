"""
A module for base page in the bdd.tests.acceptance.locators package.
"""

from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE: tuple[str, str] = (
        By.TAG_NAME,
        "h1",
    )
