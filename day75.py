MOD = 10**9 + 7

s = input("Enter the string: ")

q = int(input("Enter number of queries: "))

queries = []

print("Enter queries (l r):")
for _ in range(q):
    l, r = map(int, input().split())
    queries.append((l, r))

n = len(s)

pref_sum = [0] * (n + 1)
pref_cnt = [0] * (n + 1)
pref_val = [0] * (n + 1)

pow10 = [1] * (n + 1)
for i in range(1, n + 1):
    pow10[i] = (pow10[i - 1] * 10) % MOD

for i, ch in enumerate(s):
    pref_sum[i + 1] = pref_sum[i]
    pref_cnt[i + 1] = pref_cnt[i]
    pref_val[i + 1] = pref_val[i]

    if ch != '0':
        d = int(ch)
        pref_sum[i + 1] += d
        pref_cnt[i + 1] += 1
        pref_val[i + 1] = (pref_val[i] * 10 + d) % MOD

answer = []

for l, r in queries:
    total_sum = pref_sum[r + 1] - pref_sum[l]
    cnt = pref_cnt[r + 1] - pref_cnt[l]

    if cnt == 0:
        answer.append(0)
        continue

    x = (pref_val[r + 1] - pref_val[l] * pow10[cnt]) % MOD
    answer.append((x * total_sum) % MOD)

print("Answer:", answer)

# sample input 
# Enter the string: 10203004
# Enter number of queries: 3
# Enter queries (l r):
# 0 7
# 1 3
# 4 6

# sample output
# Answer: [12340, 4, 9]