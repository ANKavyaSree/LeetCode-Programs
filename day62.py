from bisect import bisect_left, insort

n = int(input("Enter size of array: "))

print("Enter array elements:")
nums = list(map(int, input().split()))

target = int(input("Enter target element: "))

prefix = 0
ans = 0

arr = [0]

for x in nums:
    if x == target:
        prefix += 1
    else:
        prefix -= 1

    ans += bisect_left(arr, prefix)
    insort(arr, prefix)

print("Number of valid subarrays:", ans)


# sample input
# Enter size of array: 4
# Enter array elements:
# 1 2 2 3
# Enter target element: 2

# sample output
# Number of valid subarrays: 5