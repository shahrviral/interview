# Graphs


Graphs consist of Vertices (Nodes) and Edges (Relationships)

All trees are graphs

Graphs don't have a root node, you can start at any point.


**Vertices / Nodes** - Points in a graph containing data, they are connected by edges

**Edges** - Relations connecting various vertices. Can contain data and optionally direction

**Directed Graph** - All edges in graph have a direction

**Undirected Graph** - All edges in graph have no direction

**Cycle** - When you can start at one vertex and travel other edges back to the vertex

**Acyclic Graph** - Graph containing no cycles

**Directed Acyclic Graph (DAG)** - A directed graph containing no cycles


## Connectivity

**Connected Graph** - All vertices are reachable from all other vertices

**Disconnected Graph** - Graph with at least one vertex which can not be reached by other vertices

**Connectivity** - The amount of connectivity between the nodes. The minimum number of nodes needed to be removed to make the graph disconnected

**Weakly Connected Graph** - A directed graph where, replacing directed edges with undirected edges can make the graph strongly connected

    For example. If A -> B, C -> B , A -> C. If I remove the direction, all nodes have a path to all other nodes.

**Strongly Connected Graph** - Directed graph where every vertex has a path to every other vertex

## Representation

```
Vertex
 - [edges]
 - value
 
Edge
 - from_node
 - to_node
 - value
```

### Edge List

A 2D list of edges where each edge is represented as an array of 2 ids, refering to the start and end nodes

```
0 - 1
1 - 2
1 - 3
2 - 3

   E1      E2      E3      E4
[[0, 1], [1, 2], [1, 3], [2, 3]]
```

### Adjacency List

A 2D list of nodes where each node is represented by a list containing ids to all the nodes it connects to. 
The index of the inner list identifies the node in question, number of nodes should equal number of inner lists.

Nodes are considered adjacent to each other if they have an edge between them

```
0 - 1
1 - 2
1 - 3
2 - 3

  N1      N2      N3     N4
[[1], [0, 2, 3], [3], [1, 2]]
```

### Adjacency Matrix

A 2D representation of the graph where a n by n matrix of 0s and 1s is created.
A 1 is placed `[i][j]` position if nodes i and j are adjacent.  

Each edge is represented twice in the matrix i,j and j,i

Ideal representation for calculating the Node Degree (number of edges connected to a node)

```
0 - 1
1 - 2
1 - 3
2 - 3

    1  2  3  4
1 [[0, 1, 0, 0]
2  [1, 0, 1, 1]
3  [0, 1, 0, 1]
4  [0, 1, 1, 0]]
```
