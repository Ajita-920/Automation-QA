# import webdriver
from selenium import webdriver
import time
# initialize chrome with webdriver
driver = webdriver.Chrome()
time.sleep(1)
# maximize window
driver.maximize_window()
# navigate to url
url = "https://www.google.com/"
driver.get(url)
time.sleep(1)
#check current url
print("The current url is: ", driver.current_url)

driver.get("https://www.saucedemo.com/")
time.sleep(1)
# refresh the page
driver.refresh()
time.sleep(1)
# Browser back navigation
driver.back()
time.sleep(1)
# Browser forward navigation
driver.forward()
time.sleep(1)
# quit the driver
driver.quit()
