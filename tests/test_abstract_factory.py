from typing import List

from pytest import fixture

from creational.abstract_factory import Car


@fixture
def list_of_cars():
    cars = (
        ("BMW", "black"),
        ("Toyata", "red"),
        ("KIA", "green"),
        ("Tesla", "black"),
    )
    return cars


class TestAbstractFactory:

    def test_should_return_four_objects(self, list_of_cars: tuple):
        list_of_car_objects: List[Car] = []
        for car in list_of_cars:
            list_of_car_objects.append(Car(car[0], car[1]))

        assert len(list_of_car_objects) == 4

    def test_should_return_objects(self, list_of_cars: tuple):
        list_of_car_objects: List[Car] = []
        for car in list_of_cars:
            list_of_car_objects.append(Car(car[0], car[1]))

        assert all(car for car in list_of_car_objects)
