import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By

ser_obj=ChromeService(executable_path="C:\\Users\\RanadheerDurgi\\git\\qa-automation2\\OLobby\\OLOBBYHYBRIDAUTOMATION\\Drivers\\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")
time.sleep(2)
red=driver.find_elements(By.XPATH,"//div[@class='products']/div")

count=len(red)

assert count>0
for res in red:
    res.find_element(By.XPATH,"div/button").click()

time.sleep(5)
driver.find_element(By.XPATH,"//a//img[@alt='Cart']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//div/button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Apply']").click()
time.sleep(2)
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
time.sleep(5)
#Sum validation
totalAmnt=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum=0
for prices in totalAmnt:

    sum=sum+int(prices.text)

print(sum)
tp=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == tp

distotal=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert distotal < tp
print("Sucess")
#assert sum == tp