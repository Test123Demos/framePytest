#配置每个包路径的变量

import os
'''
####################################################
####################################################
####################################################
'''


'''#获取项目路径'''
path=os.path.dirname(os.path.dirname(__file__))

'''API包路径'''
Api_path=os.path.join(path,"Api","")

'''Config包的路径'''
Config_path=os.path.join(path,"Config","")

'''Report目录的路径'''
Report_path=os.path.join(path,"Report","")

'''Testcase_Api包的路径'''
Teacase_Apipath=os.path.join(path,"Testcase_Api","")

'''Testcase_Po包的路径'''
Testcase_Popath=os.path.join(path,"Testcase_Po","")

'''Untils包的路径'''
Untlis_path=os.path.join(path,"Untils","")

'''Data包的路径'''
Data_path=os.path.join(path,"Data","")

