import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
"""@pytest.fixture()
def setup():
    global driver
    # options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    return driver
"""
@pytest.fixture()     #ranadheer_durgi
def setUp():
    driver = webdriver.Chrome()
    #driver.get("https://opensource-demo.orangehrmlive.com/")
    #driver.maximize_window()

    yield
    driver.close()


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    elif browser=='Edge':
        driver = webdriver.Edge()
        print("Launching edge browser........")
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")
    return driver

