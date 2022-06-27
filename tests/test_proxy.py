from structural.proxy import Microservice, Proxy


class TestProxy:
    microservice = Microservice()
    body = {"body": "content"}

    def test_proxy_returns_payload_if_user_login(self):

        proxy = Proxy("Admin", self.microservice)
        proxy.send_request(self.body)

        assert proxy.send_request(self.body) == {"body": "content"}

    def test_proxy_returns_none_if_no_user_login(self):
        proxy = Proxy(None, self.microservice)
        proxy.send_request(self.body)

        assert proxy.send_request(self.body) is None
