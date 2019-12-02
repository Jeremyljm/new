#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import sys
# sys.path.append('E:\Git\selenium')

from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
import os

class FirstCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.login = RegisterBusiness(self.driver)
    def tearDown(self):
        self.driver.close()
        print("这是case的后置条件")

    def test_login_email_error(self):
        email_error = self.login.login_email_error('34','111','111111','test1')
        self.assertFalse(email_error,"case执行了")
        # if email_error == True:
        #     print("注册成功，此条case执行失败")

    def test_login_username_error(self):
        username_error = self.login.login_name_error('78747324@qq.com', '1111', '111111', 'test1')
        self.assertFalse(username_error)

    def test_login_code_error(self):
        code_error = self.login.login_name_error('78747324@qq.com', '111111', '111111', 'test')
        self.assertFalse(code_error)

    def test_login_password_error(self):
        password_error = self.login.login_name_error('78747324@qq.com', '111', '111', 'test1')
        self.assertFalse(password_error)

    def test_login_success(self):
        success = self.login.login_name_error('78747324@qq.com', '11111', '111111', 'test1')
        self.assertFalse(success)

"""
def main():
    first = FirstCase()
    first.test_login_code_error()
    first.test_login_email_error()
    first.test_login_password_error()
    first.test_login_username_error()
    first.test_login_success()
"""
if __name__ == '__main__':
    file_path = os.path.join(os.getcwd() + "/report" + "test.html")
    f = open(file_path, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_success'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="这是一个报告",description="这是第一个测试报告")
    runner.run(suite)

    # unittest.TextTestRunner().run(suite)
   # unittest.main()








