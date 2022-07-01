import copy

from creational.prototype import Component, EventObject


class TestPrototype:

    def test_should_return_copy(self):
        list_of_events = ["payment", "checkout"]

        ref_component = Component()

        event = EventObject("finished", list_of_events)
        ref_component.set_parent(event)

        shallow_copy = copy.copy(event)

        assert shallow_copy.__str__() == "finished event with copied events: ['payment', 'checkout']"

    def test_should_return_deep_cpy(self):
        list_of_events = ["payment", "checkout"]

        ref_component = Component()

        event = EventObject("finished", list_of_events)
        ref_component.set_parent(event)

        deepcopy = copy.deepcopy(event)

        assert deepcopy.__str__() == "finished event with copied events: ['payment', 'checkout']"
