from collections import deque

n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v cost):")
for _ in range(m):
    u, v, cost = map(int, input().split())
    edges.append((u, v, cost))

online = list(map(int, input("Enter online status (0/1): ").split()))
online = [bool(x) for x in online]

k = int(input("Enter maximum recovery cost: "))

graph = [[] for _ in range(n)]
indegree = [0] * n

for u, v, cost in edges:
    graph[u].append((v, cost))
    indegree[v] += 1

topo = []
q = deque(i for i in range(n) if indegree[i] == 0)

while q:
    u = q.popleft()
    topo.append(u)

    for v, _ in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)


def can(score):
    INF = 10**18
    dist = [INF] * n
    dist[0] = 0

    for u in topo:
        if dist[u] == INF:
            continue

        if u != 0 and u != n - 1 and not online[u]:
            continue

        for v, cost in graph[u]:
            if cost < score:
                continue

            if v != n - 1 and not online[v]:
                continue

            if dist[u] + cost <= k:
                dist[v] = min(dist[v], dist[u] + cost)

    return dist[n - 1] <= k


left = 0
right = max(cost for _, _, cost in edges)
answer = -1

while left <= right:
    mid = (left + right) // 2

    if can(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print("Maximum Path Score:", answer)


# sample input
# Enter number of nodes: 4
# Enter number of edges: 4
# Enter edges (u v cost):
# 0 1 5
# 1 3 10
# 0 2 3
# 2 3 4
# Enter online status (0/1): 1 1 1 1
# Enter maximum recovery cost: 10

# sample output
# Maximum Path Score: 3