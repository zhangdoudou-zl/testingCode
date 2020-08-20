from selenium import webdriver
import time
import os

#如何去定位一组元素

driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath("C:/Users/doudou/AppData/Local/Temp/360zip$Temp/360$5/selenium2html/checkbox.html")
driver.get(file_path)
driver.maximize_window()

# 选择页面上所有的input，然后从中过滤出所有的checkbox 并勾选之
inputs=driver.find_elements_by_tag_name("input")
for input in inputs:
    #get_attribute：获得属性值
    if input.get_attribute("type")=="checkbox":
        input.click()

time.sleep(6)




driver.quit()