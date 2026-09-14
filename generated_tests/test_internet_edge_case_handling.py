"""Playwright coverage generated from the 'The Internet edge case handling' BDD feature."""

from playwright.sync_api import Page, expect

BASE_URL = "https://the-internet.herokuapp.com"


def test_dynamically_loaded_element_appears_after_clicking_start(page: Page) -> None:
    """Example 2 renders Hello World after Start is clicked."""
    page.goto(f"{BASE_URL}/dynamic_loading/2")

    page.get_by_role("button", name="Start").click()

    expect(page.get_by_text("Hello World!", exact=True)).to_be_visible(timeout=15000)


def test_accepting_a_javascript_alert_shows_handled_result(page: Page) -> None:
    """Accepting the JS alert displays its confirmation result."""
    page.goto(f"{BASE_URL}/javascript_alerts")
    page.once("dialog", lambda dialog: dialog.accept())

    page.get_by_role("button", name="Click for JS Alert").click()

    expect(page.get_by_text("You successfully clicked an alert", exact=True)).to_be_visible()


def test_first_checkbox_can_be_checked(page: Page) -> None:
    """The initially unchecked first checkbox can be toggled on."""
    page.goto(f"{BASE_URL}/checkboxes")
    first_checkbox = page.get_by_role("checkbox").first

    first_checkbox.check()

    expect(first_checkbox).to_be_checked()
