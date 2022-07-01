import copy
from typing import List


class EventObject:

    def __init__(self, name: str, previous_event: List[str]):
        self.name = name
        self.previous_event = previous_event

    def __copy__(self):
        name = copy.copy(self.name)
        previous_event = copy.copy(self.previous_event)

        new_event = self.__class__(
            name, previous_event
        )

        new_event.__dict__.update(self.__dict__)
        return new_event

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}

        name = copy.deepcopy(self.name, memo)
        previous_event = copy.deepcopy(self.previous_event, memo)

        new_event = self.__class__(
            name, previous_event
        )

        new_event.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new_event

    def __str__(self):
        return f"{self.name} event with copied events: {[event for event in self.previous_event]}"


class Component:

    def __init__(self):
        self.parent = None

    def set_parent(self, parent: EventObject):
        self.parent = parent


if __name__ == "__main__":
    list_of_events = ["payment", "checkout"]

    ref_component = Component()

    event = EventObject("finished", list_of_events)
    ref_component.set_parent(event)

    shallow_copy = copy.copy(event)