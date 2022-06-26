from abc import ABC, abstractmethod


class RadioInterface(ABC):

    @abstractmethod
    def broadcast(self, message: str, bandwidth: int) -> str:
        pass


class RadioOne(RadioInterface):

    def broadcast(self, message: str, bandwidth: int) -> str:
        return f"Message from {self.__class__.__name__}: {message} on {bandwidth} MHz"


class RadioTwo(RadioInterface):

    def broadcast(self, message: str, bandwidth: int) -> str:
        return f"Transmission from {self.__class__.__name__}: {message} on {bandwidth} MHz"


class Emitter:

    def __init__(self, radio: RadioInterface, message: str, bandwidth: int):
        self.radio = radio
        self.message = message
        self.bandwidth = bandwidth

    def operation(self):
        return self.radio.broadcast(self.message, self.bandwidth)


if __name__ == "__main__":
    radio_1 = RadioOne()
    radio_2 = RadioTwo()

    emitter_1 = Emitter(radio_1, "Message sent!", 52)
    emitter_2 = Emitter(radio_2, "Transmission sent!", 32)

    print(emitter_1.operation())
    print(emitter_2.operation())
