from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os


import os
driver = webdriver.Firefox()
driver.get("http://127.0.0.1:88/pro/user-login.html")
#放大窗口
driver.maximize_window()
driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_id("account").send_keys(Keys.TAB)
time.sleep(6)
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("password").send_keys(Keys.ENTER)
