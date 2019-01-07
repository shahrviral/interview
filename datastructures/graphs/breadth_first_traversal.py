from graph import Graph


def breadth_first_traversal(start, size):
    visited = [None] * size
    queue = [start]
    visited[start.id] = start.id
    while queue:
        vertex = queue.pop(0)
        for child_vertex in vertex.connected_to:
            if visited[child_vertex.id] is None:
                queue.append(child_vertex)
                visited[child_vertex.id] = child_vertex.id
    return visited


def breadth_first_traversal_set(start):
    visited = set()
    queue = [start]
    visited.add(start.id)
    while queue:
        vertex = queue.pop(0)
        for child_vertex in vertex.connected_to:
            if child_vertex.id not in visited:
                queue.append(child_vertex)
                visited.add(child_vertex.id)
    return visited



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
