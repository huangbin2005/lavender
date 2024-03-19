# coding=utf-8
__author__ = 'laohuang'

import pickle

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


fr = open('d://workspaces//python-project//tables.pkl','rb')
tablse = pickle.load(fr)
# print(tablse)
fr.close()

# 将各个字段处理为相同的类
class FieldDetail:
    databases = ''
    tablseName = ''
    fieldName =''
    type = ''

# 有不同的类型的的同名或类同名字段合并统计
class DiffFieldName :
    tablseName = ''
    fields=[]
    # 0是类型都一致，1是类型不一致
    isdiff = 0;
    def __init__(self, tablseName="",field=[]):
        # 下面为Person对象增加2个实例变量
        self.tablseName = tablseName
        self.fields = field
    def show(self):
        print(self.tablseName, len(self.fields))
# 1、 先把所有同名字段都放到一起
fieldDetails = []
# 1.1 所有字段摊平
for tb in tablse:
    # print("---------------")
    print(tb.databases,tb.tablseName[0], len(tb.fields))
    for fd in tb.fields:
        fdt =FieldDetail()
        fdt.databases=tb.databases
        fdt.tablseName=tb.tablseName[0]
        fdt.fieldName = str(fd[0])
        fdt.type = fd[1]
        # print(fd[0],fd[1],fd[2],fd[3],fd[4],fd[5])
        fieldDetails.append(fdt)
# 2、 再把类型不一致的打上标签
for fd in fieldDetails:
    print(fd.databases,fd.tablseName,fd.fieldName,fd.type)



# 3、 输出出类型不一致的详情
# for tb in tablse:
#     print("---------------")
#     print(tb.databases,tb.tablseName[0], len(tb.fields))
#     for fd in tb.fields:
#         print(fd[0],fd[1],fd[2],fd[3],fd[4],fd[5])
for fd in fieldDetails:
    print(fd.databases,fd.tablseName,fd.fieldName,fd.type)









