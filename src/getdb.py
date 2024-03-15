# coding=utf-8
import sqlparse
import numpy as np
import pandas as pd
import jieba


import pymysql
databases =[
    "item_center",
    "price_center",
    "service_item",
    "service_order",
    "service_sourcing",
    "service_user",
    "supplier_center",
]
for database in databases:
    print("------------"+database+"--------------------------")
    conn_obj = pymysql.connect(
        host='127.0.0.1',  # MySQL服务端的IP地址
        port=3307,  # MySQL默认PORT地址(端口号)
        user='root',  # 用户名
        password='123456f',  # 密码,也可以简写为passwd
        database=database,  # 库名称,也可以简写为db
        charset='utf8'  # 字符编码
    )

    cursor = conn_obj.cursor()  # 括号内不写参数,数据是元组套元组
    cursor1 = conn_obj.cursor()  # 括号内不写参数,数据是元组套元组
    cursor2= conn_obj.cursor()  # 括号内不写参数,数据是元组套元组

    sql1 = 'show tables;'
    # 执行SQL语句
    tables = cursor.execute(sql1)
    # print(tables)
    data_result = cursor.fetchall()
    for  table in data_result :
        # print(table[0])
        #
        sql2 = 'select count(1) from '+table[0] +';'
        cursor1.execute(sql2)
        cnt1 =  cursor1.fetchall()
        # print(cnt1[0][0])
        if cnt1[0][0]>0 :
        # if cnt1[0][0]==0 :
        # 暂时只关心有数据的表
            print( 'select * from '+table[0] +';---->>',cnt1[0][0])
            print("********************************")
            tables = cursor2.execute('DESCRIBE '+ table[0] )
            result2 = cursor2.fetchall()
            for row2 in result2:
                print(row2)
            print("********************************")
            #查询相关表的字段类型与长度
    print("--------------------------------------")



