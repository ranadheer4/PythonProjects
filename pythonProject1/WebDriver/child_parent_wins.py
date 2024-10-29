import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By

ser_obj=ChromeService(executable_path="C:\\Users\\RanadheerDurgi\\git\\qa-automation2\\OLobby\\OLOBBYHYBRIDAUTOMATION\\Drivers\\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Click Here").click()
AllWins=driver.window_handles
time.sleep(3)
driver.switch_to.window(AllWins[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
time.sleep(3)
driver.switch_to.window(AllWins[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text