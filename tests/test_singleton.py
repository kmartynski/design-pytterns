from creational.singleton import Config


class TestSingleton:

    def test_should_return_same_id_for_instances(self):
        first_cfg = Config()
        second_cfg = Config()
        assert id(first_cfg) == id(second_cfg)
