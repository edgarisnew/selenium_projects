import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get("http://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html")

driver.implicitly_wait(30)

autoclose_success = driver.find_element(By.ID,("autoclosable-btn-success"))

autoclose_success.click()

normal_success = driver.find_element(By.ID,"normal-btn-success")

time.sleep(5)

WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.ID,"normal-btn-success"))
)

normal_success.click()


close_normal_sucess = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div[2]/div[2]/button")

close_normal_sucess.click()

normal_warning = driver.find_element(By.ID,"normal-btn-warning")

normal_warning.click()

close_normal_warning = driver.find_element(By.XPATH,"  ")



time.sleep(5)

driver.quit()