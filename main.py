from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get('https://www.google.ru/')
e = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
e.send_keys('купить ноутбук')
e.send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '/html/body/div[7]/div/div[11]/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div/a').click()

tabs = driver.window_handles
driver.switch_to.window(tabs[1])

time.sleep(4)
d = driver.find_element(By.XPATH, '/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/mvid-filters-list/div/div[1]/div/div/mvid-accordion[3]/div/div/div/mvid-price-facet/div/mvid-range/div/input[1]')
d.clear()
d.send_keys('50000')
d.send_keys(Keys.ENTER)
time.sleep(30)
