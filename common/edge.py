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
