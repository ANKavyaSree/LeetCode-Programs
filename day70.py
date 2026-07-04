from collections import defaultdict, deque

def min_score_path(n, roads):
    graph = defaultdict(list)

    for u, v, d in roads:
        graph[u].append((v, d))
        graph[v].append((u, d))

    visited = [False] * (n + 1)
    queue = deque([1])
    visited[1] = True

    answer = float('inf')

    while queue:
        city = queue.popleft()

        for nxt, dist in graph[city]:
            answer = min(answer, dist)

            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

    return answer


n = int(input("Enter number of cities: "))
m = int(input("Enter number of roads: "))

roads = []

print("Enter each road as: city1 city2 distance")

for _ in range(m):
    u, v, d = map(int, input().split())
    roads.append([u, v, d])

print("Minimum Score of Path:", min_score_path(n, roads))

# sample input
# Enter number of cities: 4
# Enter number of roads: 4
# Enter each road as: city1 city2 distance
# 1 2 9
# 2 3 6
# 2 4 5
# 1 4 7

# sample output
# Minimum Score of Path: 5