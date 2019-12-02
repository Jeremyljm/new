#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

response = requests.get(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince')
response.text
print type(response)