from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get('https://www.google.ru/')
e = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
e.send_keys('купить ноутбук')
e.send_keys(Keys.ENTER)
time.sleep(4)
driver.find_element(By.XPATH, '/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a/h3').click()

tabs = driver.window_handles
driver.switch_to.window(tabs[1])

time.sleep(10)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[6]/div/div/div[2]/label[14]').click()
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[2]/div/button[1]').click()

time.sleep(30)
