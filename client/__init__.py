from client.http.leetcode_psm import  LeetcodePsm


class Client(object):
    @property
    def leet_code_psm(self):
        return LeetcodePsm()
