def get_input_graph_in_dict():
    vertex_count, edges_count = _get_vertex_and_edges_counts()
    edges_dict = dict()

    for i in range(1, vertex_count + 1):
        edges_dict[str(i)] = ()

    for _ in range(edges_count):
        new_edge = input().split()
        if new_edge[1] not in edges_dict[new_edge[0]]:
            edges_dict[new_edge[0]].add(new_edge[1])
            edges_dict[new_edge[1]].add(new_edge[0])
    return edges_dict


def get_input_graph_in_list():
    vertex_count, edges_count = _get_vertex_and_edges_counts()
    edges_list = []

    for _ in range(edges_count):
        new_edge = input().split()
        if new_edge not in edges_list and list(reversed(new_edge)) not in edges_list:
            edges_list.append(new_edge)
    return edges_list, vertex_count


def _get_vertex_and_edges_counts():
    inp = input().split()
    vertex_count, edges_count = int(inp[0]), int(inp[1])
    return vertex_count, edges_count
