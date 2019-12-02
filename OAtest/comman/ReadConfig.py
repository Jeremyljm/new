#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import os
def getbrowserinfo(name):
    cf = configparser.ConfigParser()
    cfpath = os.path.dirname(os.path.abspath('.')) + '\\config\\config.ini'
    cf.read(cfpath)
    browsername = cf.get('browser', name)
    return browsername

