import json

import allure
import requests


def send_request(url,headers,params):
    host = "https://api16-normal-vpc2-useast5.us.tiktokv.com"
    resp=requests.get(url=host+url,headers=headers,params=params)
    allure.attach(body=json.dumps(json.loads(resp.text)),name=url,attachment_type=allure.attachment_type.TEXT)
    return resp.text