import configparser
from Config.config_Path import Data_path
# config=configparser.ConfigParser()
# config.read(filenames=r"F:\pageProject\Data\email.ini",encoding="utf-8")
# print(dict(list(config.items("basic"))))

# config=configparser.ConfigParser() #生成对象
# config.read(filenames=r"{}email.ini".format(path_D),encoding="utf-8")
# data=dict(config.items("basic")) #读取到的内容
# print(data)

class read_ini():
    def __init__(self,filename):
        self.config = configparser.RawConfigParser()  # 生成对象
        self.config.read(filenames=r"{}{}".format(Data_path,filename), encoding="utf-8")

    def data(self,section):
        data = dict(self.config.items(section))  # 读取到的内容
        return data
if __name__ == '__main__':
    # r=read_ini("email.ini")
    # print(r.data("basic"))
    print("{}bases.ini".format(Data_path))
    r = read_ini("bases.ini")
    data = r.data("case")
    print(data)