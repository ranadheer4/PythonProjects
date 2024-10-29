import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

ser_obj=ChromeService(executable_path="C:\\Users\\RanadheerDurgi\\PycharmProjects\\pythonProject1\\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()
products_list=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
print(len(products_list))

for all_prdcts in products_list:
    all_items=all_prdcts.find_element(By.XPATH,"div/h4").text
    print(all_items)
    if all_items=="Blackberry":
        all_prdcts.find_element(By.XPATH,"div/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("Ind")
my_wait=WebDriverWait(driver,10)
my_wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
my_msg=driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
assert "Thank you! Your order" in my_msg
