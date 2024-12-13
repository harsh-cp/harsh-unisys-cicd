from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize web driver
chrome_driver = webdriver.Chrome()

# Open the registration page
chrome_driver.get("https://app.delvex.io/register")

# Fill in the registration form
chrome_driver.find_element(By.NAME, "email").send_keys("abcd@gmail.com")
chrome_driver.find_element(By.NAME, "name").send_keys("harsh")
chrome_driver.find_element(By.NAME, "password").send_keys("Pass@1234")
chrome_driver.find_element(By.NAME, "confirm_password").send_keys("Pass@1234")


# By XPath
chrome_driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[5]/button').click()
# By CSS selector 
#chrome_driver.find_element(By.CSS_SELECTOR,"button[type='button']").click()
# Close the browser after a delay
time.sleep(10)
chrome_driver.quit()
