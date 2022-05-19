from pytest import fixture, mark

from behavioral.template_method import CreditCardProcessor, VirtualCreditCardProcessor

@fixture
def master_card_mock():
    credit_card = "Master Card"
    return credit_card


@fixture
def virtual_card_mock():
    virtual_credit_card = "Virtual Visa Card"
    return virtual_credit_card

@fixture
def master_card_fixture():
    return CreditCardProcessor().template_method(master_card_mock)


@fixture
def virtual_visa_card_fixture():
    return VirtualCreditCardProcessor().template_method(virtual_card_mock)


class TestTemplateMethod:

    @mark.parametrize(
        "credit_card",
        [
            master_card_fixture,
            virtual_visa_card_fixture
        ]
    )
    def test_should_return_callable_for_both_processors(self, credit_card):
        assert callable(credit_card)

    def test_should_return_true_for_virtual_card_method(self, virtual_visa_card_fixture):
        assert callable(getattr(VirtualCreditCardProcessor, "check_application_origin")) is True

    def test_should_return_for_implemented_method(self, virtual_card_mock):
        assert VirtualCreditCardProcessor().check_application_origin(virtual_card_mock) ==\
               f"Checking application issuer for virtual card no. {virtual_card_mock}"

    def test_should_return_none_for_unimplemented_method(self, master_card_mock):
        assert CreditCardProcessor().check_application_origin(master_card_mock) is None
