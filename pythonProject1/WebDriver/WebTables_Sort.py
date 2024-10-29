import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By


ser_obj=ChromeService(executable_path="C:\\Users\\RanadheerDurgi\\git\\qa-automation2\\OLobby\\OLOBBYHYBRIDAUTOMATION\\Drivers\\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(5)
withoutSorted=[]
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
list_veg=driver.find_elements(By.XPATH,"//tbody/tr/td[1]")
for list_all in list_veg:
    withoutSorted.append(list_all.text)

print(len(list_veg))
orginal_sorted=withoutSorted.copy()
withoutSorted.sort()
assert withoutSorted == orginal_sorted
