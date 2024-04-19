# coding=utf-8
__author__ = 'laohuang'

import pymysql
import pickle

databases =[
    "item_center",
    "price_center",
    "service_item",
    "service_order",
    "service_sourcing",
    "service_user",
    "supplier_center",
]

class Table :
    databases = ""
    tablseName = ''
    fields=[]
    def __init__(self, databases = '', tablseName="",field=[]):
        # 下面为Person对象增加2个实例变量
        self.databases = databases
        self.tablseName = tablseName
        self.fields = field
    def show(self):
        print(self.databases,self.tablseName, len(self.fields))




# 可能有问题的字段有：
# shop_id  、 sku_id   、  item_id、item_type
tablse = []

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
            fields = []
            for row2 in result2:
                fields.append(row2)
                # print(row2)
            tablse.append( Table(database,table,fields))
            print("********************************")
            print()
            #查询相关表的字段类型与长度
    print("--------------------------------------")

# 此处将查询结果做持久化的处理
# for tb in tablse:
#     print(tb.databases,tb.tablseName, len(tb.fields))

fw = open('d://workspaces//python-project//tables.pkl','wb')
# Pickle the list using the highest protocol available.
pickle.dump(tablse, fw, pickle.HIGHEST_PROTOCOL)
fw.close()




