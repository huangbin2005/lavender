# coding=utf-8
import pymysql

conn_obj = pymysql.connect(
    host='10.80.166.64',  # MySQL服务端的IP地址
    port=20005,  # MySQL默认PORT地址(端口号)
    user='root',  # 用户名
    password='M@ysql%ab34',  # 密码,也可以简写为passwd
    database='eos',  # 库名称,也可以简写为db
    charset='utf8'  # 字符编码
)

cursor = conn_obj.cursor()  # 括号内不写参数,数据是元组套元组
cursor1 = conn_obj.cursor()  # 括号内不写参数,数据是元组套元组


sql1 = 'show tables;'
# 执行SQL语句
tables = cursor.execute(sql1)
# print(tables)
data_result = cursor.fetchall()
for  table in data_result :
    print(table[0])
    sql2 = 'select count(1) from '+table[0] +';'
    cursor1.execute(sql2)
    cnt1 =  cursor1.fetchall()
    # print(cnt1[0][0])
    if cnt1[0][0]>0 :
    # if cnt1[0][0]==0 :
        print( 'select * from '+table[0] +';')



