from playwright.sync_api import Page, expect


BASE_URL = "https://the-internet.herokuapp.com"


def test_dynamic_loading_example_2_reveals_hello_world(page: Page) -> None:
    """Verify the dynamically rendered element becomes visible after Start."""
    page.goto(f"{BASE_URL}/dynamic_loading/2")

    page.get_by_role("button", name="Start").click()

    expect(page.get_by_role("heading", name="Hello World!")).to_be_visible()


def test_accepting_javascript_alert_reports_handled_result(page: Page) -> None:
    """Verify accepting the JavaScript alert produces the expected result."""
    page.goto(f"{BASE_URL}/javascript_alerts")
    page.once("dialog", lambda dialog: dialog.accept())

    page.get_by_role("button", name="Click for JS Alert").click()

    expect(page.get_by_text("You successfully clicked an alert")).to_be_visible()


def test_first_checkbox_can_be_checked(page: Page) -> None:
    """Verify the first checkbox can be checked."""
    page.goto(f"{BASE_URL}/checkboxes")
    first_checkbox = page.get_by_role("checkbox").first

    first_checkbox.check()

    expect(first_checkbox).to_be_checked()
