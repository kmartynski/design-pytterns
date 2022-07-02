from abc import ABC, abstractmethod


class Memento(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_content(self) -> str:
        pass


class BucketSnapshotMemento(Memento):

    def __init__(self, name: str, content: str):
        self._name = name
        self._content = content

    def get_name(self) -> str:
        return self._name

    def get_content(self) -> str:
        return self._content


class BucketSaver:

    _name = None

    def __init__(self, name: str, new_content: str):
        self._name = name
        self._new_content = new_content

    def save(self) -> Memento:
        return BucketSnapshotMemento(self._name, self._new_content)

    def restore(self, memento: Memento):
        self._name = memento.get_name()

    def set_name(self, name: str):
        self._name = name

    def set_content(self, content: str):
        self._new_content = content



class Orchestrator:

    def __init__(self, saver: BucketSaver):
        self._mementos = []
        self._saver = saver

    def backup(self):
        self._mementos.append(self._saver.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        try:
            self._saver.restore(memento)
        except Exception:
            self.undo()

    def show_history(self):
        return self._mementos


if __name__ == "__main__":
    saver = BucketSaver("AWS bucket", "file.json")
    orchestrator = Orchestrator(saver)

    orchestrator.backup()
    saver.set_name("New input")

    orchestrator.backup()
    saver.set_name("New input 2")

    orchestrator.backup()
    saver.set_name("New input 3")

    print()
    print(orchestrator.show_history())
    print([data for data in orchestrator.show_history()])

    print("\nClient: Now, let's rollback!\n")
    orchestrator.undo()

    print("\nClient: Once more!\n")
    orchestrator.undo()

    print(orchestrator.show_history())