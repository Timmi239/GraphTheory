import sys

from helpers import get_input_graph_in_dict


# Найдите все точки сочленения в графе.
#
# На вход программе подаётся описание графа, состоящее не более чем из 100000 строк.
# Каждая строка описывает очередное ребро: содержит два номера вершин, которые данное ребро соединяет.
# Номера разделены пробелом.
# Гарантируется, что ребра определяют связный граф, вершины которого пронумерованы числами от 0 до некоторого n.
#
# Выведите единственную строку — список номеров точек сочленения графа через пробел.


def dfs(v, adj_list, timer, p):
    global visited, tin, fup, result
    visited[int(v)] = True
    tin[int(v)] = timer
    fup[int(v)] = timer
    timer += 1
    children = 0
    for w in adj_list[v]:
        if w == p:
            continue
        if not visited[int(w)]:
            dfs(w, adj_list, timer, v)
            fup[int(v)] = min(fup[int(v)], fup[int(w)])
            if fup[int(w)] >= tin[int(v)] and p != '-1':
                result.add(v)
            children += 1
        else:
            fup[int(v)] = min(fup[int(v)], tin[int(w)])
    if p == '-1' and children > 1:
        result.add(v)


visited = []
tin = []
fup = []
result = set()


def main():
    sys.setrecursionlimit(100000)
    adj_list = get_input_graph_in_dict(start_vertex_number=0)
    global visited, tin, fup, result
    visited = [False] * len(adj_list)
    tin = [-1] * len(adj_list)
    fup = [-1] * len(adj_list)
    dfs('0', adj_list, 0, '-1')
    print(' '.join(sorted(result, key=int)))


if __name__ == '__main__':
    main()
