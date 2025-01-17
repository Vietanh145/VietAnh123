# TP5 Exercise

import pandas as pd
import heapq

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M']
edges = [
    ('A', 'C', 1), ('A', 'B', 4), ('B', 'F', 3),
    ('C', 'D', 8), ('C', 'F', 7), ('D', 'H', 5),
    ('F', 'H', 1), ('F', 'E', 1), ('E', 'H', 2),
    ('H', 'G', 3), ('H', 'M', 7), ('H', 'L', 6),
    ('G', 'M', 4), ('M', 'L', 1), ('L', 'G', 4), ('L', 'E', 2)
]

n = len(vertices)

adj_matrix = pd.DataFrame(float('inf'), index=vertices, columns=vertices)

for u, v, w in edges:
    adj_matrix.at[u, v] = w
    adj_matrix.at[v, u] = w

# Display the adjacency matrix
def display_matrix(matrix):
    print("Adjacency Matrix:")
    for row in matrix.values:
        print(f"[{' '.join([f'{val:4}' if val != float('inf') else ' inf' for val in row])}]")

display_matrix(adj_matrix)

# Dijkstra's Algorithm: Finding the shortest path
def find_shortest_path(graph, start, end):
    # Map vertex names to indices
    idx_map = {vertex: index for index, vertex in enumerate(vertices)}
    start_idx = idx_map[start]
    end_idx = idx_map[end]

    distances = [float('inf')] * n
    distances[start_idx] = 0
    previous = [None] * n

    pq = [(0, start_idx)]

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        # Check each neighbor of the current node
        for neighbor, weight in enumerate(graph.iloc[node]):
            if weight != float('inf'):
                new_dist = dist + weight
                # Update the distance if a shorter path is found
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = node
                    heapq.heappush(pq, (new_dist, neighbor))

    path = []
    current = end_idx
    while current is not None:
        path.append(vertices[current])
        current = previous[current]
    path.reverse()

    return path, distances[end_idx]

# Input source node and target node
def get_valid_node_input():
    while True:
        source_node = input("Enter the source node S (A-M): ").strip().upper()
        target_node = input("Enter the target node T (A-M): ").strip().upper()

        # Check if the input nodes are valid
        if source_node in vertices and target_node in vertices:
            return source_node, target_node
        else:
            print("Invalid input. Please input valid nodes (A-M).")

source_node, target_node = get_valid_node_input()

# Find and display the shortest path and its weight
path, weight = find_shortest_path(adj_matrix, source_node, target_node)
print(f"Shortest path to move from {source_node} to {target_node}: {' -> '.join(path)}")
print(f"The weighted sum of shoretest path: {weight}")
