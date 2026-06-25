n = int(input("Enter size of array: "))

print("Enter array elements:")
nums = list(map(int, input().split()))

target = int(input("Enter target element: "))

ans = 0

for i in range(n):
    cnt_target = 0

    for j in range(i, n):
        if nums[j] == target:
            cnt_target += 1

        length = j - i + 1

        if cnt_target > length // 2:
            ans += 1

print("Number of valid subarrays:", ans)


# sample input
# Enter size of array: 4
# Enter array elements:
# 1 2 2 3
# Enter target element: 2

# sample output
# Number of valid subarrays: 5