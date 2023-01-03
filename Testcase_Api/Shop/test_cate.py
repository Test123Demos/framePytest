import pytest
import allure

@allure.title("我是cate的第一条用例!")
def test_01():
    print("我是cate的第一条用例!")

@allure.title("我是cate的第二条用例!")
@pytest.mark.skip
# @pytest.mark.one
def test_02():
    print("我是cate的第二条用例!")

@allure.title("我是cate的第三条用例!")
# @pytest.mark.one
def test_03():
    print("我是cate的第三条用例!")

@allure.title("我是cate的第四条用例!")
def test_04():
    print("我是cate的第四条用例!")
    pytest.fail()