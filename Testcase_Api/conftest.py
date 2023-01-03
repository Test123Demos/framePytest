import logging
from Testcase_Api.login import Authorization
import pytest

'''登录函数'''
@pytest.fixture(scope="package")
def login():
    Authorization().update_header()
    if "Authorization" in Authorization.header: #判断更新鉴权没
        return True
    else:
        return False

@pytest.fixture(scope="package",autouse=True)
def package_berfor(login):
    logging.info("--------Testcase_Api start--------!!")
    if login is False: #如果没更新鉴权则不测试
        pytest.skip()
    else: #更新就测试
        yield
    logging.info("--------Testcase_Api stop--------!!")