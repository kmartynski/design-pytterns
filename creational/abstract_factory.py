from abc import ABC, abstractmethod
from typing import List


class CarAbstractFactory(ABC):

    @abstractmethod
    def create_car(self) -> str:
        pass


class Car(CarAbstractFactory):

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def create_car(self) -> dict:
        return {
            "name": self.name,
            "color": self.color
        }

    def __str__(self):
        return f"{self.name} in {self.color} color."


if __name__ == "__main__":
    list_of_car_objects: List[Car] = []
    cars = (
        ("BMW", "black"),
        ("Toyata", "red"),
        ("KIA", "green"),
        ("Tesla", "black"),
    )

    for car in cars:
        list_of_car_objects.append(Car(car[0], car[1]))