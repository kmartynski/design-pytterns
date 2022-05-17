from structural.composite import Composite


root = Composite("root")
square = Composite("square")
triangle = Composite("triangle")
circle = Composite("circle")
star = Composite("star")


class TestComposite:

    def test_should_add_children_to_parent_element(self):
        root.add_element(square)
        assert len(root.get_subcomposites())

    def test_should_remove_children_from_parent_element(self):
        star.add_element(square)
        star.remove_element(square)
        assert not star.get_subcomposites()

    def test_should_get_each_parent_children_number(self):
        triangle.add_element(circle)

        square.add_element(star)
        square.add_element(triangle)

        root.add_element(square)
        assert len(root.get_subcomposites()) == 1
        assert len(triangle.get_subcomposites()) == 1
        assert len(square.get_subcomposites()) == 2
