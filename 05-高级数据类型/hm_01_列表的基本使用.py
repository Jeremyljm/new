#!/usr/bin/env python
# -*- coding: utf-8 -*-


name_list = ["zhangsan", "lisi","wangwu"]

# 1.取值和取索引

print(name_list[2])

# 知道数据内容，想确定数据在列表中的位置
name_list.index("lisi")

print(name_list.index("lisi"))

# 2. 修改
name_list[2] = "李杰明"

# 3.增加
# append 方法可以在列表的末尾追加数据
name_list.append("wangxiaoer")

# insert 方法可以在列表的指定索引位置插入数据
name_list.insert(3,"张大仙")

# extend 方法可以把其他列表中的完整内容追加到当前列表的末尾
name_list2 = ["孙悟空", "猪八戒", "沙和尚"]
name_list.extend(name_list2)

# 4.删除
# remove 方法可以从列表中删除制定的数据
name_list.remove("张大仙")
# pop 方法默认可以把列表中最后一个元素删除
name_list.pop()
# pop 方法可以指定要删除元素的索引
name_list.pop(2)
# clear 方法可以清空列表
name_list.clear()




print(name_list)