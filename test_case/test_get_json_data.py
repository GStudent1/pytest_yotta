# -*- coding:UTF-8 -*-
import json
import allure
from assertpy import assert_that
from util import TEST_DATA

class TestGetJsonData(object):
    def test_get_json_data(self):
        allure.attach(body=json.dumps(TEST_DATA), name="test_get_json_data", attachment_type=allure.attachment_type.TEXT)
        print(TEST_DATA.get("lisi").get("age"))
        assert_that(TEST_DATA.get("lisi").get("age"),"lisi's age").is_equal_to(1)


