#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

class Login():
    def browserstart(self, url):
        self.driver = webdriver.Chrome()
        # url = 'http://192.168.0.8:83/SignIn.aspx'
        self.driver.get(url)
        time.sleep(2)
    def login(self, uname, pwd):

        # driver.find_element_by_link_text("登录").click()
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        submit = self.driver.find_element_by_xpath('//*[@id="tabs22"]/tbody/tr[3]/td[2]/span')

        username.send_keys(uname)
        password.send_keys(pwd)
        submit.click()
        time.sleep(5)
        userid = self.driver.find_element_by_xpath('//*[@id="defaultMain"]/table[1]/tbody/tr/td[1]/div/b')

        if userid.text == '李杰明':
            print("login ok")
            self.logout()
        else:
            print("login fail")
            self.driver.quit()
    def logout(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/a').click()
        self.driver.quit()

t = Login()
t.browserstart('http://192.168.0.8:83/SignIn.aspx')
t.login('李杰明', 'SIXI#2015g')
# login('http://192.168.0.8:83/SignIn.aspx', '李杰明', 'SIXI#2015g')