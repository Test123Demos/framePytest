
#   __
#  /__)  _  _     _   _ _/   _
# / (   (- (/ (/ (- _)  /  _)
#          /

'''
本模块用于requets模块的二次封装，
把get，put,post,delet封装在一个方法中
'''
import requests
from Untlis.public.AllureVoid import Allurevoid,allure


class HttpURLConnection():

    def __init__(self):
        self.allure_v=Allurevoid()
    '''
    #发起请求的方法
    '''
    # @allure.step(title="-----发起接口请求-----")
    def request(self,Method,url,data=None,json=None,**kwargs):
        try:
            response=None
            method=Method.lower()
            if method=="post":
                response=self.__post(url,data=data, json=json, **kwargs)
            elif method=="get":
                response=self.__get(url, params=None, **kwargs)
            elif method=="put":
                response=self.__put(url, data=None, **kwargs)
            elif method=="delete":
                response=self.__delete(url, **kwargs)
            else:
                raise Exception("请求类型错误！！！！")
            #往allure报告中贴上附件
            body="请求前的数据:\nMethod:{}\nurl:{}\ndata:{}\njson:{}\nkwargs:{}\n请求后的数据:\nheaders:{}\ncode:{}\ntext:{}".format(Method,url,data,json,kwargs,response.headers,response.status_code,response.text)
            self.allure_v.attach_text(name="requets.txt",body=body)
            return response
        except Exception as error:
            body1 = "数据处理异常:\n{}".format(error)
            self.allure_v.attach_text(name="requets.txt", body=body1)
            print(error)

    '''
    #get请求方法
    '''
    @allure.step(title="-----发起get接口请求-----")
    def __get(self,url, params=None, **kwargs):
        try:
            with requests.get(url, params=params, **kwargs) as response:
                return response
        except Exception as error:
            print(error)

    '''
    #post请求方法
    '''
    @allure.step(title="-----发起post接口请求-----")
    def __post(self,url, data=None, json=None, **kwargs):
        requests.post(url)
        with requests.post(url=url, data=data, json=json, **kwargs) as response:
            return response

    '''
    #put请求方法
    '''
    @allure.step(title="-----发起put接口请求-----")
    def __put(self,url, data=None, **kwargs):

        with requests.put(url=url, data=data, **kwargs) as response:
            return response

    '''
    #delete请求方法
    '''
    @allure.step(title="-----发起delete接口请求-----")
    def __delete(self,url, **kwargs):

        with requests.delete(url=url, **kwargs) as response:
            return response



if __name__ == '__main__':

    '''
    #
    #调试
    #
    '''

    '''获取code'''
    a=HttpURLConnection().request("get","http://manage.duoceshi.com/auth/code")
    uuid=a.json()["uuid"]

    '''获取token'''
    body={"username":"admin","password":"oeO6NV/rAsT+reM7DqAjdmZ/Bz0jCDO7mWpQqQaFHMjhsSdSQhKap3QjkZOS1EYuzDZt3VuLsho/7RH7lANi4Q==","code":"8888","uuid":uuid}
    b=HttpURLConnection().request("post","http://manage.duoceshi.com/auth/login",json=body)
    token=b.json()["token"]

    '''查询数据'''
    header={
        "Authorization":token,
        "keep_alive":"False"
    }
    c=HttpURLConnection().request("get",url="http://manage.duoceshi.com/api/yxStoreCategory?page=0&size=10&sort=sort%2Cdesc",headers=header)
    print(c.text)