from typing import Any, List

from pytest import fixture

from behavioral.iterator import BasicIterator, DataCollection


@fixture
def collection():
    collection = DataCollection()
    collection.add_item("WAV format")
    collection.add_item("MPEG format")
    collection.add_item("MP3 format")
    return collection


class TestIterator:

    def test_iterator_return_three_elements(self, collection: List[Any]):
        test_list = ['WAV format', 'MPEG format', 'MP3 format']
        assert [data for data in collection] == test_list

    def test_iterator_is_basic_iterator_type(self, collection: List[Any]):
        assert type(iter(collection)) == BasicIterator
