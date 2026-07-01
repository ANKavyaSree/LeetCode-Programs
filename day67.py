from collections import deque
import heapq

from python import sample

n = int(input("Enter grid size: "))

print("Enter the grid (0 for empty, 1 for thief):")
grid = [list(map(int, input().split())) for _ in range(n)]

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

# Multi-source BFS
dist = [[-1] * n for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            dist[i][j] = 0
            q.append((i, j))

while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

# Maximum Bottleneck Path
heap = [(-dist[0][0], 0, 0)]
visited = [[False] * n for _ in range(n)]

answer = 0

while heap:
    safe, x, y = heapq.heappop(heap)
    safe = -safe

    if visited[x][y]:
        continue

    visited[x][y] = True

    if x == n - 1 and y == n - 1:
        answer = safe
        break

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            heapq.heappush(heap, (-min(safe, dist[nx][ny]), nx, ny))

print("Maximum Safeness Factor:", answer)


# sample input
# Enter grid size: 3
# Enter the grid (0 for empty, 1 for thief):
# 0 0 1
# 0 0 0
# 0 0 0

# sample output
# Maximum Safeness Factor: 2
