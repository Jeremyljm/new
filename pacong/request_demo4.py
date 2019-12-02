#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# respnse = requests.get('https://www.baidu.com/')
# print(respnse.cookies.get_dict())

#  如果想要在多次请求中共享cookies，那么应该使用session，
url = "http://www.renren.com/PLogin.do"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

data = {
    "email": "15827418090",
    "password": "ljm9527.."
}
session = requests.Session()
session.post(url=url,data=data,headers=headers)

response = session.get('http://www.renren.com/880151247/profile')
with open('6666.html','w',encoding='utf-8') as fp:
    fp.write(response.text)