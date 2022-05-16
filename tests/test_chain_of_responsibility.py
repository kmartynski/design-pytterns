from pytest import mark, fixture

from behavioral.chain_of_responsibility import (
    RandomStore,
    IsStoreOpenHandler,
    MaintenanceHandler,
    ErrorCodeHandler
)

visitor = IsStoreOpenHandler()
maintenance = MaintenanceHandler()
error_code = ErrorCodeHandler()


@fixture
def random_store():
    store_status = RandomStore(
        is_store_open=True,
        maintenance=False,
        error_code="unknown"
    )
    return store_status

@fixture
def random_chain():
    visitor.set_successor(maintenance).set_successor(error_code)

@fixture
def random_chain_2():
    maintenance.set_successor(visitor).set_successor(error_code)
