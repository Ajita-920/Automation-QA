from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Login page URL
url = "https://sagar-test-qa.vercel.app"

# Replace these with your test credentials
username_value = "your_username"
password_value = "your_password"

# Start Chrome
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Open the login page
    driver.maximize_window()
    driver.get(url)

    # Locate the username and password fields
    username = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[1]"))
    )
    password = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[2]"))
    )

    # Enter login details
    username.send_keys(username_value)
    password.send_keys(password_value)

    # Click the Login button
    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Login']")
        )
    )
    login_button.click()

    # Check whether a JavaScript alert appears
    try:
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())

        print("TEST PASSED: JavaScript alert appeared.")
        print("Alert message:", alert.text)

        # Click OK on the alert box
        alert.accept()
        print("Alert closed successfully.")

    except TimeoutException:
        print("No JavaScript alert appeared after clicking Login.")
        print("Current page URL:", driver.current_url)

        # Check whether the page displays an inline error message
        print("Page title:", driver.title)

    time.sleep(2)

except Exception as e:
    print("TEST FAILED:", e)

finally:
    # Close the browser

    alert=driver.switch_to.alert
    alert.accept()
    #alert.dismiss()

    driver.quit()
