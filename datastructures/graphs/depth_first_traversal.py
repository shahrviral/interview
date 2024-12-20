from graph import Graph


def depth_first_traversal_disconnected(graph):
    pass


def depth_first_traversal(start, size):
    pass


def _depth_first_traversal(vertex, visited):
    pass


def depth_first_traversal_set_disconnected(graph):
    pass

def depth_first_traversal_set(start):
    pass


def _depth_first_traversal_set(vertex, visited):
    pass


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 5)
g.add_edge(1, 6)
g.add_edge(2, 4)
g.add_edge(2, 6)
g.add_vertex(7)
# g.add_edge(3, 7)
g.add_edge(4, 6)
g.add_edge(5, 6)
print(g)
print(depth_first_traversal(g.get_vertex(0), len(g.vertices)))
print(depth_first_traversal_disconnected(g))
print(depth_first_traversal_set(g.get_vertex(0)))
print(depth_first_traversal_set_disconnected(g))
