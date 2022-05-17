class UserDataReceiver:

    def retrieve(self, user_data: dict):
        return user_data


class UserDataHandler:

    def unpack_user_data(self, user_data: dict):
        name, surname = user_data.values()
        return name, surname


class UserDataStorage:

    def save_user_data(self, user_data: dict):
        return f"Saving user data to db for user namme {user_data.get('name')}"


class UserDataFacade:

    def __init__(self):
        self.receiver = UserDataReceiver()
        self.handler = UserDataHandler()
        self.storage = UserDataStorage()

    def process_user_data(self, user_data):
        self.receiver.retrieve(user_data)
        self.handler.unpack_user_data(user_data)
        self.storage.save_user_data(user_data)
        return "User data processed!"


if __name__ == "__main__":

    sample_user_data = {
        "name": "John",
        "surname": "Doe"
    }

    user = UserDataFacade()
    user.process_user_data(sample_user_data)
