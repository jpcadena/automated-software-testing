"""
A module for blog page in the bdd.tests.acceptance.locators package.
"""

from selenium.webdriver.common.by import By


class BlogPageLocators:
    ADD_POST_LINK: tuple[str, str] = By.ID, "add-post-link"
    POSTS_SECTION: tuple[str, str] = By.ID, "posts"
    POST: tuple[str, str] = By.CLASS_NAME, "post-link"
