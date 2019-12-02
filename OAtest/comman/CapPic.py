#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os

def CapPic(driver):
    pt = time.strftime('%Y%m%d%H%m',time.localtime(time.time()))
    picname = os.path.dirname(os.path.abspath('.')) + '\\picture\\' + pt + '.png'
    driver.get_screenshot_as_file(picname)

