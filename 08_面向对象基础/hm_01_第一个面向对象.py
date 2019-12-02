#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")

tom = Cat()

tom.drink()
tom.eat()
print(tom)

addr = id(tom)
# 十进制
print("%d" % addr)
# 十六进制
print("%x" % addr)