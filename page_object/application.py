import allure
import pytest
from playwright.sync_api import Playwright


class Alert:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://www.acma.gov.au/blocked-gambling-websites#blocked-illegal-gambling-websites", timeout=0)

    def casino_check(self):
        self.page.locator("button:has-text(\"S-Z\")").click()
        self.page.locator("button:has-text(\"J-R\")").click()

    def check_result(self):
        return self.page.locator("//html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/main[1]/div["
                                 "2]/div[2]/article[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[5]/d"
                                 "iv[1]/div[2]/div[1]/div[1]/p[1]").is_visible("text='sl12otvibe.com'")

    def close(self):
        self.context.close()
        self.browser.close()
