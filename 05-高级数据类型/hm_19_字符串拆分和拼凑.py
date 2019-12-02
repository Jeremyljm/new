#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 假设：以下内容是从网上抓取的
# 要求：
# 1. 将字符串的空白字符全部去掉
# 2. 再使用" "作为分隔符，拼接成一个整齐的字符串

poem_str = "登黄鹤楼\t 王之涣\t 白日依山尽\t \n 黄河入海流 \t \t欲穷千里目 \t更上一层楼"

print(poem_str)

# 1.拆分字符串
poem_list = poem_str.split()

print(poem_list)

# 2.合并字符串

result = " ".join(poem_list)
print(result)
