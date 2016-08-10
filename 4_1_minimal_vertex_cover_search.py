# Найдите минимальное вершинное покрытие в двудольном графе.

# На вход подается описание двудольного графа, в котором доли уже выделены явно.
# Первая строка содержит три натуральных числа:
# v1<100 — число вершин первой доли, v2<100 — число вершин второй доли, e≤v1∗v2 — число рёбер.
# Подразумевается, что первая доля состоит из вершин с номерами от 0 до v1−1,
# вторая — из вершин с номерами от v1 до v1+v2−1.
# Следующие ee строк описывают рёбра: каждая из этих строк содержит два числа:
# 0≤ui<v1 и v1≤wi<v1+v2,
# что означает, что между вершинами ui и wi есть ребро.

# Скопируйте описание графа из входа на выход и выведите единственную дополнительную строку — список номеров вершин,
# составляющих минимальное вершинное покрытие. Если таких покрытий несколько, выведите любое.


class Edge(object):
    def __init__(self, c, v_from, v_to):
        self.c = c
        self.f = 0
        self.v_from = v_from
        self.v_to = v_to

    def __repr__(self):
        return '|c: {}, f: {}, v_from: {}, v_to: {}|'.format(self.c, self.f, self.v_from, self.v_to)

    def __str__(self):
        return self.__repr__()


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.mark = Mark(None, None, 0)
        self.edges_list = []

    def add_edge(self, edge):
        self.edges_list.append(edge)

    def __repr__(self):
        return '|name: {}, edges_list: {}, mark: {}|'.format(self.name, self.edges_list, str(self.mark))

    def __str__(self):
        return self.__repr__()


class Mark(object):
    def __init__(self, prev_vertex_name, sign, value):
        self.prev_vertex_name = prev_vertex_name
        self.sign = sign
        self.value = value

    def __repr__(self):
        return '|prev_vertex_name: {}, sign: {}, value: {}|'.\
            format(self.prev_vertex_name, self.sign, str(self.value))


def main():
    vertex_list, v1, v2 = get_vertex_list_from_input()
    while True:
        vertex_list[0].mark = Mark(None, '-', float('Inf'))
        vertex_list = mark_vertexes(vertex_list, current_vertex=vertex_list[0])
        if vertex_list[-1].mark.sign is not None:
            vertex_list = change_flow(vertex_list, current_vertex=vertex_list[-1])
        else:
            break
        delete_marks(vertex_list)

    count = sum([e.f for e in vertex_list[-1].edges_list if e.v_to == vertex_list[-1].name])
    search_min_tops_cover(vertex_list, count, v1, v2)


def search_min_tops_cover(vertex_list, count, v1, v2):
    tops_left_cover_names = [e.v_to for e in vertex_list[0].edges_list if e.f == 1]
    tops_right_cover_names = [e.v_from for e in vertex_list[-1].edges_list if e.f == 1]
    helper_edges = [vertex_list[int(v)].edges_list for v in tops_left_cover_names]
    tt = []
    for h in helper_edges:
        for e in h:
            if e.f == 1 and e.v_from in tops_left_cover_names:
                tt.append([e.v_from, e.v_to])
    # for comb in product(*tt):
    #     if check_tops_cover(comb, vertex_list):
    #         print_answer(comb)
    #         return
    # print('Whoops...')
    # return None
    get_tops_cover(vertex_list, v1, v2, tops_left_cover_names, tops_right_cover_names, tt)


def get_tops_cover(vertex_list, v1, v2, tops_left_cover_names, tops_right_cover_names, tt):
    l_tops_not_in_pairs = [str(i) for i in range(1, v1) if str(i) not in tops_left_cover_names]
    visited_vertexes = set(l_tops_not_in_pairs)
    for v in l_tops_not_in_pairs:
        visited_vertexes.update(dfs_l(vertex_list, set(), int(v), tt))
    l_minus = [i for i in tops_left_cover_names if i not in visited_vertexes]
    r_plus = [i for i in tops_right_cover_names if i in visited_vertexes]
    print_answer(l_minus + r_plus)


def dfs_l(vertex_list, visited_vertexes, current_vertex_index, pairs):
    for e in vertex_list[current_vertex_index].edges_list:
        if [e.v_from, e.v_to] not in pairs \
                and e.v_to not in visited_vertexes \
                and e.v_to != str(len(vertex_list) - 1) \
                and e.v_from != '0':
            visited_vertexes.add(e.v_to)
            visited_vertexes = dfs_r(vertex_list, visited_vertexes, int(e.v_to), pairs)
    return visited_vertexes


def dfs_r(vertex_list, visited_vertexes, current_vertex_index, pairs):
    for e in vertex_list[current_vertex_index].edges_list:
        if [e.v_from, e.v_to] in pairs \
                and e.v_from not in visited_vertexes \
                and e.v_to != str(len(vertex_list) - 1) \
                and e.v_from != '0':
            visited_vertexes.add(e.v_from)
            visited_vertexes = dfs_l(vertex_list, visited_vertexes, int(e.v_from), pairs)
    return visited_vertexes

def print_answer(tops):
    tops = map(lambda x: str(int(x) - 1), tops)
    print(' '.join(tops))


def check_tops_cover(tops, vertex_list):
    for v in vertex_list[1:-1]:
        for e in v.edges_list:
            if e.v_from not in tops and e.v_to not in tops and e.v_from != '0' and e.v_to != vertex_list[-1].name:
                return False
    return True


def get_vertex_list_from_input():
    v1, v2, e = _parse_vertexes_and_edges_counts()
    start_vertex = _get_start_vertex(v1)
    vertex_list = [start_vertex] + [Vertex(str(i)) for i in range(1, v1 + v2 - 1)]
    for i in range(e):
        u1, u2 = input().split()
        print(' '.join([u1, u2]))
        vertex_list[int(u1) + 1].add_edge(Edge(1, str(int(u1) + 1), str(int(u2) + 1)))
        vertex_list[int(u2) + 1].add_edge(Edge(1, str(int(u1) + 1), str(int(u2) + 1)))

    finish_vertex = _get_finish_vertex(v2, v1)
    vertex_list.append(finish_vertex)

    _add_paths_to_start_and_from_finish(vertex_list, v1, v2)

    return vertex_list, v1, v2


def _get_start_vertex(v1):
    start_vertex = Vertex('0')
    for i in range(1, v1):
        start_vertex.add_edge(Edge(1, '0', str(i)))
    return start_vertex


def _add_paths_to_start_and_from_finish(vertex_list, v1, v2):
    for i in range(1, v1):
        vertex_list[i].add_edge(Edge(1, '0', str(i)))
    for i in range(v1, v1 + v2 - 1):
        vertex_list[i].add_edge(Edge(1, str(i), str(v1 + v2 - 1)))


def _get_finish_vertex(v2, v1):
    finish_vertex = Vertex(str(v2 + v1 - 1))
    for i in range(v1, v2 + v1 - 1):
        finish_vertex.add_edge(Edge(1, str(i), str(v2 + v1 - 1)))
    return finish_vertex


def _parse_vertexes_and_edges_counts():
    v1_str, v2_str, e_str = input().split()
    print(' '.join([v1_str, v2_str, e_str]))
    v1, v2, e = map(int, [v1_str, v2_str, e_str])
    return v1 + 1, v2 + 1, e


def mark_vertexes(vertex_list, current_vertex):
    if current_vertex.name == str(len(vertex_list) - 1):
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


main()

# for future tests
'''
4 4 7
0 4
1 4
1 5
2 5
3 5
3 6
3 7
'''


'''
4 4 7
0 4
1 4
1 5
2 4
3 5
3 6
3 7
'''
