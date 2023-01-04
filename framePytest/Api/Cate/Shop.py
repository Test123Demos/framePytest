from Untlis.public.HttpURLConnection import HttpURLConnection
from Untlis.public.login import Authorization
from Api.Cate.Shop_Cate import cate_class
import logging

session=HttpURLConnection()
class  shop_class():

    @classmethod
    def add(cls):
        url = "http://manage.duoceshi.com/api/yxStoreProduct/addOrSave"
        method = "post"
        body = {"imageArr":[],"sliderImageArr":[],"store_name":"飒飒撒00","cate_id":cate_class.cate_id,"keyword":"都是","unit_name":"1","store_info":"1","image":"http://127.0.0.1:8001/file/pic/20221207215749885121.jpg","slider_image":["http://127.0.0.1:8001/file/pic/20221207215749885121.jpg"],"description":"<p>大多数</p>","ficti":0,"give_integral":0,"sort":0,"is_show":1,"is_hot":0,"is_benefit":0,"is_best":0,"is_new":0,"is_good":0,"is_postage":0,"is_sub":0,"is_integral":0,"id":0,"spec_type":0,"temp_id":280,"attrs":[{"imageArr":[],"pic":"http://127.0.0.1:8001/file/pic/20221207215749885121.jpg","price":2,"cost":0,"ot_price":0,"stock":"10","seckill_stock":0,"seckill_price":0,"pink_stock":0,"pink_price":0,"bar_code":"","weight":0,"volume":0,"brokerage":0,"brokerage_two":0,"integral":0}],"items":[],"header":[],"selectRule":""}

        with session.request(Method=method, url=url, json=body, headers=Authorization.header) as r:
            print(r.status_code)
            logging.info(r.status_code)



if __name__ == '__main__':
    a=Authorization()
    a.login()
    a.update_header()
    cate_class.add()
    cate_class.select()
    shop_class.add()
    print(a.header)
    print(cate_class.cate_id)
