"""Generated Playwright tests for the TodoMVC task-management BDD scenarios."""

from playwright.sync_api import Page, expect


TODO_URL = "https://demo.playwright.dev/todomvc/#/"
TODO_TEXT = "buy milk"


def add_todo(page: Page, text: str) -> None:
    """Add a todo using the observed TodoMVC input."""
    new_todo = page.get_by_role("textbox", name="What needs to be done?")
    new_todo.fill(text)
    new_todo.press("Enter")


def todo_item(page: Page, text: str):
    """Return the task list item matching the supplied todo text."""
    return page.get_by_role("listitem").filter(has_text=text)


def test_add_a_new_todo_item(page: Page) -> None:
    """Scenario: Add a new todo item."""
    page.goto(TODO_URL)

    add_todo(page, TODO_TEXT)

    expect(todo_item(page, TODO_TEXT)).to_be_visible()
    expect(page.get_by_text("1 item left", exact=True)).to_be_visible()


def test_complete_a_todo_item(page: Page) -> None:
    """Scenario: Complete a todo item."""
    page.goto(TODO_URL)
    add_todo(page, TODO_TEXT)

    toggle = todo_item(page, TODO_TEXT).get_by_role("checkbox", name="Toggle Todo")
    toggle.check()

    expect(toggle).to_be_checked()
    expect(page.get_by_text("0 items left", exact=True)).to_be_visible()


def test_clear_completed_todos(page: Page) -> None:
    """Scenario: Clear completed todos."""
    page.goto(TODO_URL)
    add_todo(page, TODO_TEXT)
    todo_item(page, TODO_TEXT).get_by_role("checkbox", name="Toggle Todo").check()

    page.get_by_role("button", name="Clear completed").click()

    expect(page.get_by_role("listitem")).to_have_count(0)
