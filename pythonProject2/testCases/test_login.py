import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
class Test_001_Login:

    baseURL = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"
    def test_homePageTitle(self,setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "OangeHRM":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_homePageTitle.png")
            self.driver.close()
            assert False
    def test_login(self,setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        time.sleep(3)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_Login.png")
            self.driver.close()
            assert False

