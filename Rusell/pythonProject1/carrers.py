from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Path to your WebDriver executable (ChromeDriver in this case)
#webdriver_path = '/path/to/chromedriver'  # Replace with the path to your WebDriver

# URL of the website to launch
website_url = 'https://alector.com/culture-careers/'

# Initialize the WebDriver
#driver = webdriver.Chrome(executable_path=webdriver_path)
driver = webdriver.Chrome()
try:
    # Open the website
    driver.get(website_url)

    # Wait for a few seconds to see the launched website (optional)
    time.sleep(5)

    # Optionally, interact with the website
    # For example, find an element by its ID and print its text
    element = driver.find_element(By.ID, 'element_id')  # Replace 'element_id' with the actual ID of an element
    print(element.text)

finally:
    # Close the browser
    driver.quit()
