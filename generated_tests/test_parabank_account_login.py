"""Generated Playwright tests for the ParaBank account-login feature."""

import re

from playwright.sync_api import Page, expect


PARABANK_HOME_URL = "https://parabank.parasoft.com/parabank/index.htm"


def login(page: Page, username: str, password: str) -> None:
    """Submit the observed customer-login form."""
    page.goto(PARABANK_HOME_URL)
    page.locator('input[name="username"]').fill(username)
    page.locator('input[name="password"]').fill(password)
    page.get_by_role("button", name="Log In").click()


def test_successful_login_with_valid_credentials(page: Page) -> None:
    """A valid customer can reach Accounts Overview and see Log Out."""
    login(page, "john", "demo")

    expect(page).to_have_url(re.compile(r".*/overview\.htm$"))
    expect(page.get_by_role("heading", name="Accounts Overview")).to_be_visible()
    expect(page.get_by_role("link", name="Log Out")).to_be_visible()


def test_login_fails_with_invalid_credentials(page: Page) -> None:
    """Invalid credentials show the observed error and do not authenticate."""
    login(page, "john", "wrongpassword")

    expect(page).to_have_url(re.compile(r".*/login\.htm$"))
    expect(page.get_by_role("heading", name="Error!")).to_be_visible()
    expect(page.get_by_text("The username and password could not be verified.")).to_be_visible()
    expect(page.get_by_role("link", name="Log Out")).to_have_count(0)
