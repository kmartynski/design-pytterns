from abc import ABC, abstractmethod


class AbstractProcessor(ABC):

    def template_method(self, credit_card_mock):
        self.validate_number(credit_card_mock)
        self.check_issue_date(credit_card_mock)
        self.verify_owner(credit_card_mock)
        self.check_cvc_code(credit_card_mock)
        self.check_application_origin(credit_card_mock)
        self.make_payment(credit_card_mock)

    def validate_number(self, credit_card_mock):
        return f"Validating number for {credit_card_mock}"

    def check_issue_date(self, credit_card_mock):
        return f"Checking issue date for {credit_card_mock}"

    def verify_owner(self, credit_card_mock):
        return f"Checking owner name for {credit_card_mock}"

    def check_cvc_code(self, credit_card_mock):
        return f"Validating CVC number for {credit_card_mock}"

    def check_application_origin(self, credit_card_mock):
        pass

    @abstractmethod
    def make_payment(self, credit_card_mock):
        pass


class VirtualCreditCardProcessor(AbstractProcessor):

    def check_application_origin(self, credit_card_mock):
        return f"Checking application issuer for virtual card no. {credit_card_mock}"

    def make_payment(self, credit_card_mock):
        return f"Processing payment for {credit_card_mock}"


class CreditCardProcessor(AbstractProcessor):

    def make_payment(self, credit_card_mock):
        return f"Processing payment for {credit_card_mock}"


if __name__ == "__main__":
    credit_card = "Master Card"
    virtual_credit_card = "Virtual Visa Card"
    card1 = CreditCardProcessor().template_method(credit_card)
    card2 = VirtualCreditCardProcessor().template_method(virtual_credit_card)
