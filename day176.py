# day176.py
# Find Target Indices After Sorting Array

nums = list(map(int, input("Enter array elements separated by spaces: ").split()))
target = int(input("Enter target: "))

nums.sort()
result = []

for i in range(len(nums)):
    if nums[i] == target:
        result.append(i)

print(result)
