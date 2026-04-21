import json

from pages.login_page import LoginPage
from playwright.sync_api import Page, expect, Locator, TimeoutError

def test_login_success(page):
    login_page = LoginPage(page)
    # login_page.login_with_account("admin_example", "123456")

    with open("data/credentials.json") as f:
        creds = json.load(f)[0]
    valid = creds["valid_user"]
    locked = creds["locked_user"]
    login_page.open()
    login_page.login(valid['username'],valid["password"])

