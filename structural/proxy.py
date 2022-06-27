from abc import ABC, abstractmethod


class ApiConnector(ABC):

    @abstractmethod
    def send_request(self, payload: dict) -> dict:
        pass


class Microservice(ApiConnector):

    def send_request(self, payload: dict) -> dict:
        return payload


class Proxy(ApiConnector):

    def __init__(self, user_login: str | None, service: Microservice):
        self.user_login = user_login
        self._service = service

    def send_request(self, payload: dict) -> dict:
        if self.validate_user():
            return payload

    def validate_user(self):
        if self.user_login:
            return True


if __name__ == "__main__":
    microservice = Microservice()
    body = {"body": "content"}

    proxy = Proxy("Admin", microservice)
    proxy.send_request(body)
