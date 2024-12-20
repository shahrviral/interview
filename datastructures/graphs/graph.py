class Vertex:
    def __init__(self, key):
        pass

    def connect_to(self, vertex, edge_weight=0):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        return f'{self.id} -> {[v.id for v in self.connected_to]}'


class Graph:

    def __init__(self, directed=False):
        pass

    def add_vertex(self, key):
        [pass]

    def get_vertex(self, key):
        pass

    def __contains__(self, vertex_key):
        pass

    def add_edge(self, from_key, to_key, edge_value=0):
        pass

    def __iter__(self):
        return iter(self.vertices.values())

    def __repr__(self):
        return str(self.vertices)

    def __str__(self):
        return '\n'.join([f'{str(vertex)}' for vertex in self.vertices.values()])


if __name__ == '__main__':
    g = Graph()
    g.add_vertex('a')
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'd')

    print(g)
