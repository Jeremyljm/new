#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test(num):

    print("在函数内部%d 对应的地址是%d" %(num, id(num)))

    # 1>定义一个字符串变量
    result = "hello"
    print("函数要返回的数据的内存地址是%d" %id(result))

    # 2> 将字符串变量返回
    return result

# 1.定义一个数字的变量
a = 10

print("a 变量保存数据的内存地址是%d" %id(a))

r = test(a)

print(r, id(r))