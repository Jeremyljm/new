#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1.有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j ) and (i != k) and (j != k):

                print(i ,j ,k)


# 2.复制表格到另外一个表格
list1 = [11, 22, 33]
list2 = list1[:]

# list2.extend(list1)
print(list2)


# 3.九九乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (i, j, i * j), end="\t"),
    print("")


