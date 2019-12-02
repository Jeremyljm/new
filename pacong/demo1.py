#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request
from urllib import parse

# 1.urlopen的用法 打开网页获取内容
# resp = request.urlopen('http://www.baidu.com')
# print(resp.getcode())
# print(resp.readline())
# rint(resp.readlines())

# 2.urlretrieve的用法 获取网页上的文件保存到本地
# request.urlretrieve('http://www.baidu.com', 'd:/baidu.html')

# 3.urllencode函数的用法
# params = {'name':'张三', 'age':18, 'greet':'hello world'}
# result = parse.urlencode(params)
# print(result)

# url = 'https://www.baidu.com/s'
# params = {"wd": "刘德华"}
# qs = parse.urlencode(params)
# print(qs)
# url = url + '?' + qs
# print(url)
# resp = request.urlopen(url)
# print(resp.read())

# 4.paras_qs函数的用法
params = {'name':'张三', 'age':18, 'greet':'hello world'}
result = parse.urlencode(params)
print(result)
qs = parse.parse_qs(result)
print(qs)