"""
A module for new post page in the bdd.tests.acceptance.locators package.
"""

from selenium.webdriver.common.by import By


class NewPostPageLocators:
    NEW_POST_FORM: tuple[str, str] = (By.ID, "post-form")
    TITLE_FIELD: tuple[str, str] = (By.ID, "title")
    CONTENT_FIELD: tuple[str, str] = (By.ID, "content")
    SUBMIT_BUTTON: tuple[str, str] = (By.ID, "create-post")
