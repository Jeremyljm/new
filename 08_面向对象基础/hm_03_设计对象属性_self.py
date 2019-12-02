#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Cat:

    # 哪一个对象调用的方法，self就是哪一个对象的引用
    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("%s爱喝水" % self.name)
# 创建猫对象
tom = Cat()

# 可以使用 .属性名  利用赋值语句就可以
tom.name = "Tom"

tom.drink()
tom.eat()
print(tom)
# 再创建一个猫对象
lazy_cat = Cat()

lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)

