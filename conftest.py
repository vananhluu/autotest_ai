import pytest
from playwright.sync_api import Playwright, ViewportSize


# Launch browser (headless = False)
@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, channel= "chrome")
    yield browser
    browser.close()
# Because when you login with account A, then access the website again,
# it may be in a logged in state -> could not test the case logging in with
# a different account -> need to create a fresh browser for each test
@pytest.fixture
def context(browser):
    context = browser.new_context(viewport=ViewportSize(width=1400, height=900))
    yield context
    context.close()

# After create a fresh browser for  each test -> need to create a new page object for each test
@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()