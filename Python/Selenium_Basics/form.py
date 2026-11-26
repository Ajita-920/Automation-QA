
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Initialize Chrome WebDriver
driver = webdriver.Chrome()
# Maximize browser
driver.maximize_window()
# Open URL
url = "https://formy-project.herokuapp.com/form"
driver.get(url)
time.sleep(2)

# Initialize wait
wait = WebDriverWait(driver, 10)

# 1. First Name
firstname = driver.find_element(By.ID, "first-name")
firstname.send_keys("Ram")

# Validation
assert firstname.get_attribute("value") == "Ram"
print("First name entered successfully")

time.sleep(1)

# 2. Last Name
lastname = driver.find_element(By.ID, "last-name")
lastname.send_keys("Shyam")

# Validation
assert lastname.get_attribute("value") == "Shyam"
print("Last name entered successfully")

time.sleep(1)

# 3. Job Title
job_title = driver.find_element(By.ID, "job-title")
job_title.send_keys("Doctor")

# Validation
assert job_title.get_attribute("value") == "Doctor"
print("Job title entered successfully")

time.sleep(1)

# 4. Select Education 
education = driver.find_element(By.ID, "radio-button-3")
education.click()

# Validation
assert education.is_selected()
print("Education selected successfully")

time.sleep(1)

# 5. Select Sex (Checkbox)
sex = driver.find_element(By.ID, "checkbox-1")
sex.click()

# Validation
assert sex.is_selected()
print("Sex selected successfully")

time.sleep(1)

# 6. Select Years of Experience (Dropdown)
dropdown_menu = driver.find_element(By.ID, "select-menu")
select = Select(dropdown_menu)
select.select_by_value("4")

# Validation
assert select.first_selected_option.get_attribute("value") == "4"
print("Experience selected successfully")

time.sleep(1)

# 7. Scroll down to Date field
date_field = driver.find_element(By.ID, "datepicker")

driver.execute_script(
    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
    date_field
)

time.sleep(2)

# Enter Date
date_field.send_keys("11/25/2026")

# Validation
assert date_field.get_attribute("value") == "11/25/2026"
print("Date entered successfully")

time.sleep(1)

# 8. Scroll down to Submit button
submit_button = driver.find_element(By.XPATH, "//a[@role='button']")

driver.execute_script(
    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
    submit_button
)

time.sleep(2)

# Click Submit
submit_button.click()

# 9. Validate successful submission
success_message = wait.until(
    EC.visibility_of_element_located(
        (By.TAG_NAME, "h1")
    )
)

assert "Thanks for submitting your form" in success_message.text

print("Form submitted successfully!")
print("Validation Passed!")

time.sleep(3)

# Close browser
driver.quit()
