#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
# 1.发送get请求，直接调用‘request.get就可以，想要什么类型的请求，就调用什么方法
response = requests.get("https://www.baidu.com/")
# 2.response.text和response.content的区别
# response.text：这个是requests，将response.text进行解码的字符串，解码需要指定一个解码方式，
#                 requests会根据自己的猜测来判断编码的方式，所以有时候可能会猜错，就会导致解码产生乱码，这个时候就应该使用response.content.decode('utf-8')进行手动解码
# response.content：这个是直接从网络上面抓取的的数据，没有经过解码，所以是一个bytes类型，其实在硬盘上和在网络上传输的字符串都是bytes类型


# print(type(response.text))
# print(response.text)

# print(type(response.content))
# print(response.content.decode('utf-8'))
#
# print(response.url)
# print(response.encoding)
# print(response.status_code)

params = {
    'wd':'中国'
}
headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                    '(KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

response = requests.get("https://www.baidu.com/s", params=params, headers=headers)
with open('12.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))

print(response.url)