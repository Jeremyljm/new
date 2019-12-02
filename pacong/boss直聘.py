#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup

import requests
import xlwt
import bs4

url = "https://www.zhipin.com/"

def get_job_info(index):
    params = {
        "query":"index",
        "city":100010000
    }
    request_url = url + "/job_detail/?" + urlencode(params)
    print("请求的URL:{}".format(request_url))
    post_infos = []
    flip_flag = True
    while flip_flag:
        print("[DEBUG INFO]: 请求网址:{}".format(request_url))
        try:
            soup = bs4.BeautifulSoup(request.get(request_url).text,"lxml")
            job_list =  soup.find("div",{"class":"job-box"}).find("div",{"class":"job-list"})
        except:
            print("没有查询到相关记录")
            break
        for job in job_list:
            job_primary = job.find("div",{"class":"job-primary"})
            info_primary = job_primary.find("div",{"class":"info-primary"})
            info_company = job_primary.find("div",{"class":"info-company"})
            info_publis = job_primary.find("div", {"class": "info_publis"})


