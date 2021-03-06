# Найти количество компонент связности неориентированного графа
# при помощи поиска в глубину.
#
# На вход подаётся описание графа.
# В первой строке указаны два натуральных числа, разделенные пробелом:
# число вершин v≤1000 и число рёбер e≤1000.
# В следующих ee строках содержатся описания рёбер.
# Каждое ребро задаётся разделённой пробелом парой номеров вершин, которые это ребро соединяет.
# Считается, что вершины графа пронумерованы числами от 1 до v.
#
# Формат выходных данных:
# Количество компонент связности графа.

from common.helpers import get_input_graph_in_list, fill_vertices_dict_with_default_value


def count_connected_component(edges_list, vertex_count):
    components = 0
    vertices_with_status = fill_vertices_dict_with_default_value(vertex_count, default=False, start_index=1)
    while True:
        start_vertex = _search_not_visited_vertex(vertices_with_status)
        if not start_vertex:
            return components
        components += 1
        dfs(start_vertex, edges_list, vertices_with_status)


def _search_not_visited_vertex(vertices_with_status):
    for vertex_with_status in vertices_with_status.items():
        if not vertex_with_status[1]:
            return vertex_with_status[0]
    return None


def dfs(current_vertex, edges_list, vertices_with_status):
    vertices_with_status[current_vertex] = True
    for edge in edges_list:
        if current_vertex in edge:
            connected_vertex = edge[1] if current_vertex == edge[0] else edge[0]
            if not vertices_with_status[connected_vertex]:
                dfs(connected_vertex, edges_list, vertices_with_status)


if __name__ == '__main__':
    print(count_connected_component(*get_input_graph_in_list()))
