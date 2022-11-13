from client.http.tiktok_ug_incentive_client_api import TikTokUgIncentiveClientApi

class Client(object):
    @property
    def tiktok_ug_incentive_client_api(self):
        return TikTokUgIncentiveClientApi()
