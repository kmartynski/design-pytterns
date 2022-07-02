from behavioral.memento import BucketSaver, Orchestrator


class TestMemento:

    def test_memento_restore_bucket(self):
        saver = BucketSaver("AWS bucket", "file.json")
        orchestrator = Orchestrator(saver)

        orchestrator.backup()
        saver.set_name("New input")

        orchestrator.backup()

        assert len(orchestrator.show_history()) == 2

    def test_mement_undo_last_save(self):
        saver = BucketSaver("AWS bucket", "file.json")
        orchestrator = Orchestrator(saver)

        orchestrator.backup()
        saver.set_name("New input")

        orchestrator.backup()

        orchestrator.undo()

        assert len(orchestrator.show_history()) == 1

        orchestrator.undo()

        assert len(orchestrator.show_history()) == 0
