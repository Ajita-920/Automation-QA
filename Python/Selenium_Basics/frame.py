#import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#initialize chrome with webdriver
driver=webdriver.Chrome()
#maximize window
driver.maximize_window()
#Navigate to url
url="https://demoqa.com/frames"
driver.get(url)
time.sleep(2)

driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)
frame2=driver.find_element(By.ID, "frame2")
driver.switch_to.frame(frame2)
time.sleep(2)

driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)

driver.switch_to.default_content()

driver.quit()