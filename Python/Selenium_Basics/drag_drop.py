
# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# initialize chrome with webdriver
driver = webdriver.Chrome()
driver.maximize_window()

url="https://fromy"


from selenium.webdriver.common.action_chains import ActionChains
source=driver.find_element(By.XPATH,"//div[@id='image']//img")
destination=driver.find_element(By.XPATH,"//div[@id='box']")
actions=ActionChains(driver)
actions.drag_and_drop(source,destination).perform()
time.sleep(2)
driver.quit()
