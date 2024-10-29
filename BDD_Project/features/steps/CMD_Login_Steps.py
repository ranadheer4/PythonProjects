import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch Chrome browser')
def step_impl(context):
    context.driver=webdriver.Chrome()

@when('I open CMD Login home page')
def step_impl(context):
    context.driver.maximize_window()
    context.driver.get("https://stage-refactor.credentialmydoc.com/")

@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element(By.XPATH, "//input[@formcontrolname='email']").send_keys(user)
    context.driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(pwd)

@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(2)

@then('User must succesfully login to the Dashboard page')

def step_impl(context):
    try:
        text=context.driver.find_element(By.XPATH,"//div/h4[text()='Workflow']").text
    except:
        context.driver.close()
        assert False,"Test Failed"
    if text=="Workflow":
        context.driver.close()
        assert True, "Test Passed"



