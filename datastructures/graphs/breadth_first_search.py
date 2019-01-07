from graph import Graph


def breadth_first_search(start, id):
    queue = [start]
    visited = set()
    visited.add(start.id)
    while queue:
        vertex = queue.pop(0)
        if vertex.id == id:
            return True
        for child_vertex in vertex.connected_to:
            if child_vertex.id not in visited:
                queue.append(child_vertex)
                visited.add(child_vertex.id)
    return False


if __name__ == '__main__':
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
    print(breadth_first_search(g.get_vertex(1), 1))
    print(breadth_first_search(g.get_vertex(1), 7))
    print(breadth_first_search(g.get_vertex(0), 6))
