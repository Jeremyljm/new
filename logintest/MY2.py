#!/usr/bin/env python
# -*- coding: utf-8 -*-

test = []

def new_man():

    id_str = input("请输入id")
    name_str = input("请输入姓名")
    phone_str = input("请输入手机")
    email_str = input("请输入电子邮箱")
    list = {"id": id_str,
            "name": name_str,
            "phone": phone_str,
            "email": email_str}
    test.append(list)

    print(test)


