class ConfigMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Config(metaclass=ConfigMeta):

    def get_config(self):
        return {
            "api-key": "key",
            "base_url": "url",
        }


if __name__ == "__main__":

    first_cfg = Config()
    second_cfg = Config()
