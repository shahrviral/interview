class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def connect_to(self, vertex, edge_weight=0):
        self.connected_to[vertex] = edge_weight

    def __repr__(self):
        return str(self.id)

    def __str__(self):
        return f'{self.id} -> {[v.id for v in self.connected_to]}'


class Graph:

    def __init__(self, directed=False):
        self.vertices = {}
        self.directed = directed

    def add_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]

    def __contains__(self, vertex_key):
        return vertex_key in self.vertices

    def add_edge(self, from_key, to_key, edge_value=0):

        if from_key not in self.vertices:
            self.vertices[from_key] = Vertex(from_key)
        if to_key not in self.vertices:
            self.vertices[to_key] = Vertex(to_key)

        self.vertices[from_key].connect_to(self.vertices[to_key], edge_value)
        if not self.directed:
            self.vertices[to_key].connect_to(self.vertices[from_key], edge_value)

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
