from math import gcd

def gcd_sum(nums):
    prefix_gcd = []
    mx = 0

    for num in nums:
        mx = max(mx, num)
        prefix_gcd.append(gcd(num, mx))

    prefix_gcd.sort()

    ans = 0
    left, right = 0, len(prefix_gcd) - 1

    while left < right:
        ans += gcd(prefix_gcd[left], prefix_gcd[right])
        left += 1
        right -= 1

    return ans

n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter the elements: ").split()))

if len(nums) != n:
    print("Error: Number of elements does not match n.")
else:
    print("Sum of GCDs:", gcd_sum(nums))
