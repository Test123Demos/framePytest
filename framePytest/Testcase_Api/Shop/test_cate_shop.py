import logging

import pytest
import allure
from Api.Cate.Shop import shop_class


@allure.epic("商品模块")
class Test_shop():

    @allure.title("添加商品")
    def test_001(self):
        shop_class.add()
        logging.error("添加商品成功！")
        assert 1==2