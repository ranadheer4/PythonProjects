import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class vup(unittest.TestCase):
    def test_Login(self):
        self.driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://env-app.olobby.com/")
        print("Tittle pf page"+self.driver.title)