#!/usr/bin/env python
# -*- coding: utf-8 -*-

name_list = ["张三", "李四", "王五", "王小二"]

# 使用迭代遍历列表
"""
顺序的从列表中一次获取数据，每一次循坏过程中，数据都会保存在my_name这个变量中，在循环体
内部可以访问到当前这一次获取到的数据

for my_name in 列表变量:

    print("我的名字是 %s" % my_name)
    
"""

for my_name in name_list:

    print("我的名字是 %s" % my_name)




