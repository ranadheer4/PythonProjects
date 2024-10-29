from selenium.webdriver.common.by import By


class AccountRegisterationPage():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_pswrd_name = "password"
    check_agree_name = "agree"
    btn_continue_xpath = "//button[@type='submit']"
    txt_confirmmsf_xpath = "//h1[text()='Your Account Has Been Created!']"

    def     __init__(self,driver):
        self.driver=driver

    def setFirstName(self,fname):
        self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)
        #self.driver.find_element_by_.self.txt_firstname_name).sendkeys(fname)
        #self.driver.find_element_by_xpath(self.txt_firstname_name).sendkeys(fname)
    def setLastName(self,lname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def setPassword(self, pswrd):
        self.driver.find_element(By.NAME, self.txt_pswrd_name).send_keys(pswrd)

    def setPrivacy(self):
        self.driver.find_element(By.NAME, self.check_agree_name).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.btn_continue_xpath).click()

    def getConfirmation(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_confirmmsf_xpath).text()
        except:
            None