#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.dianjiangla.com/")

testobj = driver.find_element_by_link_text("登录")
testobj.click()
username = driver.find_element_by_name("username")
username.send_keys("15827418090")
password = driver.find_element_by_name("password")
password.send_keys("123456")


# username.send_keys(Keys.CONTROL, 'a')
# username.send_keys(Keys.BACKSPACE)

submit = driver.find_element_by_xpath('//*[@id="form1"]/div/div[5]/div[2]/input')
submit.send_keys(Keys.ENTER)


time.sleep(3)
driver.quit()