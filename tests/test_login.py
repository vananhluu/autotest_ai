from pages.login_page import LoginPage
from playwright.sync_api import Page, expect, Locator, TimeoutError

def test_login_success(page):
    login_page = LoginPage(page)
    login_page.login_with_account("admin_example", "123456")