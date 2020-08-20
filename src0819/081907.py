from selenium import webdriver
import time
import os


driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath("C:/Users/doudou/AppData/Local/Temp/360zip$Temp/360$7/selenium2html/level_locate.html")
driver.get(file_path)
driver.maximize_window()
from selenium.webdriver.common.action_chains import ActionChains

driver.find_element_by_link_text("Link1").click()
time.sleep(6)
target=driver.find_element_by_link_text("Another anction")
#鼠标事件，移动鼠标到目标元素
ActionChains(driver).move_to_element(target).perform()
time.sleep(10)

driver.quit()

