# STLC Playwright MCP Demo

Target repository for the `test-executor` Foundry agent.

The agent commits one generated Playwright Python test per run to `generated_tests/test_*.py`
on a `test-executor-<short-uuid>` branch and opens a pull request. Opening the pull request
triggers the `Playwright tests` workflow, which installs Chromium and runs the generated test.

This repository intentionally contains no application code. The application under test is
external (https://parabank.parasoft.com).

## Layout

```text
.github/workflows/playwright-tests.yml   Runs generated tests on pull requests into main
generated_tests/                         Agent-generated Playwright tests land here
```
