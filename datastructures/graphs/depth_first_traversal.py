from graph import Graph


def depth_first_traversal_disconnected(graph):
    visited = [None] * len(graph.vertices)
    for vertex in graph:
        if vertex.id not in visited:
            _depth_first_traversal(vertex, visited)
    return visited


def depth_first_traversal(start, size):
    visited = [None] * size
    _depth_first_traversal(start, visited)
    return visited


def _depth_first_traversal(vertex, visited):
    visited[vertex.id] = vertex.id
    for child_vertex in vertex.connected_to:
        if child_vertex.id not in visited:
            _depth_first_traversal(child_vertex, visited)


def depth_first_traversal_set_disconnected(graph):
    visited = set()
    for vertex in graph:
        if vertex.id not in visited:
            _depth_first_traversal_set(vertex, visited)
    return visited

def depth_first_traversal_set(start):
    visited = set()
    _depth_first_traversal_set(start, visited)
    return visited


def _depth_first_traversal_set(vertex, visited):
    visited.add(vertex.id)
    for child_vertex in vertex.connected_to:
        if child_vertex.id not in visited:
            _depth_first_traversal_set(child_vertex, visited)


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
