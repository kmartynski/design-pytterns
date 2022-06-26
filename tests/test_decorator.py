from time import sleep

from structural.decorator import decorator


class TestDecorator:

    def test_decorator_returns_time(self):
        x = decorator(lambda: sleep(2))
        assert x() > 2

