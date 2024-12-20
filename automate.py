from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

# Setting up headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU (Windows-specific)
chrome_options.add_argument("--no-sandbox")  # Required for running as root in Docker
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
 
# Initializing the web driver with options
service = Service("/usr/bin/chromedriver")  # Update the path to chromedriver
chrome_driver = webdriver.Chrome(service=service, options=chrome_options)

# opening a web URL
chrome_driver.get("https://rahulshettyacademy.com/angularpractice/")
#chrome_driver.get("https://portal.adhocnet.org/")

chrome_driver.find_element(By.NAME, "name").send_keys("harsh")
chrome_driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
chrome_driver.find_element(By.ID, "exampleInputPassword1").send_keys("Pass@1234")

chrome_driver.find_element(By.ID, "exampleCheck1").click()
myselect = Select(chrome_driver.find_element(By.ID,"exampleFormControlSelect1"))
# By visible text
#myselect.select_by_visible_text('Male')
# By index
myselect.select_by_index(0)


# By ID & CSS selector
#chrome_driver.find_element(By.ID, "inlineRadio2").click()
chrome_driver.find_element(By.CSS_SELECTOR, '#inlineRadio2').click()
chrome_driver.find_element(By.NAME, "bday").send_keys("24-06-2002")

# Submit the form
# using xpath for complex pattern matching
chrome_driver.find_element(By.XPATH, "//input[@type='submit']").click()


message = chrome_driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

#message validation 
assert "Success" in message
# precise way to print message
# try:
#     success_message = WebDriverWait(chrome_driver, 10).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
#     )
#     print("success message: ",success_message.text)
# except:
#     print("Success message not found")


time.sleep(5)


print("page title :",chrome_driver.title)

print("Page URL :", chrome_driver.current_url)

chrome_driver.save_screenshot("pagehome1.png")
print("current page screenshot saved")

# closing my driver / stopping
chrome_driver.quit() 
