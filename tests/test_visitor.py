from behavioral.visitor import ConcreteVisitor1, ConcreteVisitor2, UserAntiFraud, UserPaymentGateway


class TestVisitor:

    def test_user_in_fraud_system(self):
        user = {
            "name": "Tom",
            "fraud": True,
            "payment": False
        }
        visitor = ConcreteVisitor1()
        anti_fraud = UserAntiFraud(user)
        anti_fraud.accept(visitor)

        assert anti_fraud.check_if_fraud_account()


    def test_user_has_paid(self):
        user = {
            "name": "Vlad",
            "fraud": False,
            "payment": True,
        }
        visitor = ConcreteVisitor2()
        anti_fraud = UserPaymentGateway(user)
        anti_fraud.accept(visitor)

        assert anti_fraud.check_if_payment_accepted()
