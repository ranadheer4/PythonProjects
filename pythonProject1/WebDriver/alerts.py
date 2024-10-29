import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By
name="ranadheer"
ser_obj=ChromeService(executable_path="C:\\Users\\RanadheerDurgi\\git\\qa-automation2\\OLobby\\OLOBBYHYBRIDAUTOMATION\\Drivers\\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys(name)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
time.sleep(2)
alert=driver.switch_to.alert
alt=alert.text
print(alt)

assert name in alt
alert.accept()
