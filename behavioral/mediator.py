from abc import ABC, abstractmethod


class MediatorInterface(ABC):

    @abstractmethod
    def dispatch(self, sender: object, event: str):
        pass


class Mediator(MediatorInterface):

    def __init__(self, receiver_1, receiver_2):
        self.receiver_1 = receiver_1
        self.receiver_1.mediator = self
        self.receiver_2 = receiver_2
        self.receiver_2.mediator = self

    def dispatch(self, sender: object, trigger: str) -> None:
        if trigger == "user":
            self.receiver_1.retrieve_user_data()
        elif trigger == "card":
            self.receiver_2.send_card_data()


class ComponentInterface(ABC):

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    def __set_mediator__(self, mediator):
        self.mediator = mediator

    def __get__(self, obj, type=None):
        return obj.__dict__.get(self._mediator)

    def __set__(self, obj, value):
        obj.__dict__[self._mediator] = value


class ServerComponent1(ComponentInterface):
    def retrieve_user_data(self) -> None:
        print("Retrieving user data")
        self.mediator.dispatch(self, "save_data")

    def retrieve_card_data(self) -> None:
        print("Retrieving card data")
        self.mediator.dispatch(self, "card")


class ServerComponent2(ComponentInterface):
    def send_user_data(self) -> None:
        print("Sending user data")
        self.mediator.dispatch(self, "user")

    def send_card_data(self) -> None:
        print("Sending card data")
        self.mediator.dispatch(self, "retrieve_data")


if __name__ == "__main__":
    s1 = ServerComponent1()
    s2 = ServerComponent2()
    mediator = Mediator(s1, s2)

    s2.send_user_data()

    print("\n", end="")

    s1.retrieve_card_data()


