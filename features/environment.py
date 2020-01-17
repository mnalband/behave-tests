from behave import use_fixture
import fixtures

def before_all(context):
    use_fixture(fixtures.selenium_browser_headless, context)
