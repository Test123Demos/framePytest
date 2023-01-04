import logging
from Untlis.public.login import Authorization
import pytest

'''进行登录的功能，把鉴权加进header'''
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
        pytest.skip() #跳过测试
    else: #更新就测试
        yield
    logging.info("--------Testcase_Api stop--------!!")