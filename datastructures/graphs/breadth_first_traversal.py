from graph import Graph


def breadth_first_traversal(start, size):
    pass


def breadth_first_traversal_set(start):
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
print(breadth_first_traversal(g.get_vertex(0), len(g.vertices)))
print(breadth_first_traversal_set(g.get_vertex(0)))
