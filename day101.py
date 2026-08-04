n = int(input("Enter the number of elements: "))
nums = list(map(int, input("Enter the elements: ").split()))

s = set(nums)
mn = min(nums)
mx = max(nums)

missing = []
for num in range(mn, mx + 1):
    if num not in s:
        missing.append(num)

print("Missing integers:", missing)
