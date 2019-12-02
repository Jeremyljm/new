#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 大鹏董成鹏主页 http://www.renren.com/880151247/profile
# 人人网登陆 url：http://www.renren.com/SysHome.do

from urllib import request,parse
from http.cookiejar import CookieJar

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

def get_opener():
    # 1. 登陆
    # 1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    # 1.2 使用cookiejar创建一个HTTPCookieprocess对象
    handel = request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用上一步创建的handel创建一个opener
    opener = request.build_opener(handel)

    return opener
    # 1.4 使用opener发送登录的请求（人人网的邮箱和密码）

def login_renren(opener):
    data = {
        "email": "15827418090",
        "password": "ljm9527.."
    }
    login_url = "http://www.renren.com/PLogin.do"
    req = request.Request(login_url,data=parse.urlencode(data).encode('utf-8'),headers=headers)
    opener.open(req)
def visit_profile(opener):
    # 2.访问个人主页
    dapeng_url = 'http://www.renren.com/880151247/profile'
    # 获取个人主页的页面的时候，可直接使用之前的opener
    req = request.Request(dapeng_url,headers=headers)
    resp = opener.open(req)
    with open('renren1.html','w',encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))

if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)