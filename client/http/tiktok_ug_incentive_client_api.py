from client.http import send_request

class TikTokUgIncentiveClientApi(object):

    def tiktok_incentive_v1_eoy_main_page(self,device_id,appid,carrier_region,sessionid):
        url="/tiktok/incentive/v1/eoy/main_page"
        headers={
            "sessionid" : sessionid
        }
        params={
            "device_id":device_id,
            "appid":appid,
            "carrier_region":carrier_region
        }
        return  send_request(url,headers,params)
