# day183.py
# 3619. Count Islands With Total Value Divisible by K
# User-input Python program

def count_islands(grid, k):
    m, n = len(grid), len(grid[0])
    count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                continue

            stack = [(i, j)]
            total = grid[i][j]
            grid[i][j] = 0

            while stack:
                r, c = stack.pop()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                        total += grid[nr][nc]
                        stack.append((nr, nc))
                        grid[nr][nc] = 0

            if total % k == 0:
                count += 1

    return count


# Input format:
# First line: m n
# Next m lines: n space-separated integers
# Last line: k
m, n = map(int, input().split())
grid = []

for _ in range(m):
    grid.append(list(map(int, input().split())))

k = int(input())

print(count_islands(grid, k))
