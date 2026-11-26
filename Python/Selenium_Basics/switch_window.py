# Script to swtich windows or window handling
#import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#initialize chrome with webdriver
driver=webdriver.Chrome()
#maximize window
driver.maximize_window()
#Navigate to url
url="https://formy-project.herokuapp.com/switch-window"
driver.get(url)
time.sleep(2)
#Switch window
switch_window=driver.find_element(By.ID, "new-tab-button")
switch_window.click()
time.sleep(2)
#window handling
#print(driver.window_handles)
windows=driver.window_handles
print("The driver is in this window:", driver.current_window_handle)

#switch to new window
driver.switch_to.window(windows[1])
print("The driver is in this window:", driver.current_window_handle)

driver.find_element(By.XPATH, "//a[@class='btn btn-lg btn-primary']").click()
time.sleep(2)
driver.quit()