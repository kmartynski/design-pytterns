from abc import ABC, abstractmethod

from datetime import datetime


class State(ABC):

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context) -> None:
        self._context = context

    @abstractmethod
    def handle_1(self) -> None:
        pass


class Context:

    _state = None

    def __init__(self, state: State):
        self.switch_to(state)

    def switch_to(self, state: State):
        self._state = state
        self._state.context = self

    def request_1(self):
        self._state.handle_1()


class InitialState(State):

    _list_of_changes = []

    def handle_1(self):
        self._list_of_changes.append(f"Initialised at: {datetime.now()}")
        self.context.switch_to(FinalState())


class FinalState(State):

    _list_of_changes = []

    def handle_1(self):
        self._list_of_changes.append(f"Finished at: {datetime.now()}")
        return


if __name__ == "__main__":

    context = Context(FinalState())
    context.request_1()

