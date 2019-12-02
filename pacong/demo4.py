#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request

# 没有使用代理的
# url = 'http://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())

# 使用代理的
url = 'http://httpbin.org/ip'
# 1.使用ProxyHandle，传入代理构建一个handler
handel = request.ProxyHandler({"http":"112.16.172.107:63141"})
# 2.使用上面创建的handel构建一个opener
opener = request.build_opener(handel)
# 3.使用opener去发送一个请求
resp = opener.open(url)

print(resp.read())

# 1.https://www.kuaidaili.com/ops/ 快代理地址
# 2.http://httpbin.org/ip 获取自己电脑ip地址