import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By

ser_obj=ChromeService(executable_path="C:\\Users\\RanadheerDurgi\\git\\qa-automation2\\OLobby\\OLOBBYHYBRIDAUTOMATION\\Drivers\\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
expect_list=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actualList=[]
driver.find_element(By.XPATH,"//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")
time.sleep(2)
red=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=print(len(red))


for list in red:
    actualList.append(list.find_element(By.XPATH,"h4").text)

assert expect_list == actualList














