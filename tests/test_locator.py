from playwright.sync_api import Page, expect
import time
def test_login_success(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    time.sleep(10)
