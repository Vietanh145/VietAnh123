# TP4 Exercise

import numpy as np

nodes = 9

matrix = np.inf * np.ones((nodes, nodes))

data = [
    (1, 2, 4), (1, 5, 1), (1, 7, 2),
    (2, 3, 7), (2, 6, 5),
    (3, 4, 1), (3, 6, 8),
    (4, 6, 6), (4, 7, 4), (4, 8, 3),
    (5, 6, 9), (5, 7, 10),
    (6, 9, 2),
    (7, 9, 8),
    (8, 9, 1),
    (9, 8, 7)
]

for start, end, w in data:
    matrix[start - 1, end - 1] = w

format_value = lambda x: " inf" if x == float('inf') else f"{int(x):4d}"

def print_matrix(m):
    formatted = [[format_value(v) for v in row] for row in m]
    print("Adjacency Matrix:")
    for line in formatted:
        print("  [" + " ".join(line) + "]")

print_matrix(matrix)

# Prim's Algorithm
def prim_mst(graph, total_nodes, start):
    visited = [False] * total_nodes
    visited[start] = True
    mst_edges = []
    mst_weight = 0

    while len(mst_edges) < total_nodes - 1:
        smallest = (None, None, float('inf'))
        for u in range(total_nodes):
            if visited[u]:
                for v in range(total_nodes):
                    if not visited[v] and graph[u, v] != float('inf'):
                        if graph[u, v] < smallest[2]:
                            smallest = (u, v, graph[u, v])

        if smallest[0] is None or smallest[1] is None:
            print("MST cannot be completed from the given root node.")
            return [], 0

        u, v, w = smallest
        mst_edges.append((u + 1, v + 1, w))
        mst_weight += w
        visited[v] = True

    return mst_edges, mst_weight

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

# Kruskal's Algorithm
def kruskal_mst(graph, total_nodes):
    all_edges = []
    for i in range(total_nodes):
        for j in range(i + 1, total_nodes):
            if graph[i, j] != float('inf'):
                all_edges.append((i, j, graph[i, j]))

    all_edges.sort(key=lambda x: x[2])

    uf = UnionFind(total_nodes)
    mst_edges = []
    mst_weight = 0

    for u, v, w in all_edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((u + 1, v + 1, w))
            mst_weight += w

    return mst_edges, mst_weight

while True:
    try:
        root = int(input("\nEnter the root node for Prim's Algorithm (1-9): ")) - 1
        if root < 0 or root >= nodes:
            raise ValueError("Root node must be between 1 and 9.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")

prim_result, prim_total = prim_mst(matrix, nodes, root)
if prim_result:
    print("\nMinimum Spanning Tree (MST) from Prim's Algorithm:")
    for edge in prim_result:
        print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
    print(f"Total weight of MST: {prim_total}")
else:
    print("No MST could be formed from the given root node.")

kruskal_result, kruskal_total = kruskal_mst(matrix, nodes)

print("\nMinimum Spanning Tree (MST) from Kruskal's Algorithm:")
for edge in kruskal_result:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
print(f"Total weight of MST: {kruskal_total}")
