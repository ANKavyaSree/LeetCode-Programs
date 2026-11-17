s = input("Enter the string: ").strip()
k = int(input("Enter the value of k: "))

n = len(s)

# cost[i][j] = minimum changes to make s[i:j+1] a semi-palindrome
cost = [[0] * n for _ in range(n)]

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        best = float("inf")

        for d in range(1, length):
            if length % d != 0:
                continue

            changes = 0
            for r in range(d):
                group = s[i + r:j + 1:d]
                left, right = 0, len(group) - 1

                while left < right:
                    if group[left] != group[right]:
                        changes += 1
                    left += 1
                    right -= 1

            best = min(best, changes)

        cost[i][j] = best

# dp[i][p] = minimum changes for first i characters in p parts
INF = float("inf")
dp = [[INF] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 0

for p in range(1, k + 1):
    for i in range(2 * p, n + 1):
        for j in range(2 * (p - 1), i - 1):
            if i - j >= 2 and dp[j][p - 1] != INF:
                dp[i][p] = min(
                    dp[i][p],
                    dp[j][p - 1] + cost[j][i - 1]
                )

print(dp[n][k])
