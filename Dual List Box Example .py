import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("http://demo.seleniumeasy.com/bootstrap-dual-list-box-demo.html")

driver.maximize_window()

select_all_right = driver.find_element(By.CLASS_NAME,"btn-group")

select_all_right.click()

move_all_right = driver.find_element(By.CSS_SELECTOR,"html > body > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div:nth-of-type(2) > button:nth-of-type(2)")
move_all_right.click()


select_all_left = driver.find_element(By.CSS_SELECTOR,"html > body > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div > div:nth-of-type(1) > div > a")

select_all_left.click()

select_all_right.click()

move_all_left = driver.find_element(By.CSS_SELECTOR,"html > body > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div:nth-of-type(2) > button:nth-of-type(1)")

move_all_left.click()

select_all_right.click()

WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,"btn-group"))
)

select_all_right.click()

select_all_left.click()

bootstrap = driver.find_element(By.CSS_SELECTOR,"html > body > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div:nth-of-type(1) > div > ul > li:nth-of-type(6)")

bootstrap.click()

cras_justo_odio = driver.find_element(By.CSS_SELECTOR,"html > body > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div:nth-of-type(1) > div > ul > li:nth-of-type(1)")

cras_justo_odio.click()

search_left = driver.find_element(By.CSS_SELECTOR,"input[type='text']")

search_left.send_keys("Vestibulum")
    


time.sleep(5)

driver.quit