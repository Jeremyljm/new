#!/usr/bin/env python
# -*- coding: utf-8 -*-

class HouseItem:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self,):

        return "[%s] 占地 %.2f" %(self.name, self.area)

class House:
    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):

        # python 能够自动的将一对括号内的代码链接在一起
        return ("户型： %s\n总面积：%.2f[剩余：%.2f]\n家具： %s" %
                (self.house_type, self.area,
                 self.free_area, self.item_list))

    def add_item(self,item):
        print("要添加%s" % item)



# 创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)

# 创建房子

my_home = House("两室一厅", 89)


my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)