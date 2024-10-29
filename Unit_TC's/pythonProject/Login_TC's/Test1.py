import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up WebDriver
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)  # Implicit wait
    @classmethod
    def setUp(self):
        # Open the web page
        self.driver.get('https://env-app.olobby.com/')
        self.wait = WebDriverWait(self.driver, 10)
        print("Im Opening")
    def test_page_title(self):
        # Verify page title
        self.assertEqual("", self.driver.title)

    """def test_search_functionality(self):
        # Perform a search
        search_box = self.driver.find_element(By.NAME, 'q')
        search_box.send_keys('example search')
        search_box.submit()

        # Wait for search results to load
        self.wait.until(EC.visibility_of_element_located((By.ID, 'search-results')))

        # Verify search results are displayed
        search_results = self.driver.find_element(By.ID, 'search-results')
        self.assertTrue(search_results.is_displayed())
"""
    def test_login(self):
        # Perform login
        username_input = self.driver.find_element(By.XPATH, "//form//input[@name='username']")
        password_input = self.driver.find_element(By.XPATH, "//form//input[@name='password']")
        submit_button = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")

        username_input.send_keys('amrut.margala@nstarxinc.com')
        password_input.send_keys('Reset@123')
        submit_button.click()

        # Verify login success
        self.assertEqual('OLOBBY', self.driver.title)
        proced_btn=self.driver.find_element(By.XPATH,"//app-dashboard-notification//button[text()='Proceed']")
        proced_btn.click()
        self.assertEqual('OLOBBY',self.driver.title)
        self.wait = WebDriverWait(self.driver, 20)

    @classmethod
    def tearDown(self):
        # Clean up after each test case
        pass
        print("Im Closing")
    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
