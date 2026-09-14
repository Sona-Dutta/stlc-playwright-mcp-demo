import re

from playwright.sync_api import Page, expect


BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"
USERNAME = "john"
PASSWORD = "demo"


def log_in_as_valid_customer(page: Page) -> None:
    page.goto(BASE_URL)
    username, password = page.get_by_role("textbox").all()
    username.fill(USERNAME)
    password.fill(PASSWORD)
    page.get_by_role("button", name="Log In").click()
    expect(page).to_have_url(re.compile(r".*/overview\.htm$"))
    expect(page.get_by_role("heading", name="Accounts Overview")).to_be_visible()


def test_transfer_funds_between_accounts(page: Page) -> None:
    try:
        log_in_as_valid_customer(page)
        page.get_by_role("link", name="Transfer Funds").click()
        expect(page.get_by_role("heading", name="Transfer Funds")).to_be_visible()

        page.get_by_role("textbox").fill("25")
        account_selectors = page.get_by_role("combobox")
        account_selectors.nth(1).select_option("12456")
        page.get_by_role("button", name="Transfer").click()

        expect(page.get_by_role("heading", name="Transfer Complete!")).to_be_visible()
        expect(page.get_by_text("$25.00 has been transferred from account #12345 to account #12456.")).to_be_visible()
    finally:
        page.close()


def test_account_overview_lists_accounts_and_total_balance(page: Page) -> None:
    try:
        log_in_as_valid_customer(page)
        page.get_by_role("link", name="Accounts Overview").click()
        expect(page.get_by_role("heading", name="Accounts Overview")).to_be_visible()

        overview_table = page.get_by_role("table")
        account_rows = overview_table.get_by_role("row").filter(has=page.get_by_role("link"))
        expect(account_rows.first).to_be_visible()
        assert account_rows.count() >= 1

        total_row = overview_table.get_by_role("row").filter(has=page.get_by_role("cell", name="Total"))
        expect(total_row).to_contain_text("Total")
        expect(total_row).to_contain_text(re.compile(r"\$-?\d+(?:\.\d{2})?"))
    finally:
        page.close()
