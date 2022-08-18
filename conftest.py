from pytest import fixture
from playwright.sync_api import sync_playwright
from page_object.application import AlertSz
from page_object.application import AlertJr


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def australia_check_zoome(get_playwright):
    zoome_check = AlertSz(get_playwright)
    yield zoome_check
    zoome_check.close()


@fixture
def australia_check_oxi(get_playwright):
    oxi_check = AlertJr(get_playwright)
    yield oxi_check
    oxi_check.close()
