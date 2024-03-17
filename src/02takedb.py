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
print(tablse)
fr.close()

for tb in tablse:
    print("---------------")
    print(tb.databases,tb.tablseName[0], len(tb.fields))
    for fd in tb.fields:
        print(fd[0],fd[1],fd[2],fd[3],fd[4],fd[5])