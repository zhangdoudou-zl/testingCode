from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("乃万")
# 定位“百度一下”按钮
su1 = driver.find_element_by_id("su")
# 右击
ActionChains(driver).context_click(su1).perform()

# 双击
time.sleep(6)
ActionChains(driver).double_click(su1).perform()


time.sleep(8)
title = driver.find_element_by_id("su")
target = driver.find_element_by_link_text("乃万_百度百科")
# 拖动
ActionChains(driver).drag_and_drop(title, target).perform()
# # 移动
ActionChains(driver).move_to_element(target).perform()
time.sleep(10)
driver.quit()
