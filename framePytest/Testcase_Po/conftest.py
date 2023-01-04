import logging
from Untlis.pageObject.pagebasc import Lover
from Untlis.public.read_ini import read_ini
import pytest

'''进行登录的功能，把鉴权加进header'''
@pytest.fixture(scope="package")
def login():
    Lover.Sdriver("edge")
    r = read_ini("bases.ini")
    data = r.data("bases")
    url = data["url"]
    name = data["name"]
    value = data["value"]
    Lover.open_Url(url)
    print("进行登录")
    Lover.maxwin()
    print("全屏")
    Lover.wait(120)
    print("隐性等待")
    cookies = {
        "name": name,
        "value": value
    }
    Lover.addcookies(**cookies)


    # getcookies=Lover.getcookies()
    # print("getcookies",getcookies)
    Lover.open_Url(url)
    # Lover.open_Url("https://mail.163.com/js6/main.jsp")
    return True

@pytest.fixture(scope="package",autouse=True)
def package_berfor(login):
    logging.info("--------Testcase_Api start--------!!")
    if login is False: #如果没更新鉴权则不测试
        pytest.skip() #跳过测试
    else: #更新就测试
        yield
    logging.info("--------Testcase_Api stop--------!!")