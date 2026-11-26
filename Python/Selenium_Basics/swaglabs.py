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
# time.sleep(2)

# Locaters

# username=driver.find_element(By.ID, "user-name")
username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
# password=driver.find_element(By.ID, "password")
password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
login_button = driver.find_element(By.ID, "login-button")
wait = WebDriverWait(driver, 10)

# login_button=driver.find_element(By.ID, "login-button")
login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))


# Action
username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()
# time.sleep(2)

actions=ActionChains(driver)
actions.send_keys(Keys.ENTER).perform()

login_button.click()
login_button.send_keys(Keys.ENTER)

if "inventory" in driver.current_url:
    print("Login successful - Assertion Passed!")
    print("Login successful")
else:
    print("Login failed - Assertion Failed!")

assert "inventory" in driver.current_url, "Login failed!"
assert "https://www.saucedemo.com/inventory.html" in driver.current_url
driver.quit()
