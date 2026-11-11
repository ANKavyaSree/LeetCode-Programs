# Day 199 - Minimum Cost to Meet Both Requirements

cost1, cost2, costBoth, need1, need2 = map(int, input().split())

both = min(need1, need2)

ans = both * min(costBoth, cost1 + cost2)

remaining1 = need1 - both
remaining2 = need2 - both

ans += remaining1 * min(cost1, costBoth)
ans += remaining2 * min(cost2, costBoth)

print(ans)
