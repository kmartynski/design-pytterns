from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class UserAntiFraud(Component):

    def __init__(self, user: dict):
        self.user = user

    def accept(self, visitor: Visitor):
        visitor.visit_antifraud(self)

    def check_if_fraud_account(self) -> bool:
        return True if self.user["fraud"] else False


class UserPaymentGateway(Component):

    def __init__(self, user: dict):
        self.user = user

    def accept(self, visitor: Visitor):
        visitor.visit_payment(self)

    def check_if_payment_accepted(self) -> bool:
        return True if self.user["payment"] else False


class Visitor(ABC):

    @abstractmethod
    def visit_antifraud(self, element: UserAntiFraud) -> None:
        pass

    @abstractmethod
    def visit_payment(self, element: UserPaymentGateway) -> None:
        pass


class ConcreteVisitor1(Visitor):
    def visit_antifraud(self, element) -> str:
        return f"User is {'' if element.check_if_fraud_account() else 'NOT '}in Antifraud system"

    def visit_payment(self, element) -> str:
        return f"User has {'' if element.check_if_payment_accepted() else 'NOT '}paid for order"


class ConcreteVisitor2(Visitor):
    def visit_antifraud(self, element) -> str:
        return f"User is {'' if element.check_if_fraud_account() else 'NOT '}in Antifraud system"

    def visit_payment(self, element) -> str:
        return f"User has {'' if element.check_if_payment_accepted() else 'NOT '}paid for order"


if __name__ == "__main__":
    user_1 = {
        "name": "Tom",
        "fraud": True,
        "payment": False
    }
    user_2 = {
        "name": "Vlad",
        "fraud": False,
        "payment": False,
    }
    components = [UserAntiFraud(user_1), UserPaymentGateway(user_2)]

    visitor1 = ConcreteVisitor1()
    UserAntiFraud(user_1).accept(visitor1)

    visitor2 = ConcreteVisitor2()
    UserPaymentGateway(user_2).accept(visitor2)
