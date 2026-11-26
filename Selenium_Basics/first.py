#import webdriver
from selenium import webdriver
import time
#initialize chrome with webdriver
driver=webdriver.Chrome()
time.sleep(1)
url="https://www.google.com/"
driver.get(url)
time.sleep(1)

#quit the driver
driver.quit()
