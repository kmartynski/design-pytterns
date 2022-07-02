from collections.abc import Iterable, Iterator
from typing import Any, List


class DataCollection(Iterable):

    def __init__(self, collection: List[Any] = []):
        if collection is not None:
            collection = []
        self._collection = [] if collection is not None else collection

    def __iter__(self):
        return BasicIterator(self._collection)

    def add_item(self, item: Any):
        self._collection.append(item)


class BasicIterator(Iterator):
    _position: int | None = None

    def __init__(self, collection: List[Any], reverse: bool = False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        else:
            return value


if __name__ == "__main__":
    collection = DataCollection()
    collection.add_item("WAV format")
    collection.add_item("MPEG format")
    collection.add_item("MP3 format")
