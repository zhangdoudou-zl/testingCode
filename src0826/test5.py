from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("C:/Users/doudou/AppData/Local/Temp/360zip$Temp/360$8/selenium2html/modal.html#")
driver.get(file_path)
driver.maximize_window()
#点击click
# driver.find_element_by_id("show_modal").click()
driver.find_element_by_link_text("Click").click()
time.sleep(5)
# 定位modal-body
# div1 = driver.find_element_by_class_name("modal-body")
driver.find_element_by_link_text("click me").click()
time.sleep(5)
# 定位modal-footer
# div2 = driver.find_element_by_class_name("modal-footer")
buttons = driver.find_elements_by_tag_name("button")
buttons[0].click()
time.sleep(5)
driver.quit()
