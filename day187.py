# Day 187 - Shortest Path With at Most K Consecutive Identical Characters
# User-input Python program

import heapq


def shortestPath(n, edges, labels, k):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))

    inf = float("inf")
    dist = [[inf] * (k + 1) for _ in range(n)]
    dist[0][1] = 0
    pq = [(0, 0, 1)]  # cost, node, consecutive count

    while pq:
        cost, u, count = heapq.heappop(pq)

        if cost != dist[u][count]:
            continue
        if u == n - 1:
            return cost

        for v, weight in graph[u]:
            new_count = count + 1 if labels[v] == labels[u] else 1
            if new_count > k:
                continue

            new_cost = cost + weight
            if new_cost < dist[v][new_count]:
                dist[v][new_count] = new_cost
                heapq.heappush(pq, (new_cost, v, new_count))

    return -1


# Input format:
# First line: n m
# Next m lines: u v weight
# Next line: labels
# Last line: k

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append([u, v, w])

labels = input().strip()
k = int(input().strip())

print(shortestPath(n, edges, labels, k))
