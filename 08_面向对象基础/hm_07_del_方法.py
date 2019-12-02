#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Cat():

    def __init__(self, new_name):

        self.name = new_name

        print("%s来了" % self.name)

    def __del__(self):

        print("%s 我去了" % self.name)


tom = Cat("Tom")

print(tom.name)
print("*" * 50)