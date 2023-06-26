import allure
import pytest
from playwright.sync_api import Playwright


class AlertSz:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False, slow_mo=500)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://www.acma.gov.au/blocked-gambling-websites#blocked-illegal-gambling-websites", timeout=0)

    def casino_check(self):
        self.page.locator("button:has-text(\"S-Z\")").click()
        self.page.locator("button:has-text(\"J-R\")").click()

    # Zoome check
    def check_result_sz(self):
        textsz = self.page.locator("//html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/main[1]/div["
                                   "2]/div[2]/article[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[5]/d"
                                   "iv[1]/div[2]/div[1]/div[1]/p[1]").text_content()
        return ["zoome3.casino", "zoome.casino", "thezoome.com"] not in textsz

    def close(self):
        self.context.close()
        self.browser.close()


class AlertJr:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://www.acma.gov.au/blocked-gambling-websites#blocked-illegal-gambling-websites", timeout=0)

    def casino_check(self):
        self.page.locator("button:has-text(\"S-Z\")").click()
        self.page.locator("button:has-text(\"J-R\")").click()

    # Oxi test
    def check_result_jr(self):
        textjr = self.page.locator("//html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/main[1]/div[2]/div[2]/article[1]/div"
                                   "[1]/div[2]/div[6]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/p[1]") \
            .text_content()
        return ["oxi.casino", "oxi1.casino"] not in textjr

    def close(self):
        self.context.close()
        self.browser.close()
