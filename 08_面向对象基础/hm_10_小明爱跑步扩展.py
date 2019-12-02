#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person:

    def __init__(self, name, weight):

        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s 我的体重是%.2f公斤" % (self.name, self.weight)

    def eat(self):
        print("%s是吃货，吃完再减肥"%self.name)
        self.weight += 1
    def run(self):
        print("%s 爱跑步,跑步锻炼身体" % self.name)
        self.weight -= 0.5

xiaoming = Person("小明", 75.0)

xiaoming.eat()
xiaoming.run()
print(xiaoming)

xiaomei = Person("小美",45.0 )

xiaomei.run()
xiaomei.eat()
print(xiaomei)