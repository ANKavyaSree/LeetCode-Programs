# LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
# User input version

nums = list(map(int, input("Enter the array elements separated by spaces: ").split()))

total = nums[0]

for i in range(1, len(nums)):
    if nums[i] == nums[i - 1] + 1:
        total += nums[i]
    else:
        break

num_set = set(nums)

while total in num_set:
    total += 1

print("Smallest missing integer:", total)
