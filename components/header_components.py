from playwright._impl._page import Page
from pages.base_page import BasePage

from pages.base_component import BaseComponentHeader
class HeaderComponent(BasePage, BaseComponentHeader):
    def __init__(self, page: Page):
        super().__init__(page)
        btnLogout = page.locator("#button-logout")

    def test_logout(self):
        self.test_click_icon_website()
        self.btnLogout.click()
