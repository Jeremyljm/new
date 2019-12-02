#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 记录所有的名片字典
card_list = []

def show_menu():

    """显示菜单"""
    print("*" * 50)
    print("欢迎使用名片管理系统")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("0.退出系统")
    print("*" * 50)

def new_card():

    """新增名片"""
    print("-" * 50)
    print("新增名片")

    name_str = input("请输入姓名")
    phone_str = input("请输入手机号码")
    qq_str = input("请输入qq号")
    email_str = input("请输入电子邮箱")

    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    card_list.append(card_dict)

    print(card_list)

    print("新增用户 %s 成功" % name_str)
    
def show_all():
    
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    if len(card_list) == 0:

        print("当前没有任何名片记录，请使用新增功能添加名片")

        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:

        print(name, end="\t\t")
    # 打印分割线
    print("")

    print("=" * 50)

    for card_dict in card_list:

        print("%s\t\t%s\t\t%s\t\t%s\t\t" %(card_dict["name"],
                                           card_dict["phone"],
                                           card_dict["qq"],
                                           card_dict["email"]))

def search_card():

    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    find_name = input("请输入要搜索的姓名：")

    for card_dict in card_list:

        if card_dict["name"] == find_name:

            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"]))
            deal_card(card_dict)

            break
    else:
        print("抱歉没有找到，%s" %find_name )

def deal_card(find_dict):

    print(find_dict)

    action_str = input("请选择要执行的操作"
                       "[1] 修改 [2] 删除 [0] 返回上级菜单")

    if action_str == "1":

        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ：")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：")
        print("修改名片成功")

    elif action_str == "2":

        card_list.remove(find_dict)
        print("删除名片成功")

def input_card_info(dict_value, tip_message):

    """输入名片信息
    :rtype: dict_value: 字典中原有的值
            tip_message: 输入的提示文字
            return：如果用户输入了内容就返回内容，否则返回原有的值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)

    # 2.针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:

        return result_str

    # 3.如果没有输入内容返回字典中原有的值
    else:
        return dict_value
