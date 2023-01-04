'''
本模块实现对webdriver类的二次封装
'''
import win32api
import win32con
import win32gui
import time
from  selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By




class Lover():
    driver=None
    #选择浏览器的驱动
    @classmethod
    def Sdriver(cls,name):
        name=name.lower()
        if name=="谷歌":
            cls.driver = webdriver.Chrome()
        elif name=="edge":
            cls.driver=webdriver.Edge()
        elif name=="火狐":
            cls.driver=webdriver.Firefox()

        elif name=="苹果":
            cls.driver=webdriver.Safari()
        else:
            raise Exception("输入的浏览器类型无效!请输入:谷歌 or Edge or 火狐 or 苹果")

    #打开网页
    @classmethod
    def open_Url(cls,url):
        cls.driver.get(url)


    #隐性等待
    @classmethod
    def wait(cls,time):
        cls.driver.implicitly_wait(time)

    #全屏
    @classmethod
    def maxwin(cls):
        cls.driver.maximize_window()

    #元素定位
    #element(”类型“,"元素定位的值")
    #args=((”类型“,"元素定位的值"))
    @classmethod
    def element(cls,*args):
        if len(args)==1:
            type=args[0][0].lower()
            value=args[0][1].lower()
            if type=="id":
                elementObject=cls.driver.find_element_by_id(value)
            elif type=="name":
                elementObject=cls.driver.find_element_by_name(value)
            elif type=="xpath":
                elementObject=cls.driver.find_element_by_xpath(value)
            elif type=="css":
                elementObject=cls.driver.find_element_by_css_selector(value)
            elif type=="class":
                elementObject=cls.driver.find_element_by_class_name(value)
            elif type=="a":
                elementObject=cls.driver.find_element_by_link_text(value)
            elif type=="tags":
                elementObject=cls.driver.find_elements_by_tag_name(value)
            else:
                raise Exception("您输入的定位方式不存在！")
            return elementObject
        else:
            raise Exception("您输入的参数有误，请检查！")

    #元素定位并点击
    @classmethod
    def eclick(cls,*args):
        print(args)
        cls.element(args[0]).click()


    #根据元素传入的对象进行点击
    @classmethod
    def click(cls,element):
        element.click()

    #元素定位并输入
    @classmethod
    def esend_keys(cls,value,*args):
        cls.element(args[0]).send_keys(value)

    #通过传入对象进行输入值
    @classmethod
    def send_keys(cls,element,value):
        element.send_keys(value)

    #显示等待
    #rtime 刷新的秒数
    #("type","值")
    @classmethod
    def webwait(cls,rtime,*args):
        if len(args)==1:
            type=args[0][0].lower()
            value=args[0][1].lower()
            if type=="css":
                elementObject=WebDriverWait(cls.driver, rtime, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
            elif type=="id":
                elementObject=WebDriverWait(cls.driver, rtime, 0.5).until(EC.presence_of_element_located((By.ID, value)))
            elif type=="name":
                elementObject=WebDriverWait(cls.driver, rtime, 0.5).until(EC.presence_of_element_located((By.NAME, value)))
            elif type=="class":
                elementObject=WebDriverWait(cls.driver, rtime, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
            elif type=="a":
                elementObject=WebDriverWait(cls.driver, rtime, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
            elif type=="tag":
                elementObject=WebDriverWait(cls.driver, rtime, 0.5).until(EC.presence_of_element_located((By.TAG_NAME, value)))
            elif type == "xpath":
                elementObject = WebDriverWait(cls.driver, rtime, 0.5).until(
                    EC.presence_of_element_located((By.XPATH, value)))

            else:
                raise  Exception("传入的类型错误！")
            return elementObject
        else:
            raise Exception("入参有误！")


    #通过js进行元素定位并输入值
    @classmethod
    #("类型"，”元素定位的值“，”输入的值“)
    def js_Sv(cls,*args):
        type=args[0][0].lower()
        value=args[0][1].lower()
        value1=args[0][2].lower()
        js=""
        if type=="id":
            js='''document.getElementById("{}").value="{}"'''.format(value,value1)
        elif type=="value":
            js='''document.getElementByName("{}").value="{}"'''.format(value,value1)
        cls.driver.execute_script(js)

    #js的点击
    @classmethod
    def Jclick(cls,*args):
        cls.driver.execute_script("arguments[0].click();", cls.element(args[0]))

    #js的滚轮
    @classmethod
    def Scroll(cls,value):
        js = "var d=document.documentElement.scrollTop={}".format(value)
        cls.driver.execute_script(js)

    #移动鼠标
    @classmethod
    def move(cls,element):
        ActionChains(cls.driver).move_to_element(element).perform()

    #定位元素并鼠标移动到这个元素上
    @classmethod
    def emove(cls,*args):
        ActionChains(cls.driver).move_to_element(cls.element(args[0])).perform()

    #按照传入的对象进行双击
    @classmethod
    def dclick(cls,element):
        ActionChains(cls.driver).double_click(element).perform()

    #定位到这个对象并双击
    @classmethod
    def edclick(cls,*args):
        ActionChains(cls.driver).double_click(cls.element(args[0])).perform()

    #上传文件
    @classmethod
    def upoldfile(cls,file):
        handle = win32gui.GetForegroundWindow()
        ComboBoxEx32 = win32gui.FindWindowEx(handle, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        button = win32gui.FindWindowEx(handle, 0, 'Button', "打开(&O)")  # 二级
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None,
                             r"{}".format(file))  # 发送文件路径
        win32gui.SendMessage(handle, win32con.WM_COMMAND, 1, button)  # 点击打开按钮

    '''
    # 向下按一次然后释放一次
    '''
    @classmethod
    def down_key(cls):
        # win32api:该函数原型：keybd_event(bVk, bScan, dwFlags, dwExtraInfo)
        # 第一个参数：虚拟键码（键盘键码建议网上搜下）；
        # 第二个参数：硬件扫描码，一般设置为0即可；
        # 第三个参数：函数操作的一个标志位，如果值为KEYEVENTF_EXTENDEDKEY则该键被按下，也可设置为0即可，如果值为KEYEVENTF_KEYUP则该按键被释放；
        # 第四个参数：定义与击键相关的附加的32位值，一般设置为0即可。

        # 40是虚拟键盘码，代表down键盘，第三个0代表按下的意思
        time.sleep(0.02)  # 时间不能去掉
        win32api.keybd_event(40, 0, 0, 0)  # 向下下按的功能
        time.sleep(0.02)  ##时间不能去掉
        # 40是虚拟键盘码，代表down键盘，win32con.KEYEVENTF_KEYUP代表释放的意思
        win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)

    '''
    # 按一下确认键
    '''
    @classmethod
    def enter_win32(cls):
        # 13是enter的虚拟键盘码
        time.sleep(0.02)
        win32api.keybd_event(13, 0, 0, 0)  # 13是enter的虚拟键盘码  第三个参数0 代表按下
        time.sleep(0.02)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # win32con.KEYEVENTF_KEYUP 释放的意思

    #获取当前的句柄
    @classmethod
    def handel(cls,type):
        handel=""
        if type=="one":
            handel=cls.driver.current_window_handle
        elif type=="all":
            handel=cls.driver.window_handles
        return handel

    #切换窗口
    @classmethod
    def switch_win(cls,handel):
        cls.driver.switch_to.window(handel)

    #根据元素的对象进入iframe
    @classmethod
    def eiframe(cls,*args):
        cls.driver.switch_to.frame(cls.element(args[0]))

    @classmethod
    def iframe(cls,value):
        cls.driver.switch_to.frame(value)

    #退出容器
    @classmethod
    def qiframe(cls):
        cls.driver.switch_to.default_content()

    #进入弹窗
    @classmethod
    def alert(cls):
        alert=cls.driver.switch_to.alert
        return alert

    #进入弹窗获取弹窗的值
    @classmethod
    def alert_text(cls):
        return cls.alert().text

    #进入弹窗点击确认
    @classmethod
    def accept(cls,alert):
        alert.accept()

    #进入弹窗点击取消
    @classmethod
    def dismiss(cls,alert):
        alert.dismiss()

    #获取浏览器的标题
    @classmethod
    def title(cls):
        return cls.driver.title

    #浏览器的刷新
    @classmethod
    def refresh(cls):
        cls.driver.refresh()

    #对象元素进行清并输入
    @classmethod
    def clear(cls,element,value):
        element.clear()
        cls.send_keys(element,value)

    #返回上一级
    @classmethod
    def back(cls):
        cls.driver.back()

    #退出浏览器
    @classmethod
    def quit(cls):
        cls.driver.quit()

    #关闭浏览器
    @classmethod
    def close(cls):
        cls.driver.close()

    #打开一个新窗口
    @classmethod
    def new_win(cls,url,type="_blank"):
        js = '''window.open('{}',type='{}')'''.format(url,type)
        cls.driver.execute_script(js)

    #选择下拉框("",("类型"，”元素定位的值“))
    @classmethod
    def Select(cls,type,*args):
        if type=="value":
            Select(cls.element(args[0])).select_by_value("7")  # value取值
        elif type=="text":
            Select(cls.element(args[0])).select_by_visible_text("湖南大学")  # text取
        elif type=="index":
            Select(cls.element(args[0])).select_by_index(3)  # 根据索引取
        else:
            raise Exception("传参类型错误！")

    #元素是否被选中
    @classmethod
    def isSelect(cls,element):
        return element.is_selected()

    #添加cookies
    @classmethod
    def addcookies(cls,**kwargs):
        cls.driver.add_cookie(kwargs)
    #获取cookies
    @classmethod
    def getcookies(cls,*args,**kwargs):
        return cls.driver.get_cookies(*args,**kwargs)
    ##获取定位元素的值
    @classmethod
    def get_attribute(cls,elment,vlaue):
        return elment.get_attribute(vlaue) #("value")

    #@classmethod
    def element_sx(cls,element,vlaue):
        return element.get_property(vlaue)

    #获取文本
    @classmethod
    def text(cls,element):
        return element.text