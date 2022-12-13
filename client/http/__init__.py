import json

import allure
import requests


def send_request(url,headers=None,params=None):
    resp=requests.get(url=url,headers=headers,params=params)
    allure.attach(body=json.dumps(json.loads(resp.text)),name=url,attachment_type=allure.attachment_type.TEXT)
    return json.loads(resp.text)