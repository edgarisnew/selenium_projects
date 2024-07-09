import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

driver = webdriver.Chrome()

driver.get("http://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

driver.implicitly_wait(15) #this line applies to all the elements in a Selenium Project - it doesn't always wait 10 seconds, if it finds the element it'll go on sooner.

download_element = driver.find_element("id","downloadButton")

download_element.click()


WebDriverWait(driver,30).until(
    EC.text_to_be_present_in_element( 
        (By.CLASS_NAME,"progress-label"), #Element that we want to inspect
         "Complete!" #Expected text
    )
)

progress_bar = driver.find_element(By.CLASS_NAME,"progress-label")

print(f"{progress_bar.text}")

close_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/button") 

close_button.click()

time.sleep(20)

driver.quit()