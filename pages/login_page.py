import json
import time

from core.base_page import BasePage
# from pages.login_page_hrm import LoginPage
# from pages.login_page import LoginPage
from playwright.sync_api import Page, expect, Locator, TimeoutError

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def load_credentials(self, user_type: str):
        with open("data/credentials.json","r") as file:
            return json.load(file)[0][user_type]

    def open(self):
        self.page.goto(self.URL)
        self._take_screenshot("open_login_page.png")

    def login(self, user_type: str):
        creds = self.load_credentials(user_type)
        self.username.fill(creds["username"])
        self.password.fill(creds["password"])
        self.login_button.click()
        time.sleep(5)
        self._take_screenshot("after_login.png")



