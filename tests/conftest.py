import playwright
import pytest
from playwright.sync_api import Playwright
from pages.login_page import LoginPage

# 1. Page objectL LoginPage
@pytest.fixture
def login_page(page):
    return LoginPage(page)

# 2. Fixture perform login (optional if need to be already logged in)
@pytest.fixture
def logged_in_page(login_page):
    login_page.open()
    login_page.login("valid_user")
    return login_page

# Class scope
@pytest.fixture(scope="class")
def logged_in_class(request, browser):
    context = browser.new_context()
    page = context.new_page()