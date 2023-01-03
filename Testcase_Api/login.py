import logging
import json
from Untlis.public.HttpURLConnection import HttpURLConnection,mothed_tp
from Untlis.public.ReadYaml import read_yaml
from Untlis.public.ParseData import ParseData



class Authorization():
    header={}

    def __init__(self):
        self.yaml=read_yaml().read_yaml(r"D:\framePytest\Data\login_test.yaml")
        self.p = ParseData()
        self.session=HttpURLConnection()

    def code(self):
        try:
            data=self.yaml["code"]
            mothed = mothed_tp(data["mothed"])
            url = data["url"].lower()
            result = self.session.request(Method=mothed, url=url)
            return result.json()["uuid"]
        except Exception as error:
            logging.info(error)

    def login(self):
        uuid=self.code()
        data = self.yaml["login"]
        mothed = mothed_tp(data["mothed"])
        url = data["url"].lower()
        data["value"]["uuid"]=uuid
        value=data["value"]
        logging.info(json.dumps(value))
        result=self.session.request(Method=mothed,url=url,json=value)

        if result.json().__contains__("token"):
            logging.info(result.text)
            return result.json()["token"]
        else:
            return None
    def update_header(self):
        token=self.login()
        if token is not None:
            Authorization.header["Authorization"]=token

if __name__ == '__main__':
    # text=read_yaml().read_yaml(r"F:\framePytest\Data\login_test.yaml")
    # print(text)
    a=Authorization()
    b=a.update_header()
    # print(a.header)
    # print(Authorization.header)