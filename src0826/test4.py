from selenium import webdriver
import time
import os

driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("C:/Users/doudou/AppData/Local/Temp/360zip$Temp/360$10/selenium2html/upload.html#")
driver.get(file_path)
time.sleep(5)
# 定位上传文件按钮
driver.find_element_by_tag_name("input").send_keys("C:/Users/doudou/AppData/Local/Temp/360zip$Temp/360$10/selenium2html/upload.html#");

time.sleep(5)
driver.quit()
