from pytest import mark, raises

from behavioral.chain_of_responsibility import (
    RandomStore,
    IsStoreOpenHandler,
    MaintenanceHandler,
    ErrorCodeHandler
)

is_store_open_handler = IsStoreOpenHandler()
maintenance_handler = MaintenanceHandler()
error_code_handler = ErrorCodeHandler()


class TestChainOfResponsibility:

    @mark.parametrize(
        "is_store_open, maintenance, error_code, exception",
        [
            (False, False, "error", "Store is closed!"),
            (True, True, "error", "Store is currently maintained"),
            (True, False, "error", "An unknown error has occurred!")
        ]
    )
    def test_should_return_error_for_each_handler(
            self,
            is_store_open,
            maintenance,
            error_code,
            exception,
    ):
        store_status = RandomStore(
            is_store_open=is_store_open,
            maintenance=maintenance,
            error_code=error_code
        )
        is_store_open_handler.set_successor(maintenance_handler).set_successor(error_code_handler)

        with raises(Exception):
            print(is_store_open_handler.handle(store_status))


    @mark.parametrize(
        "handler_1, handler_2, handler_3",
        [
            (IsStoreOpenHandler(), MaintenanceHandler(), ErrorCodeHandler()),
            (IsStoreOpenHandler(), ErrorCodeHandler(), MaintenanceHandler()),
            (MaintenanceHandler(), IsStoreOpenHandler(), ErrorCodeHandler()),
            (MaintenanceHandler(), ErrorCodeHandler(), IsStoreOpenHandler()),
            (ErrorCodeHandler(), MaintenanceHandler(), IsStoreOpenHandler()),
            (ErrorCodeHandler(), IsStoreOpenHandler(), MaintenanceHandler()),
        ]
    )
    def test_should_return_none_if_no_exception_with_different_handler_configuration(
            self,
            handler_1,
            handler_2,
            handler_3
    ):
        store_status = RandomStore(
            is_store_open=True,
            maintenance=False,
            error_code="unknown"
        )

        handler_1.set_successor(handler_2).set_successor(handler_3)
        assert handler_1.handle(store_status) is None
