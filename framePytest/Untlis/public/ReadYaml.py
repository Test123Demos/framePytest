
#   __
#  /__)  _  _     _   _ _/   _
# / (   (- (/ (/ (- _)  /  _)
#          /

# import yaml

# def read_yaml(path):
#     with open(r'{}'.format(path), 'r', encoding='utf-8') as f:
#         return list(yaml.safe_load_all(f))
#
# print(read_yaml(r"D:\framePytest\Data\login.yaml"))

import yaml
class read_yaml():

    def read_yaml(self,path):
        with open(r'{}'.format(path), "r+", encoding="utf-8") as f:
            value = yaml.safe_load(stream=f)

            return value

    def result_list(self,path):
        value=self.read_yaml(path)
        data = list(value.values())
        return data

# print(read_yaml(r"F:\framePytest\Data\login.yaml"))
"""
1 json库的操作
    json.dumps() 将python对象编码成Json字符串
    json.loads() 将Json字符串解码成python对象
    json.dump()  将python中的对象转化成json储存到文件中
    json.load()  将文件中的json的格式转化成python对象提取出来
2 yaml库的操作
    yaml.safe_dump()        将一个python值转换为yaml格式文件
    yaml.safe_load()        将yaml格式文件转换为python值
    yaml.safe_dump_all()    将一序列的python值转换为yaml格式文件
    yaml.safe_load_all()    将yaml格式文件转换为python值
"""