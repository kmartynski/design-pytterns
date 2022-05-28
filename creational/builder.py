from abc import ABC, abstractmethod
from typing import Any


class BuilderInterface(ABC):

    @property
    @abstractmethod
    def website(self):
        pass

    @abstractmethod
    def add_navbar(self):
        pass

    @abstractmethod
    def add_main_section(self):
        pass

    @abstractmethod
    def add_contact_form(self):
        pass


class Website:
    def __init__(self) -> None:
        self.elements = []

    def add(self, part: Any) -> None:
        self.elements.append(part)

    def list_elements(self) -> list:
        return self.elements


class WebBuilder(BuilderInterface):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._website = Website()

    @property
    def website(self) -> Website:
        website = self._website
        self.reset()
        return website

    def add_navbar(self) -> None:
        self._website.add("Navbar")

    def add_main_section(self) -> None:
        self._website.add("Main section")

    def add_contact_form(self) -> None:
        self._website.add("Contact")


class WebCreator:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> BuilderInterface:
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderInterface) -> None:
        self._builder = builder

    def build_business_card(self) -> None:
        self.builder.add_main_section()
        self.builder.add_contact_form()

    def build_full_featured_website(self) -> None:
        self.builder.add_navbar()
        self.builder.add_main_section()
        self.builder.add_contact_form()


if __name__ == "__main__":
    creator = WebCreator()
    builder = WebBuilder()
    creator.builder = builder

    print("Standard basic product: ")
    creator.build_business_card()
    builder.website.list_elements()

    print("\n")

    print("Standard full featured product: ")
    creator.build_full_featured_website()
    builder.website.list_elements()

    print("\n")

    print("Custom product: ")
    builder.add_navbar()
    builder.add_contact_form()
    builder.website.list_elements()
