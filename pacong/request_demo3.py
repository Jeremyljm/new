#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


# 1.在请求方法中，传递‘proxies’参数就可以
proxy = {
    'http':'113.122.169.21:9999'
}
response = requests.get('http://httpbin.org/ip',proxies=proxy)
print(response.text)