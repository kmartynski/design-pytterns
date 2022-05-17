from pytest import fixture, mark

from structural.flyweight import FlyweightFactory


@fixture
def products():
    product_data = (
        ('Banana', 'Fruit'), ('Snickers', 'Sweet'), ('Chips', 'Sweet'), ('Apple', 'Fruit'), ("Tomato", "Veggie")
    )
    return product_data


@fixture
def populated_flyweight_factory(products):
    list_of_products = []
    for i in products:
        item = FlyweightFactory(i[0], i[1])
        item.set_product_data(i[1])
        list_of_products.append(item)
    return list_of_products


class TestFlyweight:

    def test_should_return_unique_product_data_id(self, populated_flyweight_factory):
        assert populated_flyweight_factory != set(populated_flyweight_factory)

    @mark.parametrize(
        "product_name, number_of_occurrences",
        [
            ('Flyweight pattern[Fruit]', 2),
            ('Flyweight pattern[Veggie]', 1),
            ('Flyweight pattern[Sweet]', 2),
        ]
    )
    def test_should_return_number_of_products_with_same_id(
            self,
            product_name,
            number_of_occurrences,
            populated_flyweight_factory
    ):
        list_of_ids = []
        for product_id in populated_flyweight_factory:
            list_of_ids.append(product_id.get_product_data())

        assert list_of_ids.count(product_name) == number_of_occurrences
