#!/usr/bin/env python
# -*- coding: utf-8 -*-

xiaoming_dictg = {"name": "小明",
                  "qq": "178747324",
                  "phone": "15827418090"}

# 迭代遍历字典
# 遍历k是每一次循环中，获取到的键值对的key

for k in xiaoming_dictg:

    print("%s - %s" %(k, xiaoming_dictg[k]))
