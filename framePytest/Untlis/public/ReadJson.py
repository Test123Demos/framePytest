import json
import os
from Config.config_Path import Data_json_path
from Untlis.public.ParseData import ParseData


#cat -A 20 后面20行 -C 50 前后50行

class read_json():
    def __init__(self,filename:str):
        if  filename.__contains__(".json"):
            self.file=os.path.join(Data_json_path,filename)
            self.p=ParseData()
        else:
            raise Exception("file type is error!")

    def read(self):
        with open(file=self.file,mode="r") as f:
            data=json.loads(f.read())
            return data

    #获取键值当只有一个值时返回具体的值，当多个值时，返回多个值
    def read_list(self,key):
        data=self.read()
        result=self.p.result(key,data)
        return result

    def write(self,msg):
        with open(file=self.file,mode="w") as f:
            f.write(msg)

if __name__ == '__main__':
    rj=read_json("login.json")
    a=rj.read_list("loging")
    print(a)