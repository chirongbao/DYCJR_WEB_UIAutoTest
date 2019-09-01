from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class Loginlogout(object):
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self,username,password):
        self.driver.get('http://localhost')
        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').clear()
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_name('Submit').click()

    def logout(self):
        WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, '退出'))).click()
        self.driver.switch_to.alert.accept()

if __name__ == '__main__':
    aa = Loginlogout()
    aa.login('chirongbao','123456789')
    aa.logout()

