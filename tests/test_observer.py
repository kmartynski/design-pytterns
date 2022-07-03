from unittest.mock import patch, MagicMock

from behavioral.observer import FirstObserver, SecondObserver, Statuses, Worker


class TestObserver:

    @patch("behavioral.observer.Worker", side_effect=Statuses.CLOSED)
    def test_first_observer_returns_proper_status(self, mock_random: MagicMock):
        mock_random._state = Statuses.CLOSED
        worker = Worker(Statuses)
        observer = FirstObserver()
        worker.add_observer(observer)

        worker.run()
        assert observer._worker_info == "Worker is down"

    @patch("behavioral.observer.Worker", side_effect=Statuses.OPEN)
    def test_second_observer_returns_proper_status(self, mock_random: MagicMock):
        mock_random._state = Statuses.OPEN
        worker = Worker(Statuses)
        observer = SecondObserver()
        worker.add_observer(observer)

        worker.run()
        assert observer._worker_info == "Worker is up"

    def test_worker_has_observer(self):
        worker = Worker(Statuses)
        observer = FirstObserver()
        worker.add_observer(observer)

        assert worker._observers

        worker.remove_observer(observer)

        assert not worker._observers
