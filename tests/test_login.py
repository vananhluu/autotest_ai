import json

from pages.login_page import LoginPage
from playwright.sync_api import Page, expect, Locator, TimeoutError

def test_login_success(login_page):
    login_page.open()
    login_page.login("valid_user")
