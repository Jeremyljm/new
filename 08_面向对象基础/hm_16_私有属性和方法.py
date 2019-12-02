#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def secret(self):
        print("%s 我的年龄是[%d]" % (self.name,self.__age))

li = Women("ljm")

# 私有属性，在外界不能直接被直接访问
# print(li.__age)

# 在对象的方法内部，是可以访问对象的私有属性
li.secret()
