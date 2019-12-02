#!/usr/bin/env python
# -*- coding: utf-8 -*-


from ShowapiRequest import ShowapiRequest
import pytesseract
from PIL import Image
# image = Image.open("E:/QQ20190528140518.png")
# text = pytesseract.image_to_string(image)
# print(text)

r = ShowapiRequest("http://route.showapi.com/184-4", "96378", "8bc3a15c82204a02a8916797f64c7bdd" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"D:/b.png") #文件上传时设置
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息