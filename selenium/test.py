#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random




for i in range(10):
    user_email = ''.join(random.sample('123456acbfrg', 6)) + "@qq.com"
    print(user_email)