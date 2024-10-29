from selenium.webdriver.common.by import By

class HomePage():
    lnk_myacnt_xpath = "//span[text()='My Account']"
    lnk_rgstr_linktext="Register"
    lnk_login_linktext="Login"

    def __init__(self,driver):
        self.driver=driver

    def clickMyAccount(self):
         self.driver.find_element(By.XPATH,self.lnk_myacnt_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_rgstr_linktext).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()

