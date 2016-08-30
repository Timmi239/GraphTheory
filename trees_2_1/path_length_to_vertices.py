# На вход программе подаётся описание простого связного графа.
# Первая строка содержит два числа: число вершин V <= 10000 и число рёбер E <= 30000 графа.
# Следующие E строк содержат номера пар вершин, соединенных рёбрами.
# Вершины имеют номера от 0 до V-1.
# Выведите список из V чисел — расстояний от вершины 0 до соответствующих вершин графа.

from common.helpers import get_input_graph_in_list, fill_vertices_dict_with_default_value


def count_path_lengths(edges_list, vertex_count):
    start_vertex = '0'
    vertices_with_path_len = fill_vertices_dict_with_default_value(vertex_count, default=-1)
    dfs(start_vertex, edges_list, vertices_with_path_len)
    return [vertices_with_path_len[str(i)] for i in range(vertex_count)]


def dfs(current_vertex, edges_list, vertices_with_path_len, path_length=0):
    vertices_with_path_len[current_vertex] = path_length
    for edge in edges_list:
        if current_vertex in edge:
            connected_vertex = edge[1] if current_vertex == edge[0] else edge[0]
            if vertices_with_path_len[connected_vertex] > path_length + 1 or \
                    vertices_with_path_len[connected_vertex] == -1:
                dfs(connected_vertex, edges_list, vertices_with_path_len, path_length + 1)


if __name__ == '__main__':
    paths = count_path_lengths(*get_input_graph_in_list())
    print(' '.join(paths))
