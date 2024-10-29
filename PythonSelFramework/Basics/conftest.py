import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setUp(request):
    #To get browserkey value
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        ser_obj = ChromeService(executable_path="C:\\Users\\RanadheerDurgi\\git\\qa-automation2\\OLobby\\OLOBBYHYBRIDAUTOMATION\\Drivers\\chromedriver.exe")
        driver = webdriver.Chrome(executable_path="C:\\Users\\RanadheerDurgi\\git\\qa-automation2\\OLobby\\OLOBBYHYBRIDAUTOMATION\\Drivers\\chromedriver.exe")
    elif browser_name=="firefox":
        ser_obj = ChromeService(executable_path="C:\\Users\\RanadheerDurgi\\git\\qa-automation2\\OLobby\\OLOBBYHYBRIDAUTOMATION\\Drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=ser_obj)
    elif browser_name=="IE":
        ser_obj = ChromeService(executable_path="C:\\Users\\RanadheerDurgi\\git\\qa-automation2\\OLobby\\OLOBBYHYBRIDAUTOMATION\\Drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=ser_obj)

    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    print(driver.title)
    driver.close()


