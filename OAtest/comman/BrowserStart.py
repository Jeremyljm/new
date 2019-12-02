#!/usr/bin/env python
# -*- coding: utf-8 -*-

from comman.ReadConfig import getbrowserinfo
from selenium import webdriver
import os
from comman.CapPic import CapPic
from comman.LoginGen import LogGen
logger = LogGen(logger = '浏览器启动加载').getlog()

def BrowserStart():
    browsername = getbrowserinfo('BrowserName')
    url = getbrowserinfo('url')
    if browsername == 'Chrom':
        logger.info('启动谷歌浏览器')
        driver = webdriver.Chrome()
        logger.info('打开测试网页')
        driver.get(url)
    if browsername == 'IE':
        driver = webdriver.ie()
        driver.get(url)

    CapPic(driver)
BrowserStart()
