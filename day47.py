MOD = 10**9 + 7

def count_odd_assignments(edges):
    n = len(edges) + 1

    # Build adjacency list
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Find maximum depth from root (node 1)
    max_depth = 0
    stack = [(1, 0, -1)]  # node, depth, parent

    while stack:
        node, depth, parent = stack.pop()
        max_depth = max(max_depth, depth)

        for nei in graph[node]:
            if nei != parent:
                stack.append((nei, depth + 1, node))

    # Number of edges in path = max_depth
    path_length = max_depth

    if path_length == 0:
        return 0

    # Half of all assignments produce odd sum
    return pow(2, path_length - 1, MOD)


# User Input
m = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v):")
for _ in range(m):
    u, v = map(int, input().split())
    edges.append([u, v])

print("Number of valid assignments:", count_odd_assignments(edges))


# sample input
# Enter number of edges: 4
# Enter edges (u v):
# 1 2
# 1 3
# 3 4
# 3 5

# sample output
# Number of valid assignments: 2