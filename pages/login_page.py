from .base_page import BasePage
from playwright.async_api import expect
class LoginPage(BasePage):
    url = "https://hrm.anhtester.com/erp/login"
    username = "#iusername"
    password = "#ipassword"
    BtnLogin = "//button[contains(@class, 'btn-primary')]"