#!/usr/bin/env python
# -*- coding: utf-8 -*-

name_list = ["张三", "李杰明", "李四", "王五", "李杰明"]


# len(length 长度) 函数可以统计列表中元素的总数
list_len = len(name_list)

print(list_len)



# count 方法可以统计列表中某一个数据出现的次数

count = name_list.count("李杰明")
print("出现的次数： %d" % count)

# 从列表中删除此一次出现的数据
name_list.remove("李杰明")

print(name_list)