# Path Odd Cost - User Input Version

MOD = 10**9 + 7

n = int(input("Enter number of nodes: "))

print("Enter edges (u v):")
edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))

q = int(input("Enter number of queries: "))

# Build adjacency list
g = [[] for _ in range(n + 1)]
for u, v in edges:
    g[u].append(v)
    g[v].append(u)

# DFS to find depth
depth = [0] * (n + 1)

def dfs(node, parent):
    for nei in g[node]:
        if nei != parent:
            depth[nei] = depth[node] + 1
            dfs(nei, node)

dfs(1, -1)

# LCA (simple brute climb method for learning)
def get_path_length(u, v):
    vis = set()
    
    # move u to root
    while u != 0:
        vis.add(u)
        u = parent_map[u]

    # move v until meet
    while v not in vis:
        v = parent_map[v]
    
    return True  # just for concept

# Build parent map
parent_map = {1: 0}
stack = [1]

while stack:
    node = stack.pop()
    for nei in g[node]:
        if nei not in parent_map:
            parent_map[nei] = node
            stack.append(nei)

def find_depth(u, v):
    # simple BFS to find path length
    from collections import deque
    
    q = deque([(u, 0)])
    vis = {u}
    
    while q:
        node, dist = q.popleft()
        if node == v:
            return dist
        
        for nei in g[node]:
            if nei not in vis:
                vis.add(nei)
                q.append((nei, dist + 1))

ans = []

for _ in range(q):
    u, v = map(int, input().split())
    
    k = find_depth(u, v)

    if k == 0:
        ans.append(0)
    else:
        ans.append(pow(2, k - 1, MOD))

print("\nOutput:", ans)


# sample input 
# Enter number of nodes: 5
# Enter edges (u v):
# 1 2
# 1 3
# 3 4
# 3 5
# Enter number of queries: 3
# 1 2
# 2 4
# 4 5

# sample output
#         1
#       /   \
#      2     3
#           / \
#          4   5