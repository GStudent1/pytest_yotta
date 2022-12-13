# -*- coding:UTF-8 -*-

import pytest
from util.log import logger

from util.get_csv import readData
#
@pytest.mark.parametrize('test_data', readData())
class TestGetCSVData(object):
    def test_get_csv_data(self,test_data):
        data_list=test_data["data"]
        value_list=test_data["value"]
        print(data_list,value_list)
        # # for data in data_list:
        # assert_that(data_list,"data").is_not_empty()
        # # for value in value_list:
        # assert_that(value_list, "value").is_not_empty()




