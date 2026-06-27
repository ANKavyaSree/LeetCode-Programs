from collections import Counter

n = int(input("Enter number of elements: "))

print("Enter array elements:")
nums = list(map(int, input().split()))

cnt = Counter(nums)

ans = 1

if 1 in cnt:
    ones = cnt[1]
    if ones % 2 == 0:
        ones -= 1
    ans = max(ans, ones)

for x in sorted(cnt):
    if x == 1:
        continue

    cur = 0
    val = x

    while cnt[val] >= 2:
        cur += 2
        if val > 10**9:
            break
        val *= val

    if cnt[val] == 1:
        cur += 1
    else:
        cur -= 1

    ans = max(ans, cur)

print("Maximum subset length:", ans)


# sample input
# Enter number of elements: 5
# Enter array elements:
# 5 4 1 2 2

# sample output
# Maximum subset length: 3