#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib
import re
import random
from time import sleep

def main():
    url = 'https://www.zhihu.com/'
    headers = {"Referer": "https://www.zhihu.com/signup?next=%2F",
             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
    i = 925
    for x in range(1020, 2000, 20):
        data = {'start': '1000',
                'offset': str(x),
                '_xsrf': 'a128464ef225a69348cef94c38f4e428'}
        content = requests.post(url, headers=headers, data=data, timeout=10).text
        imgs = re.findall('<img src=\\\\\"(.*?)_m.jpg', content)
        for img in imgs:
            try:
                img = img.replace('\\', '')
                pic = img + '.jpg'
                path = 'd:\\ERP' + str(i) + '.jpg'
                urllib.urlretrieve(pic, path)
                print ('下载了第' + str(i) + u'张图片')
                i += 1
                sleep(random.uniform(0.5, 1))
            except:
                print ('抓漏1张')
                pass
        sleep(random.uniform(0.5, 1))

if __name__ == '__main__':
    main()