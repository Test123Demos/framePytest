import pytest
import allure
from Api.Cate.Shop_Cate import cate_class
# n=0
# def berfor(func):
#     global n
#     n=n+1
#     @allure.title("我是cate的第{}条用例!".format(n))
#     def webapper(*args,**kwargs):
#         func(*args,**kwargs)
#     return webapper
#
# @allure.epic("Test_demo测试类")
# @allure.feature("demo类")
# class Test_demo():
#     # @allure.title("我是cate的第一条用例!")
#     @berfor
#     def test_01(self):
#         print("我是cate的第一条用例!")
#
#     # @allure.title("我是cate的第二条用例!")
#     @allure.severity("critical")
#     @pytest.mark.skip
#     @berfor
#     def test_02(self):
#         print("我是cate的第二条用例!")
@allure.epic("商品分类")
class Test_Cate():

    @allure.title("新增商品分类")
    def test_01(self):
        cate_class.add()
    @allure.title("查询商品分类")
    def test_02(self):
        cate_class.select()
