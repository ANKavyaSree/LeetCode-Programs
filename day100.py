n = int(input("Enter the number of stones: "))
stoneValue = list(map(int, input("Enter the stone values: ").split()))

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    best = -10**18
    take = 0
    for k in range(3):
        if i + k < n:
            take += stoneValue[i + k]
            best = max(best, take - dp[i + k + 1])
    dp[i] = best

if dp[0] > 0:
    print("Winner: Alice")
elif dp[0] < 0:
    print("Winner: Bob")
else:
    print("Winner: Tie")
