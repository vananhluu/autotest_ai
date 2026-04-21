from playwright.sync_api import Page
class BaseComponentHeader:
    # Chưa nhung action chung
    def __init__(self, page: Page):
        self.page = page
        self.logo = page.locator("#")
        self.accSettin = page.locator("#accSettin")
    def test_click_icon_website(self):
        self.logo.click()