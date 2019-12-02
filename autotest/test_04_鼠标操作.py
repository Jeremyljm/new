#!/usr/bin/env python
# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.dianjiangla.com/")

testobj = driver.find_element_by_link_text("注册")
# testobj.click() #单点击
# ActionChains(driver).move_to_element(testobj).context_click().perform() #点击某个按钮右键
# ActionChains(driver).move_to_element(testobj).double_click().perform() #双击

time.sleep(3)
driver.quit()