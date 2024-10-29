import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('launch chrome browser')
def launchBrowser(context):
    #context.driver=webdriver.Chrome(executable_path="C:\\Users\\RanadheerDurgi\\Downloads\\chromedriver_win32 \\chromedriver.exe")
    context.driver=webdriver.Chrome()

@when('open orange hrm homepage')
def openHomepage(context):
    context.driver.get("https://stage-refactor.credentialmydoc.com/")
    context.driver.find_element(By.XPATH, "//input[@formcontrolname='email']").send_keys("ctg@credentialmydoc.com")
    time.sleep(2)
    context.driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("ctgadmin2018")
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()

@then('verify that the logo present on page')
def verifyLogo(context):
    expected_title=context.driver.find_element(By.TAG_NAME,"title")
    assert expected_title=="CredentialMyDoc - Credentialing and Provider Enrollment Made Easy"
    True

@then('close browser')
def close(context):
    context.driver.close()

"""driver=webdriver.Chrome()

driver.get("https://stage-refactor.credentialmydoc.com/")
time.sleep(2)
#driver.find_element(By.XPATH,"//div[text()='Log in']").click()
driver.find_element(By.XPATH,"//input[@formcontrolname='email']").send_keys("ctg@credentialmydoc.com")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("ctgadmin2018")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)
"""
