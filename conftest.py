import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options

chrome_capabilities = {
    "browserName": "chrome",
    "browserVersion": "99.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language. ex: en")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name").lower()
    language = request.config.getoption("language").lower()
    chrome_options = Chrome_Options()
    firefox_options = Firefox_Options()
    browser = None
    if browser_name == "chrome":
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})

        # seleniumIntegrated
        # browser = webdriver.Chrome(options=chrome_options)

        # selenoidRemote
        browser = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                   desired_capabilities=chrome_capabilities,
                                   options=chrome_options)
    elif browser_name == "firefox":
        firefox_options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be 'chrome' or 'firefox'")
    browser.maximize_window()
    yield browser
    browser.quit()
