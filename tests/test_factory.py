from pytest import mark, fixture

from creational.factory import MessageFactory


@fixture
def example_message():
    factory = MessageFactory(message_name="welcome")
    return factory


class TestMessageFactory:

    @mark.parametrize(
        "message_input, message_response",
        [
            ("welcome", "Greetings"),
            ("farewell", "Goodbye"),
            ("plans", "What are you going to do today?")
        ]
    )
    def test_should_return_message_body(self, message_input, message_response):
        factory = MessageFactory(message_name=message_input)
        assert factory.get("body") == message_response

    def test_should_return_message_keys(self, example_message):
        assert "header", "body" in example_message

    def test_should_return_message_generator_type(self, example_message):
        assert isinstance(example_message, dict)
