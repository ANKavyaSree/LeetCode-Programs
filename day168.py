# Day 168 - Sum of Squares of Special Elements
# User-input Python program

nums = list(map(int, input("Enter array elements separated by spaces: ").split()))

n = len(nums)
total = 0

for i in range(1, n + 1):
    if n % i == 0:
        total += nums[i - 1] ** 2

print("Sum of squares of special elements:", total)
