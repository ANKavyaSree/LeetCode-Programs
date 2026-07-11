from collections import deque

def countCompleteComponents(n: int, edges: list[list[int]]) -> int:
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [False] * n
    complete_components = 0
    
    for i in range(n):
        if not visited[i]:
            # Start BFS for a new component
            queue = deque([i])
            visited[i] = True
            
            vertex_count = 0
            edge_degree_sum = 0
            
            while queue:
                curr = queue.popleft()
                vertex_count += 1
                edge_degree_sum += len(adj[curr])
                
                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            # Each undirected edge is counted twice across the component
            actual_edges = edge_degree_sum // 2
            expected_edges = (vertex_count * (vertex_count - 1)) // 2
            
            if actual_edges == expected_edges:
                complete_components += 1
                
    return complete_components

if __name__ == "__main__":
    print("--- Complete Connected Components Counter ---")
    try:
        # Read total vertices
        n = int(input("Enter number of vertices (n): ").strip())
        
        # Read total edges to loop through
        num_edges = int(input("Enter total number of edges: ").strip())
        
        edges = []
        if num_edges > 0:
            print(f"Enter {num_edges} lines of edges (format: u v):")
            for _ in range(num_edges):
                u, v = map(int, input().split())
                edges.append([u, v])
        
        # Calculate result
        result = countCompleteComponents(n, edges)
        print(f"\nOutput: {result}")
        
    except ValueError:
        print("Invalid input format. Please enter integers only.")

# sample input
# Enter number of vertices (n): 6
# Enter total number of edges: 5
# Enter 5 lines of edges (format: u v):
# 0 1
# 0 2
# 1 2
# 3 4
# 3 5

# sample output
# 1