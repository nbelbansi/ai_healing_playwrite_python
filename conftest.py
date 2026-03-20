import pytest
from playwright.sync_api import Browser
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# --- Existing Fixtures ---
@pytest.fixture(scope="function")
def browser_context(browser: Browser):
    context = browser.new_context(viewport={'width': 1280, 'height': 720})
    yield context
    context.close()

# --- Updated Reporting Hooks for pytest-html 4.0+ ---

def pytest_html_report_title(report):
    """Sets the title for the HTML report (New Version Syntax)."""
    report.title = "AI-Augmented Quality Engineering Report"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # We use 'extras' to add the AI Healing badge to the report
    extras = getattr(report, "extra", [])

    if report.when == "call":
        # We check the test's captured stdout/stderr for our AI success message
        if "AI SUCCESS" in report.caplog or "AI HEALER" in report.caplog:
            import pytest_html
            extras.append(pytest_html.extras.html(
                '<div style="background-color: #e8f5e9; border-left: 6px solid #2e7d32; padding: 10px;">'
                '<strong>🤖 AI Healing:</strong> This test was automatically recovered by Llama 3.3.'
                '</div>'
            ))
        report.extra = extras