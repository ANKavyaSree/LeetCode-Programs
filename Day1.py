def containsCycle(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False]*cols for _ in range(rows)]

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    def dfs(r, c, pr, pc, char):
        if visited[r][c]:
            return True

        visited[r][c] = True

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char:
                # Skip parent cell
                if nr == pr and nc == pc:
                    continue

                if dfs(nr, nc, r, c, char):
                    return True
        return False

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                if dfs(i, j, -1, -1, grid[i][j]):
                    return True

    return False


# -------- User Input Section --------

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter grid rows (example: a a a b)")
grid = []

for i in range(m):
    row = input().split()
    grid.append(row)

if containsCycle(grid):
    print("true")
else:
    print("false")

#sample input
#Enter number of rows: 4
#Enter number of columns: 4
#Enter grid rows:
#a a a a
#a b b a
#a b b a
#a a a a

#Output
#true