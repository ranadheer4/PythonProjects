
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setUp")
class TestOne(BaseClass):
    def teste2ee(self):


        """self.driver.find_element(By.ID, "autosuggest").send_keys("ind")
        time.sleep(2)
        Countries = self.driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
        print(len(Countries))
        for country in Countries:
            if country.text == "India":
                country.click()

        time.sleep(2)
        print("Country is selected")
        # print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))
        assert self.driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
"""