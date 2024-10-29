from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj=ChromeService(executable_path="C:\\Users\\RanadheerDurgi\\git\\qa-automation2\\OLobby\\OLOBBYHYBRIDAUTOMATION\\Drivers\\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME,"name").send_keys("Ranadheer")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("ranadurgi3@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Password']").send_keys("9963883545Durgi")
driver.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
dd=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dd.select_by_visible_text("Female")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
mess=driver.find_element(By.CLASS_NAME,"alert-success").text
print(mess)
assert "success" in mess