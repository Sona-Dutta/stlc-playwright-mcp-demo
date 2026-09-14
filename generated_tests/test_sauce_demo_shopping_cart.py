import re

from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"
STANDARD_USERNAME = "standard_user"
LOCKED_OUT_USERNAME = "locked_out_user"
PASSWORD = "secret_sauce"


def login(page: Page, username: str, password: str) -> None:
    page.goto(BASE_URL)
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()


def test_login_with_valid_credentials_shows_products_page(page: Page) -> None:
    login(page, STANDARD_USERNAME, PASSWORD)

    expect(page).to_have_url(re.compile(r".*inventory\.html"))
    expect(page.get_by_text("Products", exact=True)).to_be_visible()


def test_add_sauce_labs_backpack_updates_cart_badge(page: Page) -> None:
    login(page, STANDARD_USERNAME, PASSWORD)
    expect(page).to_have_url(re.compile(r".*inventory\.html"))

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    expect(page.get_by_role("button", name="Cart, 1 items")).to_be_visible()


def test_locked_out_user_sees_locked_out_error(page: Page) -> None:
    login(page, LOCKED_OUT_USERNAME, PASSWORD)

    expect(page.get_by_role("alert")).to_contain_text(
        "Sorry, this user has been locked out."
    )
