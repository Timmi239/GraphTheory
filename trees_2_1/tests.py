from trees_2_1.connected_component_count import count_connected_component
from unittest import TestCase


class Tests(TestCase):
    def test_example_1(self):
        edges_list = [['1', '2'], ['3', '2']]
        vertex_count = 4

        assert count_connected_component(edges_list, vertex_count) == 2

    def test_example_2(self):
        edges_list = [['1', '2'], ['3', '2'], ['4', '3']]
        vertex_count = 4

        assert count_connected_component(edges_list, vertex_count) == 1

    def test_central_vertex(self):
        edges_list = [['1', '2'], ['1', '3'], ['1', '4']]
        vertex_count = 5

        assert count_connected_component(edges_list, vertex_count) == 2

    def test_loop_edge(self):
        edges_list = [['1', '1'], ['1', '2']]
        vertex_count = 3

        assert count_connected_component(edges_list, vertex_count) == 2

    def test_no_edges(self):
        edges_list = []
        vertex_count = 0

        assert count_connected_component(edges_list, vertex_count) == 0

    def test_multi_edges(self):
        edges_list = [['1', '2'], ['2', '1']]
        vertex_count = 3

        assert count_connected_component(edges_list, vertex_count) == 2

    def test_starts_not_with_one(self):
        edges_list = [['2', '3']]
        vertex_count = 4

        assert count_connected_component(edges_list, vertex_count) == 3

    def test_vertex_with_two_digits(self):
        edges_list = [['1', '2'], ['11', '12'], ['1', '12']]
        vertex_count = 12

        assert count_connected_component(edges_list, vertex_count) == 9
