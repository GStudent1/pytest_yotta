import client


class TestEoyMainPage(object):
    def test_eoy_main_page(self,client):
        respon =client.tiktok_ug_incentive_client_api.tiktok_incentive_v1_eoy_main_page(
            device_id="1",
            sessionid="1",
            appid="1180",
            carrier_region="PH"
        )