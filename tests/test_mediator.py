from pytest import fixture, mark, raises

from behavioral.mediator import (
    Mediator,
    ServerComponent1,
    ServerComponent2
)


@fixture
def server_component_1():
    return ServerComponent1()


@fixture
def server_component_2():
    return ServerComponent2()


class TestMediator:

    def test_should_return_none_for_component_case_1(self, server_component_1, server_component_2):
        _ = Mediator(server_component_1, server_component_2)

        assert server_component_2.send_user_data() is None

    def test_should_return_none_for_component_case_2(self, server_component_1, server_component_2):
        _ = Mediator(server_component_1, server_component_2)

        assert server_component_1.retrieve_card_data() is None

    @mark.parametrize(
        "component",
        [
            server_component_1,
            server_component_2
        ]
    )
    def test_mediator_fail_if_not_instantiated_for_retrieved_user_data(self, component):
        with raises(AttributeError):
            component.retrieve_user_data()

    @mark.parametrize(
        "component",
        [
            server_component_1,
            server_component_2
        ]
    )
    def test_mediator_fail_if_not_instantiated_for_retrieved_card_data(self, component):
        with raises(AttributeError):
            component.retrieve_card_data()

    @mark.parametrize(
        "component",
        [
            server_component_1,
            server_component_2
        ]
    )
    def test_mediator_fail_if_not_instantiated_for_send_card_data(self, component):
        with raises(AttributeError):
            component.send_card_data()

    @mark.parametrize(
        "component",
        [
            server_component_1,
            server_component_2
        ]
    )
    def test_mediator_fail_if_not_instantiated_for_send_user_data(self, component):
        with raises(AttributeError):
            component.send_user_data()
