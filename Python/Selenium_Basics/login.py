# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# initialize chrome with webdriver
driver = webdriver.Chrome()
# maximize window
driver.maximize_window()
# navigate to url
url = "https://www.saucedemo.com/"
driver.get(url)
driver.implicitly_wait(10)  # Wait for 10 seconds for elements to be present
#time.sleep(2)

#Locaters

#username=driver.find_element(By.ID, "user-name")
password=driver.find_element(By.ID, "password")
login_button=driver.find_element(By.ID, "login-button")
wait=WebDriverWait(driver, 10)

#login_button=driver.find_element(By.ID, "login-button")
login_button=wait.until(EC.element_to_be_clickable((By.ID, "login-button")))


#Action
username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()
#time.sleep(2)

# Validation using Assertion
expected_url = "https://www.saucedemo.com/inventory.html"
actual_url = driver.current_url

assert actual_url == expected_url, "Login failed!"

print("Login successful - Assertion Passed!")
print("Login successful")

'''
#XpathLocators
username=

Relaive XPATH
//*[@id="user-name"]
Absolute XPATH
/html/body/div/div/div[2]/div[1]/div[1]/div/form/div

'''





driver.quit()