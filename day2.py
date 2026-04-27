def hasValidPath(grid):
    rows = len(grid)
    cols = len(grid[0])

    # directions: left, right, up, down
    dirs = {
        1: [(0,-1),(0,1)],      # left-right
        2: [(-1,0),(1,0)],      # up-down
        3: [(0,-1),(1,0)],      # left-down
        4: [(0,1),(1,0)],       # right-down
        5: [(0,-1),(-1,0)],     # left-up
        6: [(0,1),(-1,0)]       # right-up
    }

    visited = set()

    def is_connected(r,c,nr,nc):
        # Check if neighbor connects back
        for dr,dc in dirs[grid[nr][nc]]:
            if nr+dr == r and nc+dc == c:
                return True
        return False

    def dfs(r,c):
        if (r,c) == (rows-1, cols-1):
            return True

        visited.add((r,c))

        for dr,dc in dirs[grid[r][c]]:
            nr,nc = r+dr,c+dc

            if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited:
                if is_connected(r,c,nr,nc):
                    if dfs(nr,nc):
                        return True
        return False

    return dfs(0,0)


# -------- User Input --------
m = int(input("Enter rows: "))
n = int(input("Enter columns: "))

print("Enter grid rows using numbers 1-6 separated by spaces:")
grid=[]

for i in range(m):
    row=list(map(int,input().split()))
    grid.append(row)

if hasValidPath(grid):
    print("true")
else:
    print("false")




#Sample input
# Enter rows: 2
# Enter columns: 3
# 2 4 3
# 6 5 2

#sample output
#True