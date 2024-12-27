# TP1 Exercise

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def is_path_exist(self, start, end):
        visited = set()
        return self._dfs(start, end, visited)
    
    def _dfs(self, current, target, visited):
        if current == target:
            return True
        visited.add(current)
        for neighbor in self.graph[current]:
            if neighbor not in visited:
                if self._dfs(neighbor, target, visited):
                    return True
        return False

def main():
    graph = Graph()
    
    edges = [
        (1, 2), 
        (2, 5), 
        (3, 6), (4, 6), (4, 7), (6, 7)
    ]
    
    for u, v in edges:
        graph.add_edge(u, v)
    
    try:
        start = int(input("Enter the start node: "))
        end = int(input("Enter the end node: "))
        
        if graph.is_path_exist(start, end):
            print("True: Path exists between node {} and node {}".format(start, end))
        else:
            print("False: No path exists between node {} and node {}".format(start, end))
    except ValueError:
        print("Please enter valid integers for nodes.")

if __name__ == "__main__":
    main()
