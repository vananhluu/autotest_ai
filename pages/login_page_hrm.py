import playwright

from core.base_page import BasePage
from playwright.sync_api import expect
import time
class LoginPageHRM(BasePage):
    URL = "https://hrm.anhtester.com/erp/login"
    Username = "#iusername"
    Password = "#ipassword"
    BtnLogin = "//button[contains(@class, 'btn-primary')]"

    def goto(self):
        browser = playwright.chromium.launch(headless=False)
        self._visit(self.URL)
    def login_with_account(self, username, password):
        self.goto()
        self._fill(self.Username, username)
        self._fill(self.Password, password)
        self._click(self.BtnLogin)
        time.sleep(10)