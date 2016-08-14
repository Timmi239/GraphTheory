class Mark(object):
    def __init__(self, prev_vertex_name, sign, value):
        self.prev_vertex_name = prev_vertex_name
        self.sign = sign
        self.value = value

    def __repr__(self):
        return '|prev_vertex_name: {}, sign: {}, value: {}|'.\
            format(self.prev_vertex_name, self.sign, str(self.value))
