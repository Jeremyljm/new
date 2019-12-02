#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import parse

url = 'https://www.baidu.com/s;hello?wd=python&username=abc#1'
# 1. urlparse函数的使用方法
# result = parse.urlparse(url)
# print('scheme:', result.scheme)
# print('netloc:', result.netloc)
# print('path:', result.path)
# print('params:', result.params)
# print('query:', result.query)
# print('fragment:', result.fragment)
# print(result)

# 2. urlsplit函数的使用方法
result1 = parse.urlparse(url)
result2 = parse.urlsplit(url)
print(result1)
print(result2)
# print('scheme:', result.scheme)
# print('netloc:', result.netloc)
# print('path:', result.path)
# # print('params:', result.params)
# print('query:', result.query)
# print('fragment:', result.fragment)