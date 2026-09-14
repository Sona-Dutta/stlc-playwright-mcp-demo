"""Generated Playwright coverage for the ParaBank account-login feature."""

from playwright.sync_api import Page, expect


PARABANK_URL = "https://parabank.parasoft.com/parabank/"


def test_parabank_customer_login_form_is_available(page: Page) -> None:
    """Verify that the ParaBank landing page exposes the customer login controls."""
    page.goto(PARABANK_URL, wait_until="domcontentloaded")

    expect(page).to_have_title("ParaBank | Welcome | Online Banking")
    expect(page.get_by_role("heading", name="Customer Login")).to_be_visible()
    expect(page.locator('input[name="username"]')).to_be_visible()
    expect(page.locator('input[name="password"]')).to_be_visible()
    expect(page.get_by_role("button", name="Log In")).to_be_visible()
