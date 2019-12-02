#!/usr/bin/env python
# -*- coding: utf-8 -*-

def GetUrl(url):
    urls = url.split('/')
    url = urls[0] +'//' + urls[1] +'/' +urls[2] +'/' +urls[3] +'/'
    return url
print(GetUrl('http://192.168.0.8:83/SignIn.aspx'))