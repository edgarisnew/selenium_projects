import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

pyperclip.copy("StPantaleon")



driver = webdriver.Chrome()

driver.get("https://www.planetminecraft.com/server/lunar-smp-5336400/vote/")

driver.implicitly_wait(30)

cookies = driver.find_element(By.CLASS_NAME,"css-47sehv")

WebDriverWait(driver,30).until(
    EC.presence_of_element_located((By.CLASS_NAME,"css-47sehv"))
)

cookies.click()


name = driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div[1]/form/input[1]")

name.click()

name.send_keys(Keys.COMMAND,"v")

submit = driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div[1]/form/input[3]")

submit.click()

pyperclip.copy(" ")

time.sleep(30)

driver.quit

