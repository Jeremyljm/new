#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver  # 加载webdrive方法
import time  # 导入time包


driver = webdriver.Chrome() # 创建谷歌对象，调用谷歌浏览器
driver.get("http://www.dianjiangla.com/") # 在谷歌中输入需访问的路径

time.sleep(3) # 设置停留等待时间3秒
# driver.maximize_window() #屏幕全屏
driver.set_window_size(400, 300)
driver.get_screenshot_as_file("c:\\test.png")

driver.refresh() #刷新页面
time.sleep(2)
driver.quit() # 退出页面