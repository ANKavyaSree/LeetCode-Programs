MOD = 10**9 + 7

def unique_paths(grid):
    m = len(grid)
    n = len(grid[0])

    # right[i][j]: number of paths entering (i, j) from the left
    # down[i][j]: number of paths entering (i, j) from above
    right = [[0] * n for _ in range(m)]
    down = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                ways = 1
            else:
                ways = (right[i][j] + down[i][j]) % MOD

            if ways == 0:
                continue

            if i == m - 1 and j == n - 1:
                return ways

            if grid[i][j] == 1:
                # A path entering from the left is reflected downward.
                if right[i][j] and i + 1 < m:
                    down[i + 1][j] = (
                        down[i + 1][j] + right[i][j]
                    ) % MOD

                # A path entering from above is reflected to the right.
                if down[i][j] and j + 1 < n:
                    right[i][j + 1] = (
                        right[i][j + 1] + down[i][j]
                    ) % MOD

            else:
                # From an empty cell, the robot may move right or down.
                if j + 1 < n:
                    right[i][j + 1] = (
                        right[i][j + 1] + ways
                    ) % MOD

                if i + 1 < m:
                    down[i + 1][j] = (
                        down[i + 1][j] + ways
                    ) % MOD

    return 0


if __name__ == "__main__":
    # Input format:
    # m n
    # followed by m rows, each containing n space-separated 0s and 1s.
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]

    print(unique_paths(grid))
