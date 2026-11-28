# Day 216 - Maximum Number of Items From Sale II
# User-input version

n = int(input("Enter number of items: "))
items = []

for i in range(n):
    f, p = map(int, input("Enter factor and price: ").split())
    items.append([f, p])

budget = int(input("Enter budget: "))

freq = [0] * (n + 1)
for f, p in items:
    freq[f] += 1

gain = [0] * (n + 1)
for f in range(1, n + 1):
    for x in range(f, n + 1, f):
        gain[f] += freq[x]
    if gain[f] > 0:
        gain[f] -= 1

min_price = min(p for f, p in items)

batches = {}
for f, p in items:
    g = gain[f]
    if g > 0 and p < 2 * min_price:
        batches[p] = batches.get(p, 0) + g

ans = 0
for p in sorted(batches):
    if budget < p:
        break
    take = min(batches[p], budget // p)
    ans += 2 * take
    budget -= take * p

ans += budget // min_price

print("Maximum number of items:", ans)
