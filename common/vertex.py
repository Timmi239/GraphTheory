from .mark import Mark


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.mark = Mark(None, None, 0)
        self.edges_list = []

    def add_edge(self, edge):
        self.edges_list.append(edge)

    def __repr__(self):
        return 'name: {}, edges_list: {}, mark: {}\n'.format(self.name, self.edges_list, str(self.mark))

    def __str__(self):
        return self.__repr__()
