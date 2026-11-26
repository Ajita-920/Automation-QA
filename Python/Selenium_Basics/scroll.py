# Script to handle scroll bar in selenium
#import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#initialize chrome with webdriver
driver=webdriver.Chrome()
#maximize window
driver.maximize_window()
#Navigate to url
url="https://formy-project.herokuapp.com/scroll"
driver.get(url)
time.sleep(2)

#scroll
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)
driver.find_element(By.ID, "name").send_keys("Ajita")
driver.find_element(By.ID, "date").send_keys("06/06/2024")
time.sleep(2)
driver.execute_script("window.scrollTo(0,0);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)   
driver.save_screenshot("scroll.png")
driver.quit()
