#!/usr/bin/env python
# -*- coding: utf-8 -*-

info_tuple = ("zhangsan", 18, 1.75)


# 1.取值和取索引
print(info_tuple[0])
# 已经知道数据的内容，希望知道该数据在元祖中的索引
print(info_tuple.index("zhangsan"))

# 2. 统计计数
print(info_tuple.count(18))

# 统计元祖中包含的元素的个数
print(len(info_tuple))








