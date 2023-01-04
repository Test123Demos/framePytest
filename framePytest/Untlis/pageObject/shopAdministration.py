'''
本文件专门存放商品管理的元素定位
'''


class commodityList():
    #商品管理
    xpath = ("xpath",'''//div[@class="menu-wrapper"][3]/li/div''')
    # 商品管理的li
    xpath00 = ("xpath",'''//div[@class="menu-wrapper"][3]/li''')
    # 商品分类
    xpath01 = ("xpath",'''//li[@class='el-submenu is-active is-opened']/ul/div[1]/a''')
    #管理商品
    xpath02=("xpath",'''//li[@class='el-submenu is-active is-opened']/ul/div[2]/a''')
    #商品规格
    xpath03=("xpath",'''//li[@class='el-submenu is-active is-opened']/ul/div[3]/a''')

# def element(*args):
#     print(args)
# element(commodityList.xpath)
'''
商品分类的元素
'''
class commodityClassification():
    # 新增
    xpath01 = "xpath",'''//button[@class='el-button filter-item el-button--primary el-button--mini']'''
    # 修改：
    xpath02 = "xpath",'''//button[@class='el-button filter-item el-button--danger el-button--mini is-disabled']'''
    # 删除:
    xpath03 = "xpath",'''//button[@class='el-button filter-item el-button--danger el-button--mini is-disabled']'''
    # 导出:
    xpath04 = "xpath",'''//span[@class="crud-opts-left"]/button[4]'''
    # 搜索的输入框:
    xpath05 = "xpath",'''//span[@class="crud-opts-left"]/../../div/div/input'''
    # 搜索按钮:
    xpath06 = "xpath",'''//i[@class="el-icon-refresh-left"]/../../button[1]'''
    # 重置：
    xpath07 = "xpath",'''//i[@class="el-icon-refresh-left"]/../../button[2]'''
    # 列表删除的按钮:
    xpath08 = "xpath",'''//div[@class="el-table__fixed-right"]/div[2]/table/tbody/tr[1]/td[5]/div/div/span/span/button'''
    # 列表修改的按钮:
    xpath09 = "xpath",'''//div[@class="el-table__fixed-right"]/div[2]/table/tbody/tr[1]/td[5]/div/div/button'''
    # 分类名称输入框
    xpath10 = "xpath",'''//div[@class="el-form-item el-form-item--small"][1]/div/div/input'''
    # 分类图片按钮
    xpath11 = "xpath",'''//div[@class="el-form-item el-form-item--small"][2]/div/div/div[1]'''
    # 图片勾选框
    xpath12 = "xpath",'''//div[@class="el-col el-col-4"][1]/div/div/div[2]/label/span[1]'''
    # 图片确认
    xpath13 = "xpath",'''//button[@class='el-button el-button--default el-button--small']/../button[2]'''
    # 排序
    xpath14 = "xpath",'''//div[@class='el-form-item el-form-item--small'][4]/div/div/input'''
    # 上级分类的输入框
    xpath15 = "xpath",'''//div[@class="vue-treeselect__value-container"]/div[3]/input'''
    # 确认按钮
    xpath16 = "xpath",'''//form[@class='el-form']/../../div[3]/div/button[2]'''

#管理商品
class manageMerchandise():
    #新增商品
    xpath="xpath",'''//div[@id='pane-first']/div/div[1]/div[4]/button[1]'''
    #商品的名称
    xpath01="xpath",'''//div[@class='el-row'][1]/div[1]/div/div/div/input'''
    #商品分类选择框
    xpath02="xpath",'''//div[@class='el-row'][1]/div[2]/div/div/div/div/input'''
    #商品的关键字
    xpath03="xpath",'''//div[@class='el-row'][1]/div[3]/div/div/div/input'''
    #单位
    xpath04="xpath",'''//div[@class='el-row'][1]/div[4]/div/div/div/input'''
    #商品的简介
    xpath05="xpath",'''//div[@class='el-row'][1]/div[5]/div/div/div/textarea'''
    #商品封面图
    xpath06="xpath",'''//div[@class='el-row'][1]/div[6]/div/div/div/div/i'''
    #商品轮播图
    xpath07="xpath",'''//div[@class='el-row'][1]/div[7]/div/div/div/div/i'''
    #添加积分兑换图
    xpath08="xpath",'''//table[@class='el-table__body']/tbody/tr/td[1]/div/div/div[1]'''
    #售价
    xpath09="xpath",'''//table[@class='el-table__body']/tbody/tr/td[2]/div/div/input'''
    #成本价
    xpath10="xpath",'''//table[@class='el-table__body']/tbody/tr/td[3]/div/div/input'''
    #原价
    xpath11="xpath",'''//table[@class='el-table__body']/tbody/tr/td[4]/div/div/input'''
    #库存
    xpath12="xpath",'''//table[@class='el-table__body']/tbody/tr/td[5]/div/div/input'''
    #商品编号
    xpath13="xpath",'''//table[@class='el-table__body']/tbody/tr/td[6]/div/div/input'''
    #重量
    xpath14="xpath",'''//table[@class='el-table__body']/tbody/tr/td[7]/div/div/input'''
    #体积
    xpath15="xpath",'''//table[@class='el-table__body']/tbody/tr/td[8]/div/div/input'''
    #所需兑换积分
    xpath16="xpath",'''//table[@class='el-table__body']/tbody/tr/td[9]/div/div/input'''
    #运费模板选择框
    xpath17="xpath",'''//div[@class='el-row'][1]/div[11]/div/div/div/div/div/input'''
    #富文本的iframe的框的id
    id='''ueditor_0'''
    #文本输入框
    xpath18="xpath",'''//body[@class='view']'''
    #虚拟销量
    xpath19="xpath",'''//input[@placeholder='请输入虚拟销量']'''
    #购买积分
    xpath20="xpath",'''//input[@placeholder='请输入积分']'''
    #请输入排序
    xpath21="xpath",'''//input[@placeholder='请输入排序']'''
    #保存按钮
    # xpath22="xpath",'''//textarea[@id='ueditor_textarea_editorValue']/../div[4]/div/button'''
    xpath22="xpath",'''//*[@id="app"]/div/div[2]/section/div[1]/div/div/form/div[4]/div/button'''
    #选择图片
    xpath23="xpath",'''//div[@class='el-checkbox-group']/div[1]/div/div/div[2]/label/span[1]'''
    #确认图片按钮
    xpath24="xpath",'''//div[@class='v-modal']/../div[4]/div/div[3]/span/button[2]'''
    #编辑商品
    xpath25="xpath",'''//tr[@class='el-table__row'][1]/td[10]/div/button'''
    #删除商品
    xpath26="xpath",'''//tr[@class='el-table__row'][1]/td[10]/div/span/span/button'''
    #确认删除按钮
    xpath27="xpath",'''//div[@class='popper__arrow']/../div[1]/button[2]'''
    #搜索输入框
    xpath28="xpath",'''//div[@id='pane-first']/div/div[1]/div[1]/input'''
    #搜索的类型
    xpath29="xpath",'''//div[@id='pane-first']/div/div[1]/div[2]/div/input'''
    #搜索的商品分类
    xpath30="xpath",'''//div[@id='pane-first']/div/div[1]/div[3]/div/input'''
    #搜索按钮
    xpath31="xpath",'''//div[@id='pane-first']/div/div[1]/button'''

    # 选择图片
    xpath32 = "xpath",'''/html/body/div[5]/div/div[2]/section/main/div/div[2]/div/div[1]/div/div[1]/div/div/div[2]/label/span[1]/span'''
    # 确认图片按钮
    xpath33 = "xpath",'''/html/body/div[5]/div/div[3]/span/button[2]'''
