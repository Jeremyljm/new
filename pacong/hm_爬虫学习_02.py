#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# 发送post请求非常简单，直接调用‘request.post’方法就可以，
#  如果返回的是json数据，那么可以调用'request.json()'来将json字符串转化成字典或者列表
data = {
        "email": "15827418090",
        "password": "ljm9527.."
    }

headers = {
    'Referer':'http://www.renren.com/970373354',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
proxy = {
    'http':'124.205.155.151:9090'
}
response = requests.get('http://www.renren.com/PLogin.do',
                         proxies=proxy,data=data, headers=headers)

print(response.json())