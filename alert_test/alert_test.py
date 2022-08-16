from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.acma.gov.au/blocked-gambling-websites#blocked-illegal-gambling-websites", timeout=0)

    page.locator("button:has-text(\"S-Z\")").click()
    page.locator("button:has-text(\"J-R\")").click()
    #
    # result = page.inner_text("//html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/main[1]"
    #                          "/div[2]/div[2]/article[1]/div[1]/div[2]/div[6]/div[1]/"
    #                          "div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/p[1]") == 'slotvibe.com'
    # assert result == "slotvibe.com"
    # # assert page.locator("//html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/main[1]/div["
    # #                     "2]/div[2]/article[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[5]/d"
    # #                     "iv[1]/div[2]/div[1]/div[1]/p[1]").input_value("slotvibe.com")
    text = page.locator("//html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/main[1]/div["
                          "2]/div[2]/article[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[5]/d"
                          "iv[1]/div[2]/div[1]/div[1]/p[1]").text_content()
    assert "slotvibe.com" in text
    # expect(page.locator(
    #     "//html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/main[1]/div[2]/div[2]/article[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/p[1]")) \
    #     .to_contain_text("slotvibe.com")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
