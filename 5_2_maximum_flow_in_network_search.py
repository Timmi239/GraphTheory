# Найдите максимальный поток в сети.
#
# Первая строка содержит два числа 2≤v≤50 и 0≤e≤1000 — число вершин и число рёбер сети.
# Следующие ee строк описывают рёбра: каждая из них содержит три целых числа через пробел:
# 0≤ui<v, 0≤vi<v, 0<ci<50 — исходящую и входящую вершины для этого ребра, а так же его пропускную способность.
from common.edge import Edge
from common.mark import Mark
from common.vertex import Vertex


def main():
    vertex_list = get_vertex_list_from_input()
    while True:
        vertex_list[0].mark = Mark(None, '-', float('Inf'))
        vertex_list = mark_vertexes(vertex_list, current_vertex=vertex_list[0])
        if vertex_list[-1].mark.sign is not None:
            vertex_list = change_flow(vertex_list, current_vertex=vertex_list[-1])
        else:
            break
        delete_marks(vertex_list)
    print(sum([e.f for e in vertex_list[-1].edges_list if e.v_to == vertex_list[-1].name]))


def get_vertex_list_from_input():
    v, e = _parse_vertexes_and_edges_counts()
    vertex_list = [Vertex(str(i)) for i in range(v)]
    for i in range(e):
        u1, u2, c = input().split()
        vertex_list[int(u1)].add_edge(Edge(int(c), u1, u2))
        vertex_list[int(u2)].add_edge(Edge(int(c), u1, u2))
    return vertex_list


def _parse_vertexes_and_edges_counts():
    v_str, e_str = input().split()
    v, e = map(int, [v_str, e_str])
    return v, e


def mark_vertexes(vertex_list, current_vertex):
    if current_vertex.name == str(len(vertex_list)):
        return vertex_list
    for edge in current_vertex.edges_list:
        if vertex_list[-1].mark.sign is not None:
            break
        if edge.v_from == current_vertex.name and edge.f < edge.c:
            vertex = list(filter(lambda v: v.name == edge.v_to, vertex_list))[0]
            if vertex.mark.sign is None:
                vertex.mark = Mark(current_vertex.name, '+', min(current_vertex.mark.value, edge.c - edge.f))
                vertex_list = mark_vertexes(vertex_list, current_vertex=vertex)
        elif edge.v_to == current_vertex.name and edge.f > 0:
            vertex = list(filter(lambda v: v.name == edge.v_from, vertex_list))[0]
            if vertex.mark.sign is None:
                vertex.mark = Mark(current_vertex.name, '-', min(current_vertex.mark.value, edge.f))
                vertex_list = mark_vertexes(vertex_list, current_vertex=vertex)
    return vertex_list


def change_flow(vertex_list, current_vertex):
    if current_vertex.name == '0':
        return vertex_list
    diff = vertex_list[-1].mark.value
    prev_vertex = list(filter(lambda v: v.name == current_vertex.mark.prev_vertex_name, vertex_list))[0]
    if current_vertex.mark.sign == '+':
        current_edge_1 = list(filter(
                lambda e: current_vertex.name == e.v_to and current_vertex.mark.prev_vertex_name == e.v_from,
                current_vertex.edges_list
        ))[0]
        current_edge_2 = list(filter(
                lambda e: current_vertex.name == e.v_to and current_vertex.mark.prev_vertex_name == e.v_from,
                prev_vertex.edges_list
        ))[0]
        current_edge_1.f += diff
        current_edge_2.f += diff
    elif current_vertex.mark.sign == '-':
        current_edge_1 = list(filter(
                lambda e: current_vertex.name == e.v_from and current_vertex.mark.prev_vertex_name == e.v_to,
                current_vertex.edges_list
        ))[0]
        current_edge_2 = list(filter(
                lambda e: current_vertex.name == e.v_from and current_vertex.mark.prev_vertex_name == e.v_to,
                prev_vertex.edges_list
        ))[0]
        current_edge_1.f -= diff
        current_edge_2.f -= diff
    next_vertex = list(filter(lambda v: v.name == current_vertex.mark.prev_vertex_name, vertex_list))[0]
    change_flow(vertex_list, current_vertex=next_vertex)
    return vertex_list


def delete_marks(vertex_list):
    for v in vertex_list:
        v.mark = Mark(None, None, 0)


if __name__ == '__main__':
    main()


# for future tests
'''
8 11
0 1 3
0 2 3
1 3 3
2 3 3
2 4 1
3 5 1
3 6 4
4 5 1
4 6 1
5 7 1
6 7 4
'''

'''
4 5
0 1 1000
0 2 1000
1 3 1000
1 2 1
2 3 1000
'''