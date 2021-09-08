import pytest
from selenium import webdriver

capabilities_chrome = {
    "browserName": "chrome",
    "version": "92.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}
capabilities_firefox = {
    "browserName": "firefox",
    "version": "91.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nStart Google Chrome browser for test...")
        browser = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                   desired_capabilities=capabilities_chrome)
    elif browser_name == "firefox":
        print("\nStart Mozilla Firefox browser for test...")
        browser = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                   desired_capabilities=capabilities_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    print("\nStart browser for test...")
    yield browser
    print("\nQuit browser...")
    browser.quit()
