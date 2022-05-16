from abc import ABC, abstractmethod
from typing import Any
from pydantic import BaseModel


class RandomStore(BaseModel):
    is_store_open: bool
    maintenance: bool
    error_code: str


class AbstractHandler(ABC):

    _next_handler = None

    def set_successor(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, store_status: Any) -> str or None:
        if self._next_handler:
            return self._next_handler.handle(store_status)
        return None


class IsStoreOpenHandler(AbstractHandler):
    def handle(self, store_status: RandomStore) -> str:
        if store_status.is_store_open:
            return super().handle(store_status)
        raise Exception("Store is closed!")


class MaintenanceHandler(AbstractHandler):
    def handle(self, store_status: RandomStore) -> str:
        if not store_status.maintenance:
            return super().handle(store_status)
        raise Exception("Store is currently maintained")


class ErrorCodeHandler(AbstractHandler):
    def handle(self, store_status: RandomStore) -> str:
        if store_status.error_code == "unknown":
            return super().handle(store_status)
        raise Exception("An unknown error has occurred!")


if __name__ == "__main__":
    visitor = IsStoreOpenHandler()
    maintenance = MaintenanceHandler()
    error_code = ErrorCodeHandler()

    store_status = RandomStore(
        is_store_open=True,
        maintenance=False,
        error_code="unknown"
    )

    # Setting up chain of responsibilities
    visitor.set_successor(maintenance).set_successor(error_code)

    # Setting up different chain of responsibilities, doesn't brake the code.
    maintenance.set_successor(visitor).set_successor(error_code)
    print(visitor.handle(store_status))
    print(maintenance.handle(store_status))
