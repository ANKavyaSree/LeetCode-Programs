# Day 169 - Apply Operations on Array to Maximize Sum of Squares
# User-input Python program

MOD = 10**9 + 7

nums = list(map(int, input("Enter array elements separated by spaces: ").split()))
k = int(input("Enter k: "))

bit_count = [0] * 31

for num in nums:
    for bit in range(31):
        if num & (1 << bit):
            bit_count[bit] += 1

total = 0

for _ in range(k):
    value = 0
    for bit in range(31):
        if bit_count[bit] > 0:
            value |= 1 << bit
            bit_count[bit] -= 1
    total = (total + value * value) % MOD

print("Maximum sum of squares:", total)
