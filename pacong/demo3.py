#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request,parse


# url = 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='

# resp = request.urlopen(url)
# print(resp.read())

url = 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
           'Referer':'https://www.lagou.com/jobs/list_python?px=default&city=%E5%85%A8%E5%9B%BD'}
data = {'first':'true', 'pn':1, 'kd':'python'}
req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'),method='post')
resp = request.urlopen(req)
print(resp.read().decond('utf-8'))