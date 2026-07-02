import heapq

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter the grid (0 for safe, 1 for unsafe):")
grid = [list(map(int, input().split())) for _ in range(m)]

health = int(input("Enter initial health: "))

max_health = [[-1] * n for _ in range(m)]

start = health - grid[0][0]

if start <= 0:
    print(False)
    exit()

pq = [(-start, 0, 0)]
max_health[0][0] = start

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while pq:
    curr_health, x, y = heapq.heappop(pq)
    curr_health = -curr_health

    if x == m - 1 and y == n - 1:
        print(True)
        exit()

    if curr_health < max_health[x][y]:
        continue

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < m and 0 <= ny < n:
            next_health = curr_health - grid[nx][ny]

            if next_health > 0 and next_health > max_health[nx][ny]:
                max_health[nx][ny] = next_health
                heapq.heappush(pq, (-next_health, nx, ny))

print(False)


# sample input
# Enter number of rows: 3
# Enter number of columns: 5
# Enter the grid (0 for safe, 1 for unsafe):
# 0 1 0 0 0
# 0 1 0 1 0
# 0 0 0 1 0
# Enter initial health: 1

# sample output
# True