# На вход программе подаётся описание простого связного графа.
# Первая строка содержит два числа: число вершин V <= 10000 и число рёбер E <= 30000 графа.
# Следующие E строк содержат номера пар вершин, соединенных рёбрами.
# Вершины имеют номера от 0 до V-1.
# Выведите список из V чисел — расстояний от вершины 0 до соответствующих вершин графа.
from unittest import TestCase

from common.helpers import get_input_graph_in_list


def main(edges_list, vertex_count):
    start_vertex = '0'
    vertices_with_path_len = dict()
    for i in range(vertex_count):
        vertices_with_path_len[str(i)] = -1
    dfs(start_vertex, edges_list, vertices_with_path_len)
    paths = []
    for i in range(vertex_count):
        paths.append(vertices_with_path_len[str(i)])
    return paths


def dfs(current_vertex, edges_list, vertices_with_path_len, path_length=0):
    vertices_with_path_len[current_vertex] = path_length
    for edge in edges_list:
        if current_vertex in edge:
            connected_vertex = edge[1] if current_vertex == edge[0] else edge[0]
            if vertices_with_path_len[connected_vertex] > path_length + 1 or vertices_with_path_len[connected_vertex] == -1:
                dfs(connected_vertex, edges_list, vertices_with_path_len, path_length + 1)


if __name__ == '__main__':
    paths = main(*get_input_graph_in_list())
    print(' '.join(paths))


class PathLengths(TestCase):
    def tests_example_1(self):
        edges_list = [['0', '1'], ['1', '2'], ['2', '0'], ['3', '2'], ['4', '3'], ['4', '2'], ['5', '4']]
        vertices_count = 6

        assert main(edges_list, vertices_count) == [0, 1, 1, 2, 2, 3]

    def tests_example_2(self):
        edges_list = [['0', '1'], ['0', '2'], ['1', '3'], ['3', '4'], ['2', '4']]
        vertices_count = 5

        assert main(edges_list, vertices_count) == [0, 1, 1, 2, 2]
