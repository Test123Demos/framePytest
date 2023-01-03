import pytest


if __name__ == '__main__':
    import os

    # pytest.main(["-vs","Testcase_Api/Data_Driven/test_Super.py"])
    # pytest.main(["-vs","Testcase_Api/Shop","-m","one"])
    pytest.main(["-vs", "Testcase_Api/Shop"])
    # pytest.main(["-vs","Testcase_Api/test1_login.py"])
    # 指生成报告
    # os.system("allure generate Api_report -c -o allure-report")
    #指定端口生成和ip生成
    # os.system("allure  serve -h 127.0.01  -p 52313 D:\\framePytest\Report\Api_report")


