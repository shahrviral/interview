from graph import Graph


def depth_first_search(start, id):
    pass


def _depth_first_search(vertex, id, visited):
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
print(depth_first_search(g.get_vertex(1), 4))
print(depth_first_search(g.get_vertex(1), 7))
print(depth_first_search(g.get_vertex(0), 6))
