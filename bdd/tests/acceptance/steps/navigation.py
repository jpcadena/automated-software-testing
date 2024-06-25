"""
A module for navigation in the bdd.tests.acceptance.steps package.
"""

import time
from typing import Any

from behave import given, then, use_step_matcher
from behave.runner import Context
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement

from bdd.tests.acceptance.page_models.blog_page import BlogPage
from bdd.tests.acceptance.page_models.home_page import HomePage
from bdd.tests.acceptance.page_models.new_post_page import NewPostPage

use_step_matcher("re")
options: Options = webdriver.Options()
options.add_argument("--incognito")
options.add_argument("--disable-extensions")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    " (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--password-store=basic")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--enable-automation")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-web-security")
options.add_argument("--disable-infobars")
options.add_argument("--disable-gpu")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-software-rasterizer")
options.add_argument("--proxy-server=IP_ADRESS:PORT")


@given("I am on the homepage")
def step_impl(
    context: Context, *args: tuple[Any, ...], **kwargs: dict[str, Any]
) -> None:
    context.driver = webdriver.WebDriver(options=options)
    context.driver.set_page_load_timeout(10)
    homepage: HomePage = HomePage(context.driver)
    context.driver.get(homepage.url)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


@given("I am on the blog page")
def step_impl(
    context: Context, *args: tuple[Any, ...], **kwargs: dict[str, Any]
) -> None:
    context.driver = webdriver.WebDriver(options=options)
    context.driver.set_page_load_timeout(10)
    homepage: BlogPage = BlogPage(context.driver)
    context.driver.get(homepage.url)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


@given("I am on the new post page")
def step_impl(
    context: Context, *args: tuple[Any, ...], **kwargs: dict[str, Any]
) -> None:
    context.driver = webdriver.WebDriver(options=options)
    context.driver.set_page_load_timeout(10)
    new_post_page: NewPostPage = NewPostPage(context.driver)
    context.driver.get(new_post_page.url)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


@then("I am on the blog page")
def step_impl(
    context: Context, *args: tuple[Any, ...], **kwargs: dict[str, Any]
) -> None:
    expected_url: str = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url
    time.sleep(5)


@then("I am on the homepage")
def step_impl(
    context: Context, *args: tuple[Any, ...], **kwargs: dict[str, Any]
) -> None:
    expected_url: str = HomePage(context.driver).url
    assert context.driver.current_url == expected_url
    time.sleep(5)


@then('I can see there is a post with title "(.*)" in the posts section')
def step_impl(context: Context, title: str) -> None:
    blog_page: BlogPage = BlogPage(context.driver)
    posts_with_title: list[WebElement] = [
        post for post in blog_page.posts if post.text == title
    ]
    assert posts_with_title
    assert all([post.is_displayed() for post in posts_with_title])
