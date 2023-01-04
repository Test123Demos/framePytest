import pytest
import allure
from Untlis.pageObject.pagebasc import Lover
from Untlis.pageObject.shopAdministration import commodityList,commodityClassification,manageMerchandise

@allure.epic("UI商品分类")
class Test_cate():

    # 每日条用例执行前
    @allure.title("商品模块每条用例执行前")
    def setup(self) -> None:
        print("每条用例执行前执行一次！")
        # text = Lover.driver.find_element_by_xpath(commodityList.xpath00).get_attribute("class")
        text = Lover.get_attribute(Lover.element(commodityList.xpath00), "class")
        print(text)
        if text != "el-submenu is-active is-opened":
            Lover.eclick(commodityList.xpath)
            # Case02.driver.find_element_by_xpath(commodityList.xpath).click()

    # 添加商品分类
    @allure.title("添加商品分类")
    def test_01(self):
        # 点击商品分类
        Lover.eclick(commodityList.xpath01)
        # Case02.driver.find_element_by_xpath(commodityList.xpath01).click()
        # 点击新增
        Lover.eclick(commodityClassification.xpath01)
        # Case02.driver.find_element_by_xpath(commodityClassification.xpath01).click()
        # 输入分类名称
        Lover.esend_keys("我是numberone!", commodityClassification.xpath10)
        # Case02.driver.find_element_by_xpath(commodityClassification.xpath10).send_keys("我是numberone!")
        # 点击分类图片
        Lover.eclick(commodityClassification.xpath11)
        # Case02.driver.find_element_by_xpath(commodityClassification.xpath11).click()
        # 选择图片
        Lover.eclick(commodityClassification.xpath12)
        # Case02.driver.find_element_by_xpath(commodityClassification.xpath12).click()
        # 点击确认
        Lover.eclick(commodityClassification.xpath13)
        # Case02.driver.find_element_by_xpath(commodityClassification.xpath13).click()
        # 输入排序
        Lover.esend_keys("2", commodityClassification.xpath14)
        # Case02.driver.find_element_by_xpath(commodityClassification.xpath14).send_keys("2")
        # 上级分类输入框
        Lover.esend_keys("品新茶", commodityClassification.xpath15)
        # Case02.driver.find_element_by_xpath(commodityClassification.xpath15).send_keys("品新茶")

        Lover.down_key()
        # down_key()
        Lover.enter_win32()
        Lover.eclick(commodityClassification.xpath16)
        # Case02.driver.find_element_by_xpath(commodityClassification.xpath16).click()
        assert 1==2
