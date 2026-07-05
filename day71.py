MOD = 10**9 + 7

def paths_with_max_score(board):
    n = len(board)

    score = [[-1] * n for _ in range(n)]
    ways = [[0] * n for _ in range(n)]

    score[n - 1][n - 1] = 0
    ways[n - 1][n - 1] = 1

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                continue

            best = -1
            cnt = 0

            for x, y in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                if x < n and y < n and score[x][y] != -1:
                    if score[x][y] > best:
                        best = score[x][y]
                        cnt = ways[x][y]
                    elif score[x][y] == best:
                        cnt = (cnt + ways[x][y]) % MOD

            if best == -1:
                continue

            value = int(board[i][j]) if board[i][j].isdigit() else 0
            score[i][j] = best + value
            ways[i][j] = cnt

    if score[0][0] == -1:
        return [0, 0]

    return [score[0][0], ways[0][0]]


n = int(input("Enter board size: "))

print("Enter the board rows:")
board = []
for _ in range(n):
    board.append(input().strip())

result = paths_with_max_score(board)

print("Maximum Score:", result[0])
print("Number of Paths:", result[1])


# sample input
# Enter board size: 3
# Enter the board rows:
# E23
# 2X2
# 12S

# sample output
# Maximum Score: 7
# Number of Paths: 1