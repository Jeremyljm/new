#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
import unittest
import HTMLTestRunner


class WebTourTest(unittest.TestCase):

    def setUp(self):

        #初始化测试环境
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.dianjiangla.com/")

    def testLogin(self):

        #测试主体部分
        testobj = self.driver.find_element_by_link_text("登录")
        testobj.click()
        username = self.driver.find_element_by_name("username")
        username.send_keys("15827418090")
        password = self.driver.find_element_by_name("password")
        password.send_keys("123456")

        # username.send_keys(Keys.CONTROL, 'a')
        # username.send_keys(Keys.BACKSPACE)

        submit = self.driver.find_element_by_xpath('//*[@id="form1"]/div/div[5]/div[2]/input')
        submit.send_keys(Keys.ENTER)
        time.sleep(3)

    def tearDown(self):

        #收尾部分
        self.driver.quit()

if __name__ == '__main__':
    test = unittest.TestSuite()
    test.addTest(WebTourTest('testLogin'))
    file_result = open('d:\\test2.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title=u'Web测试报告', description=u'用例执行情况')
    runner.run(test)
    file_result.close()

