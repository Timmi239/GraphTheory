from unittest import TestCase

from trees_2_1.path_length_to_vertices import count_path_lengths


class PathLengthsTests(TestCase):
    def tests_example_1(self):
        edges_list = [['0', '1'], ['1', '2'], ['2', '0'], ['3', '2'], ['4', '3'], ['4', '2'], ['5', '4']]
        vertices_count = 6

        assert count_path_lengths(edges_list, vertices_count) == [0, 1, 1, 2, 2, 3]

    def tests_example_2(self):
        edges_list = [['0', '1'], ['0', '2'], ['1', '3'], ['3', '4'], ['2', '4']]
        vertices_count = 5

        assert count_path_lengths(edges_list, vertices_count) == [0, 1, 1, 2, 2]

    def tests_example_3(self):
        edges_list = [['0', '1'], ['0', '2'], ['1', '3'], ['5', '2'], ['3', '4'], ['5', '4']]
        vertices_count = 6

        assert count_path_lengths(edges_list, vertices_count) == [0, 1, 1, 2, 3, 2]

    def test_multi_edges(self):
        edges_list = [['0', '1'], ['1', '0'], ['0', '1'], ['1', '2']]
        vertices_count = 3

        assert count_path_lengths(edges_list, vertices_count) == [0, 1, 2]

    def test_loop_edge(self):
        edges_list = [['0', '1'], ['1', '1'], ['1', '2']]
        vertices_count = 3

        assert count_path_lengths(edges_list, vertices_count) == [0, 1, 2]

    def test_vertex_with_two_digits(self):
        edges_list = [['0', '1'], ['1', '2'], ['2', '3'], ['3', '4'], ['4', '5'], ['5', '6'], ['6', '7'], ['7', '8'],
            ['8', '9'], ['9', '10'], ['9', '11'], ['10', '12']]
        vertex_count = 13

        assert count_path_lengths(edges_list, vertex_count) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11]
