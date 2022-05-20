class Product:

    def products(self, product_name):
        return "Flyweight pattern[% s]" % product_name


class FlyweightFactory:
    flyweight_products = {}

    def __new__(cls, name: str, product_type: str):
        try:
            product_id = cls.flyweight_products[product_type]
        except KeyError:
            product_id = object.__new__(cls)
            cls.flyweight_products[product_type] = product_id
        return product_id

    def set_product_data(self, product_info: str):
        product_instance = Product()
        self.product_data = product_instance.products(product_info)

    def get_product_data(self):
        return self.product_data


if __name__ == '__main__':
    product_data = (
        ('Banana', 'Fruit'), ('Snickers', 'Sweet'), ('Chips', 'Sweet'), ('Apple', 'Fruit'), ("Tomato", "Veggie")
    )
    list_of_products = []

    for i in product_data:
        item = FlyweightFactory(i[0], i[1])
        item.set_product_data(i[1])
        list_of_products.append(item)

    print(list_of_products)
    print(set(list_of_products))
