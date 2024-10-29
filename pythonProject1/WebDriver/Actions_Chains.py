import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By

ser_obj=ChromeService(executable_path="C:\\Users\\RanadheerDurgi\\git\\qa-automation2\\OLobby\\OLOBBYHYBRIDAUTOMATION\\Drivers\\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action=ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()

#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
time.sleep(2)
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
time.sleep(2)
