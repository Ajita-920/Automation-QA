from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#initialize chrome with webdriver
driver=webdriver.Chrome()
#maximize window
driver.maximize_window()
#Navigate to url
url="https://formy-project.herokuapp.com/modal"
driver.get(url)
time.sleep(2)

open_modal=driver.find_element(By.ID, "modal-button")
open_modal.click()
time.sleep(2)
close_button=driver.find_element(By.XPATH, "//*[@id='close=button']")
close_button.click()


driver.quit()