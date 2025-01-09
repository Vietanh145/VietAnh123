# TP2 Exercise

import igraph as ig

edges = [
    (1, 2), (1, 4), (2, 3), (2, 6), 
    (3, 7), (3, 8), (4, 5), (5, 5), 
    (5, 9), (6, 5), (6, 7), 
    (7, 5), (7, 8), (8, 9),
]

nodes = sorted(set(u for edge in edges for u in edge))
node_to_index = {node: i for i, node in enumerate(nodes)}
edges_mapped = [(node_to_index[u], node_to_index[v]) for u, v in edges]

G = ig.Graph(directed=True)
G.add_vertices(len(nodes))
G.add_edges(edges_mapped)

adj_matrix = G.get_adjacency()

print("Adjacency Matrix:")
for row in adj_matrix: 
    print(list(row)) 

weakly_connected = len(G.connected_components(mode="weak"))
strongly_connected = len(G.connected_components(mode="strong"))

print(f"Weakly Connected Components: {weakly_connected}")
print(f"Strongly Connected Components: {strongly_connected}")
