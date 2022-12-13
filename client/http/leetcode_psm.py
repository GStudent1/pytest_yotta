from client.http import send_request

class LeetcodePsm(object):

    def leetcode_problems_api_favorites(self,referer):
        url="https://leetcode.cn/problems/api/favorites/"
        headers={
            "referer": referer
        }
        # params={
        #     "device_id":device_id,
        #     "appid":appid,
        #     "carrier_region":carrier_region
        # }
        return  send_request(url,headers)
