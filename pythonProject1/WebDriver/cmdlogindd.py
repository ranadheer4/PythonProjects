import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

ser_obj=ChromeService(executable_path="C:\\Users\\RanadheerDurgi\\git\\qa-automation2\\OLobby\\OLOBBYHYBRIDAUTOMATION\\Drivers\\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.get("https://stage-refactor.credentialmydoc.com/");
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@formcontrolname='email']").send_keys("ctg@credentialmydoc.com")
driver.find_element(By.XPATH,"//input[@formcontrolname='credential']").send_keys("ctgadmin2018")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='Close']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[text()='ADD TASK ']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//ctg-create-task//ng-select[@placeholder='Select Payer']//input").send_keys("AARP Health Care Options")
time.sleep(2)
Payers=driver.find_elements(By.XPATH,"//div[@class='ng-option ng-star-inserted']/input")
print(len(Payers))
time.sleep(2)
for country in Payers:
    if country.text=="AARP Health Care Options":
        country.click()
        break


print(driver.find_element(By.XPATH,"//ctg-create-task//ng-select[@placeholder='Select Payer']//input").text)
