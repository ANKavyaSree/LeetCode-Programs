# Day 186 - Palindromic Path Queries in a Tree
# User-input Python program

def palindromePath(n, edges, s, queries):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    LOG = n.bit_length()
    parent = [0] * n
    depth = [0] * n
    tin = [0] * n
    tout = [0] * n
    prefix = [0] * n

    # Iterative DFS
    timer = 0
    stack = [(0, -1, 0)]
    while stack:
        u, p, state = stack.pop()
        if state == 0:
            parent[u] = u if p == -1 else p
            tin[u] = timer
            timer += 1
            node_bit = 1 << (ord(s[u]) - ord('a'))
            prefix[u] = node_bit if p == -1 else prefix[p] ^ node_bit
            stack.append((u, p, 1))
            for v in reversed(graph[u]):
                if v != p:
                    depth[v] = depth[u] + 1
                    stack.append((v, u, 0))
        else:
            tout[u] = timer - 1

    # Binary lifting for LCA
    up = [[0] * n for _ in range(LOG)]
    up[0] = parent[:]
    for k in range(1, LOG):
        for u in range(n):
            up[k][u] = up[k - 1][up[k - 1][u]]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        k = 0
        while diff:
            if diff & 1:
                u = up[k][u]
            diff >>= 1
            k += 1
        if u == v:
            return u
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return parent[u]

    # Fenwick tree: subtree range XOR updates, point queries
    fenwick = [0] * (n + 2)

    def fenwick_update(i, value):
        while i < len(fenwick):
            fenwick[i] ^= value
            i += i & -i

    def point_query(i):
        result = 0
        while i > 0:
            result ^= fenwick[i]
            i -= i & -i
        return result

    def range_update(left, right, value):
        fenwick_update(left + 1, value)
        fenwick_update(right + 2, value)

    chars = list(s)
    answer = []

    for query in queries:
        parts = query.split()
        if parts[0] == "update":
            u = int(parts[1])
            c = parts[2]
            old_bit = 1 << (ord(chars[u]) - ord('a'))
            new_bit = 1 << (ord(c) - ord('a'))
            if old_bit != new_bit:
                range_update(tin[u], tout[u], old_bit ^ new_bit)
                chars[u] = c
        else:
            u = int(parts[1])
            v = int(parts[2])
            pu = prefix[u] ^ point_query(tin[u] + 1)
            pv = prefix[v] ^ point_query(tin[v] + 1)
            ancestor = lca(u, v)
            ancestor_bit = 1 << (ord(chars[ancestor]) - ord('a'))
            mask = pu ^ pv ^ ancestor_bit
            answer.append((mask & (mask - 1)) == 0)

    return answer


# Input:
# n
# n-1 lines: u v
# string s
# q
# q query lines (query u v / update u c)

n = int(input().strip())
edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append([u, v])

s = input().strip()
q = int(input().strip())
queries = [input().strip() for _ in range(q)]

print(palindromePath(n, edges, s, queries))
