from selenium import webdriver
import time
import os

#多层窗口定位

driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath("C:/Users/doudou/AppData/Local/Temp/360zip$Temp/360$6/selenium2html/frame.html")
driver.get(file_path)
driver.maximize_window()
time.sleep(6)
#从默认页面跳转到id=f2的页面
driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("布拉格")
driver.find_element_by_id("su").click()
time.sleep(6)

#跳转到默认页面
driver.switch_to.default_content()
driver.switch_to.frame("f1")
driver.find_element_by_link_text("click").click()
time.sleep(6)

driver.quit()

