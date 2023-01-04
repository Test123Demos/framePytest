import pytest
import allure
import time
from Untlis.pageObject.pagebasc import Lover
from Untlis.pageObject.shopAdministration import commodityList,commodityClassification,manageMerchandise

#管理商品
@allure.epic("管理商品")
class Test_shop():
    # driver = None
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.driver = Case02.driver

        # 每日条用例执行前
    @allure.title("每条用例执行前")
    def setup(self):
        print("每条用例执行前执行一次！")
        # text = Case02.driver.find_element_by_xpath(commodityList.xpath00).get_attribute("class")
        text = Lover.get_attribute(Lover.element(commodityList.xpath00), "class")
        print(text)
        if text != "el-submenu is-active is-opened":
            Lover.eclick(commodityList.xpath)
            # Case02.driver.find_element_by_xpath(commodityList.xpath).click()
        # 点击管理商品
        Lover.eclick(commodityList.xpath02)
        # Case03.driver.find_element_by_xpath(commodityList.xpath02).click()

    # 新增商品
    @allure.title("新增商品")
    def test_01(self):
        #点击商品新增的按钮
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath).click()
        Lover.eclick(manageMerchandise.xpath)
        #输入商品的名称
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath01).send_keys("小白子")
        Lover.esend_keys("小白子",manageMerchandise.xpath01)
        #选择商品分类
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath02).click()
        Lover.eclick(manageMerchandise.xpath02)
        time.sleep(1)
        Lover.down_key()
        time.sleep(1)
        Lover.enter_win32()
        #输入商品的关键字
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath03).send_keys("牛牛")
        Lover.esend_keys("牛牛",manageMerchandise.xpath03)
        #输入单位
        Lover.esend_keys("dcs", manageMerchandise.xpath04)
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath04).send_keys("dcs")
        #输入商品的简介
        Lover.esend_keys("dcs", manageMerchandise.xpath05)
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath05).send_keys("dcs")
        #选择商品的封面图
        Lover.eclick(manageMerchandise.xpath06)
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath06).click()
        #选择图片
        Lover.eclick(manageMerchandise.xpath23)
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath23).click()

        '''
        #滚动到积分界面
        '''
        # for i in range(1000,11000,1000):
        #     time.sleep(1)
        #     js = "var d=document.documentElement.scrollTop={}".format(i)
        #     Case03.driver.execute_script(js)

        #点击确认
        # ele1=Case03.driver.find_element_by_xpath(manageMerchandise.xpath24)
        # Case03.driver.execute_script("arguments[0].click();", ele1)
        Lover.Jclick(manageMerchandise.xpath24)
        #选择商品轮播图
        Lover.eclick(manageMerchandise.xpath07)
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath07).click()
        # 选择图片
        Lover.eclick(manageMerchandise.xpath32)

        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath32).click()
        # 点击确认
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath24).click()
        # ele1 = Case03.driver.find_element_by_xpath(manageMerchandise.xpath33)
        # Case03.driver.execute_script("arguments[0].click();", ele1)
        Lover.Jclick(manageMerchandise.xpath33)
        '''
               #滚动到积分界面
               '''
        # js = "var d=document.documentElement.scrollTop={}".format(700)
        # Case03.driver.execute_script(js)
        Lover.Scroll(700)
        #选择开启积分的图片
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath08).click()
        # 选择图片
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath23).click()
        # 点击确认
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath24).click()
        #输入售价

        # x09=Case03.driver.find_element_by_xpath(manageMerchandise.xpath09)
        # x09.clear()
        # x09.send_keys("10")
        Lover.clear(Lover.element(manageMerchandise.xpath09),"10")
        #成本价
        # x10 = Case03.driver.find_element_by_xpath(manageMerchandise.xpath10)
        # x10.clear()
        # x10.send_keys("10")
        ele=Lover.element(manageMerchandise.xpath10)
        Lover.clear(ele, "10")

        # 原价
        # x11 = Case03.driver.find_element_by_xpath(manageMerchandise.xpath11)
        # x11.clear()
        # x11.send_keys("10")
        Lover.clear(Lover.element(manageMerchandise.xpath11),"10")


        #库存
        # x12 = Case03.driver.find_element_by_xpath(manageMerchandise.xpath12)
        # x12.clear()
        # x12.send_keys("10")
        Lover.clear(Lover.element(manageMerchandise.xpath12),"10")


        #商品编号
        # x13 = Case03.driver.find_element_by_xpath(manageMerchandise.xpath13)
        # x13.clear()
        # x13.send_keys("10")
        Lover.clear(Lover.element(manageMerchandise.xpath13), "10")
        #商品重量
        # x14 = Case03.driver.find_element_by_xpath(manageMerchandise.xpath14)
        # x14.clear()
        # x14.send_keys("10")
        Lover.clear(Lover.element(manageMerchandise.xpath14), "10")


        # 商品体积
        # x15 = Case03.driver.find_element_by_xpath(manageMerchandise.xpath15)
        # x15.clear()
        # x15.send_keys("10")
        Lover.clear(Lover.element(manageMerchandise.xpath15), "10")


        #商品积分
        # x16 = Case03.driver.find_element_by_xpath(manageMerchandise.xpath16)
        # x16.clear()
        # x16.send_keys("10")
        Lover.clear(Lover.element(manageMerchandise.xpath16), "10")
        #运费模板
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath17).click()
        Lover.eclick(manageMerchandise.xpath17)
        time.sleep(1)
        Lover.down_key()
        time.sleep(1)
        Lover.enter_win32()
        #进入富文本的ifarme
        # Case03.driver.switch_to.frame(manageMerchandise.id)
        Lover.iframe(manageMerchandise.id)
        #输入文本的内容
        Lover.esend_keys("dcs",manageMerchandise.xpath18)
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath18).send_keys("dcs")
        #退出iframe框
        # Case03.driver.switch_to.default_content()
        Lover.qiframe()

        '''
        #滚动到虚拟销量
        '''
        # js = "var d=document.documentElement.scrollTop={}".format(1000)
        # Case03.driver.execute_script(js)
        Lover.Scroll(1000)
        #输入虚拟销量
        # x17 = Case03.driver.find_element_by_xpath(manageMerchandise.xpath19)
        # x17.clear()
        # x17.send_keys("10")
        Lover.clear(Lover.element(manageMerchandise.xpath19),"10")
        # 输入购买积分
        # x18 = Case03.driver.find_element_by_xpath(manageMerchandise.xpath20)
        # x18.clear()
        # x18.send_keys("10")
        Lover.clear(Lover.element(manageMerchandise.xpath20), "10")

        # 输入排序
        # x19 = Case03.driver.find_element_by_xpath(manageMerchandise.xpath21)
        # x19.clear()
        # x19.send_keys("10")
        Lover.clear(Lover.element(manageMerchandise.xpath21), "10")

        time.sleep(1)
        # js = "var d=document.documentElement.scrollTop={}".format(10000)
        # Case03.driver.execute_script(js)
        Lover.Scroll(10000)
        time.sleep(1)
        #点击保存按钮
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath22).click()
        # Lover.eclick(manageMerchandise.xpath22)
        Lover.click(Lover.webwait(20,manageMerchandise.xpath22))
        # Lover.driver.find_element_by_xpath(manageMerchandise.xpath22).click()

        text=Lover.element(("xpath",'''//div[@class='el-tabs__content']/div[1]/div/div[2]/div[3]/table/tbody/tr[1]/td[3]''')).text
        assert text=="小白子1"
    @allure.title("修改商品")
    def test_02(self):
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath25).click()
        Lover.eclick(manageMerchandise.xpath25)
        # js = "var d=document.documentElement.scrollTop={}".format(10000)
        # Case03.driver.execute_script(js)
        Lover.Scroll(10000)
        time.sleep(1)
        # js = "var d=document.documentElement.scrollTop={}".format(5000)
        # Case03.driver.execute_script(js)
        Lover.Scroll(5000)
        # 点击保存按钮
        # Case03.driver.find_element_by_xpath(manageMerchandise.xpath22).click()
        Lover.eclick(manageMerchandise.xpath22)



    def teardown(self):
        print("我点击了商品管理")
        # Lover.refresh()
        time.sleep(5)
        Lover.Jclick(("xpath",'''//div[@class="menu-wrapper"][3]/li/div/i'''))

