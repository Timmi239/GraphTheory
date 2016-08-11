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
from typing import List, Optional

from common.helpers import get_input_graph_in_list


def count_connected_component():
    #doesn`t working =(
    edges_list, vertex_count = get_input_graph_in_list()
    single_vertexes_count = count_single_vertexes(edges_list, vertex_count)
    components = single_vertexes_count
    while edges_list:
        current_vertex = edges_list[0][0]
        current_component = [current_vertex, ]
        index = 0
        while True:
            while find_connected_vertex(edges_list, current_component[index]):
                connected_vertex = find_connected_vertex(edges_list, current_component[index])
                del_edge_with_vertex(edges_list, current_component[index])
                if connected_vertex not in current_component:
                    current_component.append(connected_vertex)
            if len(current_component) > index + 1:
                index += 1
            else:
                break
        components += 1
    print(components)


def count_single_vertexes(edges_list: List[Optional[List]], vertex_count: int) -> int:
    count = 0
    for i in range(1, vertex_count + 1):
        v = str(i)
        exists = False
        for e in edges_list:
            if v in e:
                exists = True
        if not exists:
            count += 1
    return count


def find_connected_vertex(edges_list, current_vertex):
    for e in edges_list:
        if current_vertex in e:
            return e[1] if current_vertex == e[0] else e[0]
    return None


def del_edge_with_vertex(edges_list, current_vertex):
    for e in edges_list:
        if current_vertex in e:
            edges_list.remove(e)


if __name__ == '__main__':
    count_connected_component()
