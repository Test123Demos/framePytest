import pytest


if __name__ == '__main__':
    import os

    # pytest.main(["-vs","Testcase_Api/Data_Driven/test_Super.py"])
    pytest.main(["-vs","Testcase_Po","--capture=sys"])
    # pytest.main(["-vs","Testcase_Api/Shop","--capture=sys","--html=./1report.html"])
    # pytest.main(["Testcase_Api/Shop"])
    # pytest.main(["-vs","Testcase_Api/test1_login.py"])
    # 指生成报告
    # os.system("allure generate Api_report -c -o allure-report")
    #指定端口生成和ip生成
    # os.system("allure  serve -h 192.168.0.142  -p 52313 F:\\framePytest\Report\Api_report")


