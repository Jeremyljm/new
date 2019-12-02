#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
import MY2


# change root password to yours:
conn = mysql.connector.connect(host='172.30.34.210', user='root', password='root', database='lijieming')

cursor = conn.cursor()
# 创建user表:
id_str = input("请输入id")
name_str = input("请输入姓名")
phone_str = input("请输入手机")
email_str = input("请输入电子邮箱")
test = {"id": id_str,
            "name": name_str,
            "phone": phone_str,
            "email": email_str}
cursor.execute('create table test')
# 插入一行记录，注意MySQL的占位符是%s:


# cursor.execute('insert into test')

# print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from test where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()