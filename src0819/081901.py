from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")

# driver.find_element_by_css_selector("#kw").send_keys("潘粤明")
# driver.find_element_by_css_selector("#su").click()
# time.sleep(6)


#清除操作
# driver.find_element_by_name("wd").clear()
# time.sleep(3)
# driver.find_element_by_css_selector("#kw").send_keys("刘心悠")
# driver.find_element_by_css_selector("#su").submit()
# time.sleep(6)

#通过链接访问
# driver.find_element_by_link_text("视频").click()
# time.sleep(6)


# driver.find_element_by_partial_link_text("频").click()
# # time.sleep(6)


# text=driver.find_element_by_id("s-bottom-layer-right").text
# print("text="+text)
#
# driver.find_element_by_id("kw").send_keys("周深")
# driver.find_element_by_id("su").submit()
#
# driver.implicitly_wait(10)
# driver.find_element_by_link_text("周深_百度百科").click()
# time.sleep(6)


driver.find_element_by_id("kw").send_keys("大鱼海棠")
driver.find_element_by_id("su").submit()
time.sleep(5)
# #最大化浏览器
# driver.maximize_window()
# time.sleep(6)
#
# #最小化
# driver.minimize_window()
# time.sleep(6)
#
# #自己设置宽高
# driver.set_window_size(400,800)
# time.sleep(3)

# driver.maximize_window()
# #浏览器后退
# driver.back()
# time.sleep(6)

# #浏览器的前进
# driver.forward()
# time.sleep(6)

# #将浏览器的滚动条放到最底端
# js="var q=document.documentElement.scrollTop=10000"
# #执行js
# driver.execute_script(js)
# time.sleep(3)


# #将浏览器的滚动条放到最顶端
# js1="var q=document.documentElement.scrollTop=0"
# driver.execute_script(js1)


# title=driver.title
# print("title="+title)

# url=driver.current_url
# print("url="+url)

driver.set_window_size(400,1000)
time.sleep(3)
#同时控制浏览器的左右上下
js="window.scrollTo(400,800)"
driver.execute_script(js)
time.sleep(6)


driver.quit()