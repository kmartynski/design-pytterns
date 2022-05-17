from pytest import fixture, mark

from structural.facade import (
    UserDataFacade,
    UserDataHandler,
    UserDataStorage,
    UserDataReceiver
)


@fixture
def user_dict():
    sample_user_data = {
        "name": "John",
        "surname": "Doe"
    }
    return sample_user_data


class TestFacade:

    def test_should_return_message_after_processing(self, user_dict):
        user = UserDataFacade()
        assert user.process_user_data(user_dict) == "User data processed!"

    @mark.parametrize(
        "user_data_processor, processor_name",
        [
            (UserDataHandler, "handler"),
            (UserDataStorage, "storage"),
            (UserDataReceiver, "receiver")
        ]
    )
    def test_should_return_classes_of_facade_init(
            self,
            user_data_processor,
            processor_name
    ):
        user = UserDataFacade()
        assert isinstance(user.__dict__.get(processor_name), user_data_processor)
