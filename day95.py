from collections import Counter
from math import factorial

s = input("Enter a palindromic string: ")
k = int(input("Enter k: "))

freq = Counter(s)
half = []
middle = ""

for ch in sorted(freq):
    half.extend(ch * (freq[ch] // 2))
    if freq[ch] % 2:
        middle = ch

count = Counter(half)
length = len(half)

def ways(cnt):
    total = sum(cnt.values())
    res = factorial(total)
    for v in cnt.values():
        res //= factorial(v)
    return res

if ways(count) < k:
    print("")
else:
    left = []
    for _ in range(length):
        for ch in sorted(count):
            if count[ch] == 0:
                continue
            count[ch] -= 1
            w = ways(count)
            if w >= k:
                left.append(ch)
                break
            else:
                k -= w
                count[ch] += 1

    left = "".join(left)
    print("K-th lexicographically smallest palindromic permutation:", left + middle + left[::-1])
