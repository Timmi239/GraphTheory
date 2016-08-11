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

from common.helpers import get_input_graph_in_list


def count_connected_component(edges_list, vertex_count):
    single_vertexes_count = count_single_vertexes(edges_list, vertex_count)
    components = single_vertexes_count
    while edges_list:
        current_vertex = edges_list[0][0]
        current_component = [current_vertex, ]
        index = 0
        while True:
            while find_connected_vertex(edges_list, current_component[index]):
                connected_vertex = find_connected_vertex(edges_list, current_component[index])
                del_edge_with_vertex(edges_list, current_component[index], connected_vertex)
                if connected_vertex not in current_component:
                    current_component.append(connected_vertex)
            if len(current_component) > index + 1:
                index += 1
            else:
                break
        components += 1
    return components


def count_single_vertexes(edges_list, vertex_count):
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


def del_edge_with_vertex(edges_list, current_vertex, connected_vertex):
    for e in edges_list:
        if current_vertex in e and connected_vertex in e:
            edges_list.remove(e)


if __name__ == '__main__':
    print(count_connected_component(*get_input_graph_in_list()))
