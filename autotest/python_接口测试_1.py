#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince'
params = {'theRegionCode': 3113}
response = requests.get(url= url, params =params)

print(response.text)