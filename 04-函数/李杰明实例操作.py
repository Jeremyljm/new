#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 设置初始用户名和登录密码；
# 进入登录页面，提醒输入用户输入用户名和密码；
# 若用户名输错则重新输入，若用户登录密码输错三次则重新开始输入用户名和用户登录密码；

username = "ljm"
password = "123"

flag0 = 0
flag1 = 0

print('>>>用户登录<<<')

while True:
    user = input('请输入用户名')
    if user == username:

        while flag0 < 3:
            pwd = input("请输入密码")
            if pwd == password:
                print("登录成功")
                flag1 = 1
                break
            else:
                flag0 += 1
            if flag0 <= 2:
                print("密码错误，请重新输入")

        if flag1 == 1:
            break
        flag0 = 0
        print("你已经输入错误三次了")
    else:
        print("用户名错误请重新输入")
