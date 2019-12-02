#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random
from ShowapiRequest import ShowapiRequest
from PIL import Image

driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
print(EC.title_contains("注册"))
email_element = driver.find_element_by_id("register_email")
driver.save_screenshot("D:/a.png")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open("D:/a.png")
img = im.crop((left, top, right, height))
img.save("D:/b.png")

r = ShowapiRequest("http://route.showapi.com/184-4", "96378", "8bc3a15c82204a02a8916797f64c7bdd")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"D:/b.png") #文件上传时设置
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
time.sleep(10)
driver.find_element_by_id('captcha_code').send_keys(text)


# user_email = ''.join(random.sample('123456acbfrg', 6))
# print(user_email)


element = driver.find_element_by_class_name("controls")
locator = (By.CLASS_NAME, "controls")
WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator))

print(email_element.get_attribute("placeholder"))
email_element.send_keys("178747324@qq.com")
print(email_element.get_attribute("value"))

# driver.find_element_by_id("register_email").send_keys("179747324@qq.com")
# user_name_element_node = driver.find_elements_by_class_name("controls")[1]
# user_element = user_name_element_node.find_element_by_class_name("form-control")
# user_element.send_keys("Jeremy")
# driver.find_element_by_name("password").send_keys("ljm9527..")
# driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")
driver.close()

