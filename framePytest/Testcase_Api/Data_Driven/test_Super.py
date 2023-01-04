import pytest
import logging
import allure
from Untlis.public.ReadYaml import read_yaml
from Untlis.public.HttpURLConnection import HttpURLConnection
from Untlis.public.ParseData import ParseData

'''#定义mothed的类型'''
def mothed_tp(mothed):
    mothed_type = ["post", "get", "put", "delete"]
    if mothed.lower() not in mothed_type:
        return False
    else:
        return mothed.lower()


'''定义parms'''
def parms_tp(parms):
    parms_type = ["json", "data", None,"parms"]
    if parms not in parms_type:
        return False
    else:
        if parms is not  None:
            return parms.lower()
        else:
            return None

def webapp(func):
    def app(*args,**kwargs):
        print("哈哈哈",args,kwargs)
        # @allure.title()
        def first(*args,**kwargs):
            func(*args,**kwargs)
        return first
    return app



@allure.epic("数据驱动")
@allure.feature("yaml参数")
class Test_super():

    def setup_class(self):
        self.session=HttpURLConnection()
        self.p=ParseData()
    @allure.title("用例的标题: 数据驱动")
    @allure.description("用例更详细的描述: 详细描述")
    @allure.severity("normal")#用例的级别:blocker阻塞缺陷,critical缺陷,normal一般缺陷,minor次要缺陷,trivial轻微缺陷
    @allure.story("用例的标题: 对会所资源进行增、删、改、查")
    @allure.issue("https://www.baidu.com")
    @allure.testcase("https://www.baidu.com")
    @allure.link("https://www.baidu.com")
    @pytest.mark.parametrize("data",read_yaml().result_list("./Data/yaml/login.yaml"))
    def test_run(self,data):
        mothed = mothed_tp(data["mothed"])
        url=data["url"].lower()
        parms=parms_tp(data["parms"])
        value=data["value"]
        token=data["token"]
        response=data["response"]
        logging.info("mothed: {}, url: {}, value: {}".format(mothed, url, value))
        if mothed and parms :
            headers={}
            if token !=None: #判断token不为空需要填写字典值
                headers.update(token)
            if parms=="json":
                result=self.session.request(Method=mothed,url=url,json=value,headers=headers)
            elif parms=="data":
                result=self.session.request(Method=mothed,url=url,data=value,headers=headers)
            elif parms is None:
                result=self.session.request(Method=mothed,url=url,headers=headers)
            logging.info(result.text)
            if isinstance(response,dict):
                a_text=self.p.result(list(response.items())[0][0],result.json())
                rv=list(response.items())[0][1]
                if a_text is not None:
                    if isinstance(a_text,int) or isinstance(a_text,str):
                        assert a_text==rv
                    else:
                        assert rv in a_text
                else:
                    assert rv==a_text

            elif response is not None and  not isinstance(response,dict) :
                assert result.text==str(response)
            else:
                assert result.status_code==200
        else:
            logging.info("mothed: {}, url: {}, value: {}, response: {}".format(mothed, url, value,response))



