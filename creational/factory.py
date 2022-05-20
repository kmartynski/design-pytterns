from datetime import datetime
import uuid


MESSAGE_MAPPER = {
    "welcome": "Greetings",
    "farewell": "Goodbye",
    "plans": "What are you going to do today?"
}


class MessageGenerator:
    def __init__(self, message_name: str):
        self.message_name = message_name

    def create_message(self) -> dict:
        type_of_message = MESSAGE_MAPPER[self.message_name]
        message = {
            "header": self._create_header(),
            "body": type_of_message
        }
        return message

    def _create_header(self) -> dict:
        header = {
            "id": uuid.uuid4(),
            "time": datetime.utcnow(),

        }
        return header


class MessageFactory:
    def __new__(cls, message_name, *args, **kwargs) -> dict:
        return MessageGenerator(message_name=message_name).create_message()


if __name__ == "__main__":
    first_message = MessageFactory("welcome")
    second_message = MessageFactory("plans")
    third_message = MessageFactory("farewell")

    print(first_message)
    print(second_message)
    print(third_message)
