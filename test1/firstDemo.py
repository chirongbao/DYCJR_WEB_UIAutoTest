from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://localhost')
driver.find_element_by_name('username').clear()
driver.find_element_by_name('username').send_keys('chirongbao')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('123456789')
driver.find_element_by_name('Submit').click()
WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,'退出'))).click()
sleep(1)
driver.switch_to.alert.accept()
sleep(2)
driver.quit()





