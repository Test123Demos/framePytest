
#   __
#  /__)  _  _     _   _ _/   _
# / (   (- (/ (/ (- _)  /  _)
#          /

'''
#本模块用于数据解析
#使用的场景：在数据中查找某个键值
#还可以替换，条件替换
'''

import queue

class ParseData():
    def __init__(self):
        #创建队列,用来存储查找出来的值
        self.__q=queue.Queue(maxsize=10000)
        #创建查询到的数据
        self.data=[]

    #判断两个字典的键值是否相等
    def not_invalid(self,data,basedata):
        try:
            l=[] #用来存储以下判断键值都通过的个数
            if isinstance(data,dict) and isinstance(basedata,dict):#判断两个参数的值是不是都是字典
                for i in data.keys(): #变量条件的键
                    if basedata.__contains__(i): #判断元数据中是否有这个键
                        if data[i]==basedata[i]: #判断这个条件中键值和原数据中的键值是否相等
                            l.append(True) #相等则添加元素True
                if len(l)==len(list(data.keys())): #判断l列表的长度，如果长度跟键的长度一直，说明以上判断所有键值都通过
                    return True
                else:
                    return False
            else:
                raise Exception("data和basedata的值不是字典类型！！！")
        except Exception as error:
            print(error)
    '''
    #key:要找的键
    #data:找的数据
    #replace:替换的数据
    #当replace=None时，该函数会查出所有键值
    #当replace!=None时，该函数会进行替换键值
    #当replace!=None时condition为条件
    '''
    def __parse(self,key,data,replace=None,condition=None):
        try:
            if isinstance(data,dict): #判断是不是字典类型的数据
                for i in data: #遍历字典的键
                    if i==key: #如果键==要查的键
                        if replace==None: #如果不需要替换
                            self.__q.put(data[key]) #把查找到的数据赛道队列
                        else:#如果要替换，则进行替换
                            if condition==None:
                                data[key]=replace
                            else:
                                if self.not_invalid(condition,data):
                                    data[key]=replace
                    else: #如果键值不等于,执行递归
                        self.__parse(key,data[i],replace,condition)
            #判断数据的类型是元组，列表，可变集合，不可变集合时，循环递归
            elif isinstance(data,tuple) or isinstance(data,list) or isinstance(data,set) or isinstance(data,frozenset):
                for i in data:
                    self.__parse(key,i,replace,condition)
        except Exception as error:
            print(error)


    '''
    #组装parse函数得到的结果
    '''
    def __response(self):
        try:
            while not self.__q.empty():
                self.data.append(self.__q.get())
        except Exception as error:
            print(error)

    '''
    #获取查询数据的结果
    #当查询的数据只有一个时，直接返回这个数据
    #当查询的数据有多个时，返回list数据
    '''
    def __parseRulst(self,key,data):
        try:
            self.__parse(key,data)
            self.__response()

            if len(self.data)==1:
                return self.data[0]
            elif len(self.data)==0:
                return None
            else:
                return self.data
        except Exception as error:
            print(error)

    '''
    #获取替换后的数据
    '''
    def __paserRelace(self,key,data,replace=None,condition=None):
        try:
            if replace!=None: #判断replace不为None
                self.__parse(key, data,replace=replace,condition=condition)
                return data
            else:
                raise Exception("condition值存在时，replace必须不能为None")
        except Exception as error:
            print(error)

    '''
    #统一调用该函数
    #当replace==None时认为是查询值，查询出的值只有一个时就返回该值，有多个值时，返回列表
    #当replace!=None认为是替换值,condition为条件，要传入字典形势，只限跟key同级
    '''
    def result(self,key,data,replace=None,condition=None):

        try:
            if replace!=None:
                return self.__paserRelace(key,data,replace=replace,condition=condition)
            else:
                return self.__parseRulst(key,data)
        except Exception as error:
            print(error)





if __name__ == '__main__':
    '''
    #调试
    '''
    DICT1 = {"KEY": "KEY1",
             "LIST1": [{"KEY": "KEY2","key3":"11"}, {"KEY": "KEY3"}],
             "TUPLE2": ({"T1": ({"KEY": {"KEY4": "111"}})})
             }
    p=ParseData()
    a=p.result("KEY",DICT1)
    print(a)
    a=p.result("KEY",DICT1,"哈哈",{"key3":"11"})
    print(a)
    dict1={"1":"1"}
    print(list(dict1.items()))
