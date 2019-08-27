from selenium import webdriver
from time import sleep

# driver = webdriver.Firefox(executable_path=r'D:\soft\360down\Mozilla Firefox\geckodriver.exe')
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('我要自学网')
# print(driver.find_elements_by_id('kw'))
driver.set_window_size(100,600)
sleep(2)
# driver.find_element_by_id('kw').click()
# sleep(2)
driver.quit()


