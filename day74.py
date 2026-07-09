n = int(input())
nums = list(map(int, input().split()))
maxDiff = int(input())

q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

comp = [0] * n
cid = 0

for i in range(1, n):
    if nums[i] - nums[i - 1] > maxDiff:
        cid += 1
    comp[i] = cid

ans = [comp[u] == comp[v] for u, v in queries]
print(ans)

# sample input
# 4
# 2 5 6 8
# 2
# 4
# 0 1
# 0 2
# 1 3
# 2 3

# sample output
# [False, False, True, True]