from playwright.sync_api import Page, expect
import re, time

def test_check_title_google(page: Page):
    print("Navigate to google page")
    page.goto("https://www.google.com/")
    assert "google" in page.title()
    time.sleep(5)