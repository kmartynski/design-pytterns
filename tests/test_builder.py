from creational.builder import WebCreator, WebBuilder

creator = WebCreator()
builder = WebBuilder()


class TestBuilder:

    def test_should_return_len_of_business_template(self):
        creator.builder = builder
        creator.build_business_card()
        assert len(builder.website.list_elements()) == 2

    def test_should_return_len_of_full_featured_website(self):
        creator.builder = builder
        creator.build_full_featured_website()
        assert len(builder.website.list_elements()) == 3

    def test_should_reset_builder(self):
        assert builder.reset() is None

