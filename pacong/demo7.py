#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar('cookie.txt')
handel = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handel)

resp = opener.open('http://www.baidu.com/')
cookiejar.save()

