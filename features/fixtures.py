import pages
from behave import fixture
from selenium.webdriver import Chrome, ChromeOptions


def get_browser(context, *args, **kwargs):
    context.browser = Chrome(*args, **kwargs)
    context.main_page = pages.MainPage(driver=context.browser)
    yield context.browser
    context.browser.quit()


@fixture
def selenium_browser_chrome(context):
    """Run regular Chrome browser."""
    return next(get_browser(context))


@fixture
def selenium_browser_headless(context):
    """Run Chrome browser in headless mode."""
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")  # Fix running in Debian docker image
    options.add_argument("--window-size=1920x1080")
    return next(get_browser(context, options=options))
