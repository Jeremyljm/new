#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# 发送post请求非常简单，直接调用‘request.post’方法就可以，
#  如果返回的是json数据，那么可以调用'request.json()'来将json字符串转化成字典或者列表
data = {
    'first': 'true',
     'pn': '1',
     'kd': 'python'
}
headers = {
    'Referer':'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
proxy = {
    'http':'112.85.165.16:9999'
}
response = requests.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',
                         proxies=proxy, data=data,headers=headers)

print(response.json())