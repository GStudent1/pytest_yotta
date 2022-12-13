# -*- coding:UTF-8 -*-

from assertpy import assert_that
from util.log import logger


class TestLeetcode(object):
    def test_leetcode_problems(self,client):
        respon =client.leet_code_psm.leetcode_problems_api_favorites(
            referer="https://leetcode.cn/problemset/all/"
        )
        for resp in respon:
            assert_that(resp.get("id"), "resp_id").is_not_empty()
            assert_that(resp.get("name"), "resp_name").is_not_empty()

