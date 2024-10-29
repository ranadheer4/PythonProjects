from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#C:\\Users\\RanadheerDurgi\\git\\qa-automation2\\OLobby\\OLOBBYHYBRIDAUTOMATION\\Drivers\\chromedriver.exe
ser_obj=ChromeService(executable_path="C:\\Users\\RanadheerDurgi\\git\\qa-automation2\\OLobby\\OLOBBYHYBRIDAUTOMATION\\Drivers\\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.get("https://stage-refactor.credentialmydoc.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://nstarx.udemy.com/course/learn-selenium-automation-in-easy-python-language/learn/lecture/16964040#overview")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
print("Browser opened and closed success")
