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

    def __init__(self, name) -> None:
        self.name = name
        self._children: List[CompositeInterface] = []

    def add_element(self, component) -> None:
        self._children.append(component)
        component.parent = self

    def remove_element(self, component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def get_subcomposites(self):
        print(self.name)
        for child in self._children:
            print("\t", end="")
            print(child.name)
            child.get_subcomposites()


if __name__ == "__main__":

    # ...as well as the complex composites.
    root = Composite("root")

    square = Composite("square")
    triangle = Composite("triangle")
    circle = Composite("circle")
    star = Composite("star")

    triangle.add_element(circle)
    square.add_element(star)
    square.add_element(triangle)

    root.add_element(square)

    square.remove_element(triangle)
    root.get_subcomposites()

    print("*******")
    triangle.get_subcomposites()