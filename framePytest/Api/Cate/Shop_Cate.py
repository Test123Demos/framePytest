from Untlis.public.HttpURLConnection import HttpURLConnection
from Untlis.public.login import Authorization
import logging

session=HttpURLConnection()
#新增分类
class cate_class():
    cate_id=None
    @classmethod
    def add(cls):
        url="http://manage.duoceshi.com/api/yxStoreCategory"
        method="post"
        body={"id":None,
              "cateName":"232233243",
              "pid":1811,
              "isShow":1,
              "sort":1,
              "pic":"http://127.0.0.1:8001/file/pic/20221207215749885121.jpg"
              }
        with session.request(Method=method,url=url,json=body,headers=Authorization.header) as r:
            print(r.text)
            logging.info(r.text)

    @classmethod
    def select(cls):
        url = "http://manage.duoceshi.com/api/yxStoreCategory?page=0&size=10&sort=sort,desc"
        method="get"
        with session.request(Method=method,url=url,headers=Authorization.header) as r:
            cls.cate_id=r.json()["content"][-1]["id"]
            logging.info(r.json()["254"])




if __name__ == '__main__':
    a=Authorization()
    a.login()
    a.update_header()
    cate_class.add()
    cate_class.select()
    print(a.header)
    print(cate_class.cate_id)
