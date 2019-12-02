#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

class Mysql:

    def __init__(self, host, user, pwd, db):

        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8")
        # 打开游标
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        # 执行sql语句，获取所有数据
        print(sql)
        cur.execute(sql)
        #resList是list，而其中的每个元素是 tuple
        resList = cur.fetchall()
        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList



    def ExecNonQuery(self, sql):
        """
        执行非查询语句
        """
        cur = self.__GetConnect()
        # 执行sql语句，修改数据
        cur.execute(sql)
        # 执行sql语句
        self.conn.commit()
        self.conn.close()

def main(opType,sql):

    #获取数据库对象
    ms = Mysql(host="172.30.34.210", user="root", pwd="root", db="lijieming")

    if opType == "YES":
        #进行数据库查询
        resList = ms.ExecQuery(sql)
        # for (account,password,typeData) in resList:
        return resList
    elif opType == "NO":
        #进行非查询操作
        ms.ExecNonQuery(sql)
    else:
        print("程序在判断操作类型处出错！请检查，出错地址：SQLOperation.py文件")

if __name__ == '__main__':
    main(opType='YES', sql="select * from books")








# config = {'host': '172.30.34.210',
#           'port': '3306',
#           'user': 'root',
#           'password': 'root',
#           'charset': 'utf8mb4',
#           'cursorclass': pymysql.cursors.DictCursor}
#
# conn = pymysql.connect(**config)
# conn.autocommit()
# cursor = conn.cursor()