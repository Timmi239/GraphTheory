from trees_2_1.connected_component_count import count_single_vertexes, find_connected_vertex
from unittest import TestCase


class Tests(TestCase):
    def test_absent_single_vertexes(self):
        edges_list = [['1', '2'], ['1', '3']]
        vertex_count = 3

        assert count_single_vertexes(edges_list, vertex_count) == 0

    def test_count_single_vertexes(self):
        edges_list = [['1', '3'], ['2', '1']]
        vertex_count = 4

        assert count_single_vertexes(edges_list, vertex_count) == 1

    def test_find_connected_vertex(self):
        edges_list = [['1', '2'], ['1', '3']]
        current_vertex = '2'

        assert find_connected_vertex(edges_list, current_vertex) == '1'

    def test_find_connected_vertex_if_there_is_not(self):
        edges_list = [['1', '2'], ['1', '3']]
        current_vertex = '4'

        assert not find_connected_vertex(edges_list, current_vertex)
