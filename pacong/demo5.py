#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 大鹏董成鹏主页 http://www.renren.com/880151247/profile
# 人人网登陆 url：http://www.renren.com/SysHome.do

from urllib import request
# 1.不使用cookie去请求大鹏的主页


dapeng_url = 'http://www.renren.com/880151247/profile'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
'Cookie': 'jebe_key=023824dc-f08d-420f-b0bd-b20f9a4a7502%7C419a91da688d5ab4423c6c0399d74c15%7C1554875985123%7C1%7C1554875988853; _ga=GA1.2.1138647399.1554876036;' \
          ' anonymid=juaswge3-pznf7w; depovince=GW; _r01_=1; ' \
          'JSESSIONID=abc9kJmwaB66zgz0B0fOw; ick_login=7b4f8415-b12f-4ef9-86b2-9df8d526ea9d; ' \
          'ick=b438dd04-900f-458e-9ac4-b42fd5f8536b; XNESSESSIONID=200e06808763; ' \
          'WebOnLineNotice_970373354=1; first_login_flag=1; ln_uact=15827418090; ' \
          'ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebecookies=6d96223c-1b01-4589-88ae-bca44e8d9d66|||||; _de=7FDBB1605E96C19DD89AADF4B0420A80; p=d0a055d82d792de4c544a3839c42435c4; ' \
          't=cdbd83a5d5f3b6a53e73c954c328e5f54; societyguester=cdbd83a5d5f3b6a53e73c954c328e5f54; id=970373354; xnsid=fa1c1215; ver=7.0; loginfrom=null'
}

req = request.Request(url=dapeng_url,headers=headers)
resp = request.urlopen(req)
# print(resp.read())
with open('renren.html','w',encoding='utf-8') as fp:
    fp.write(resp.read().decode('utf-8'))