"""
A module for blog page in the bdd.tests.acceptance.page models package.
"""

from selenium.webdriver.remote.webelement import WebElement

from bdd.tests.acceptance.locators.blog_page import BlogPageLocators
from bdd.tests.acceptance.page_models.base_page import BasePage


class BlogPage(BasePage):
    @property
    def url(self) -> str:
        return f"{super().url}/blog"

    @property
    def posts_section(self) -> WebElement:
        return self.driver.find_element(*BlogPageLocators.POSTS_SECTION)

    @property
    def posts(self) -> list[WebElement]:
        return self.driver.find_elements(*BlogPageLocators.POST)

    @property
    def add_post_link(self) -> WebElement:
        return self.driver.find_element(*BlogPageLocators.ADD_POST_LINK)
