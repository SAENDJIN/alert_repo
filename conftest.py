from pytest import fixture
from playwright.sync_api import sync_playwright
from page_object.application import Alert


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def australia_check_oxi(get_playwright):
    zoome_check = Alert(get_playwright)
    yield zoome_check
    zoome_check.close()
