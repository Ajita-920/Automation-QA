from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#initialize chrome with webdriver
driver=webdriver.Chrome()
#maximize window
driver.maximize_window()
#Navigate to url
url="https://formy-project.herokuapp.com/fileupload"
driver.get(url)
time.sleep(2)

file_upload=driver.find_element(By.ID, "file-upload-field")
file_upload.send_keys("/home/ajita/My Documents/File mine-Ajita/QA/demo.txt")



driver.quit()