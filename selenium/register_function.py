#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
from base.find_element import FindElement

class RegisterFunction(object):
    def __init__(self,url):
        self.driver = self.get_driver(url)
    #获取driver 并且打开url
    def get_driver(self,url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver
    # 输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)

    # 定位用户信息，获取elelment
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    def get_range_user(self):
        user_info = ''.join(random.sample('acbdefrghi', 8))
        return user_info

    # 获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)

    # 解析图片获取验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "96378", "8bc3a15c82204a02a8916797f64c7bdd")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        return text



    def main(self):
        user_name = self.get_range_user()
        user_email = user_name + "@qq.com"
        file_name = "D:/c.png"
        code_text = self.code_online(file_name)
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name', user_name)
        self.send_user_info('password', "111111")
        self.send_user_info('code_text', code_text)
        self.get_user_element('register_button').click()
        code_error = self.get_user_element("code_text_error")
        if code_error == None:
            print("注册成功")
        else:
            self.driver.save_screenshot("E:\Git\selenium\Image\error.png")
        time.sleep(10)
        self.driver.close()

if __name__ == '__main__':
    register_function = RegisterFunction("http://www.5itest.cn/register")
    register_function.main()




