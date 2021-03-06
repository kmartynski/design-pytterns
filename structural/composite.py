from abc import abstractmethod, ABC
from typing import List


class CompositeInterface(ABC):

    def __set_parent__(self, parent):
        self.parent = parent

    def __get__(self, obj, type=None):
        return obj.__dict__.get(self.parent)

    def __set__(self, obj, value):
        obj.__dict__[self.parent] = value

    def add_element(self, component):
        pass

    def remove_element_element(self):
        pass

    def is_composite(self):
        pass

    @abstractmethod
    def get_subcomposites(self):
        pass


class Composite(CompositeInterface):

    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[CompositeInterface] = []

    def add_element(self, component: CompositeInterface) -> None:
        self._children.append(component)
        component.parent = self

    def remove_element(self, component: CompositeInterface) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def get_subcomposites(self):
        return self._children

    def __str__(self):
        return f"{self.__class__.__name__} of {self.name}"


if __name__ == "__main__":

    root = Composite("root")

    square = Composite("square")
    triangle = Composite("triangle")
    circle = Composite("circle")
    star = Composite("star")

    triangle.add_element(circle)

    square.add_element(star)
    square.add_element(triangle)

    root.add_element(square)

    # square.remove_element(triangle)
    root.get_subcomposites()

    triangle.get_subcomposites()
