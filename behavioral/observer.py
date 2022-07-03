from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from random import choice
from typing import List


class Statuses(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"


class WorkerInterface(ABC):

    @abstractmethod
    def add_observer(self, observer: ObserverInterface):
        pass

    @abstractmethod
    def remove_observer(self, observer: ObserverInterface):
        pass

    @abstractmethod
    def notify(self):
        pass


class ObserverInterface(ABC):

    @abstractmethod
    def update(self, worker: WorkerInterface):
        pass


class Worker(WorkerInterface):

    _state: int | None = None

    _observers: List[ObserverInterface] = []

    def __init__(self, statuses):
        self.statuses = statuses

    def add_observer(self, observer: ObserverInterface):
        self._observers.append(observer)

    def remove_observer(self, observer: ObserverInterface):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def run(self):
        self._state = choice([status for status in self.statuses])
        self.notify()


class FirstObserver(ObserverInterface):
    _worker_info = None

    def update(self, worker: WorkerInterface):
        if worker._state == Statuses.CLOSED:
            self._worker_info = "Worker is down"


class SecondObserver(ObserverInterface):
    _worker_info = None

    def update(self, worker: WorkerInterface):
        if worker._state == Statuses.OPEN:
            self._worker_info = "Worker is up"


if __name__ == "__main__":

    subject = Worker(Statuses)

    observer_a = FirstObserver()
    subject.add_observer(observer_a)

    observer_b = SecondObserver()
    subject.add_observer(observer_b)

    subject.run()
    subject.run()

    subject.remove_observer(observer_a)

    subject.run()
