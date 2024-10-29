from selenium.webdriver.common.by import By


class LoginPage:
    # Login Page
    textbox_username_name ="//input[@name='username']"
    textbox_password_name ="//input[@name='password']"
    button_login_xpath ="//button[@type='submit']"
    link_logout_linktext ="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH,self.textbox_username_name).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH,self.textbox_password_name).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()