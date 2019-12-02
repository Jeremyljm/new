#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.dianjiangla.com/user/register")


time.sleep(2)
driver.find_element_by_id("username").send_keys("18887418090")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_link_text("注册").click()

time.sleep(3)
driver.quit()