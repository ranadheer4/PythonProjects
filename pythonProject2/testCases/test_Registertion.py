import os.path
import time


from pageObjects.AccountRegistrationPage import AccountRegisterationPage
from pageObjects.HomPage import HomePage

from utilities import randomString
from utilities.readProperties import ReadConfig


class Test_01_AccntReg:
    baseURL="https://demo.opencart.com/"


    def test_accnt_reg(self, setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title

        self.hp = HomePage(self.driver)
        time.sleep(2)
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        time.sleep(2)
        self.ar=AccountRegisterationPage(self.driver)
        self.ar.setFirstName("Vin")
        self.ar.setLastName("Ran")
        #self.ar.setEmail("Drana@dsl.com")
        self.email=randomString.random_string_generator()+'@gmail.com'
        self.ar.setEmail(self.email)
        self.ar.setPassword("9963883545Durgi")
        time.sleep(5)

        self.ar.setPrivacy()
        self.ar.clickContinue()
        time.sleep(2)
        self.conf_msg=self.ar.getConfirmation()
        time.sleep(2)
        #self.driver.close()
        if self.conf_msg=="sgvreb":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\Screenshots\\"+"test_accnt_reg.png")
            self.driver.close()
            assert False






