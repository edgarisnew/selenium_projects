#Voting bot for the website "Planet Minecraft"
#I have reported this issue to the Website and it has been fixed by utilising the suggestion I made.


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

pyperclip.copy("USERNAME") #Utilizing regular send_keys() would return a non-interactable error, this was the fix I came up with.



driver = webdriver.Chrome()

driver.get("VOTING URL")

driver.implicitly_wait(30)

cookies = driver.find_element(By.CLASS_NAME,"")

WebDriverWait(driver,30).until(
    EC.presence_of_element_located((By.CLASS_NAME,""))
)

cookies.click()


name = driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div[1]/form/input[1]") #Although here I used a XPATH, a CSS_Selector would be better. Will update in the future.

name.click()

name.send_keys(Keys.COMMAND,"v")

submit = driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div[1]/form/input[3]") #Although here I used a XPATH, a CSS_Selector would be better. Will update in the future.

submit.click()

pyperclip.copy(" ")

time.sleep(30) #Not recommended to use but allowed me to check visually instead of asserting with the script.

driver.quit

