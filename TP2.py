# TP2 Exercise

def perform_dfs(node, component, graph, visited_nodes):
    stack = [node]  
    while stack:
        current_node = stack.pop()  
        if current_node not in visited_nodes:
            visited_nodes.add(current_node)  
            component.add(current_node + 1)  
            neighbors_to_explore = [index for index, is_connected in enumerate(graph[current_node]) if is_connected == 1 and index not in visited_nodes]
            stack.extend(neighbors_to_explore)  

def get_connected_components(graph, directed=True):
    visited_nodes = set()  
    components = []  

    for node in range(len(graph)):
        if node not in visited_nodes:  
            current_component = set()  
            perform_dfs(node, current_component, graph, visited_nodes)  
            components.append(current_component) 
    return components

def count_components(directed_graph):
    undirected_graph = []
    for i in range(len(directed_graph)):
        row = []
        for j in range(len(directed_graph)):
            if directed_graph[i][j] == 1 or directed_graph[j][i] == 1:
                row.append(1) 
            else:
                row.append(0)
        undirected_graph.append(row)
    directed_components = get_connected_components(directed_graph, directed=True)
    undirected_components = get_connected_components(undirected_graph, directed=False)

    return {"strong": directed_components, "weak": undirected_components}

if __name__ == '__main__':
    graph = [
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    
    result = count_components(graph)

# Print output 
    print("Strong Components (Strongly Connected):")
    for component in result["strong"]:
        print(f"Component: {component}")
    
    print("\nWeak Components (Weakly Connected):")
    for component in result["weak"]:
        print(f"Component: {component}")
