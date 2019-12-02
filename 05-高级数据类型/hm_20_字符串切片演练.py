#!/usr/bin/env python
# -*- coding: utf-8 -*-

num_str = "abcdefghi"

# 截取2-5位置的字符串
print(num_str[2:6])

# 截取2-末尾位置的字符串
print(num_str[2:])

# 截取从开始-5位置的字符串
print(num_str[0:6])

# 截取完整的字符串
print(num_str[:])

# 从开始位置，每隔一个字符截取字符串
print(num_str[::2])

# 从索引1开始，每隔一个取一个
print(num_str[1::2])

# 截取从2-末尾 -1的字符串
print(num_str[2:-1])

# 截取字符串末尾两个字符
print(num_str[-2:])

# 字符串的逆序（面试题）
print(num_str[::-1])

