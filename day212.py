from math import gcd, lcm

nums = list(map(int, input("Enter array elements: ").split()))

n = len(nums)
ans = 0

for i in range(n):
    prod = 1
    g = 0
    l = 1

    for j in range(i, n):
        prod *= nums[j]
        g = gcd(g, nums[j])
        l = lcm(l, nums[j])

        if prod == g * l:
            ans = max(ans, j - i + 1)

print("Maximum length:", ans)
