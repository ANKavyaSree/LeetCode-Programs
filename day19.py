def isGood(nums):
    nums.sort()
    n = nums[-1]   # maximum element

    # Length must be n + 1
    if len(nums) != n + 1:
        return False

    # Check numbers 1 to n-1 appear once
    for i in range(1, n):
        if nums[i - 1] != i:
            return False

    # Last two elements must be n
    return nums[-1] == n and nums[-2] == n


# User Input
size = int(input("Enter size of array: "))
nums = list(map(int, input("Enter array elements: ").split()))

# Output
if isGood(nums):
    print("True - Array is Good")
else:
    print("False - Array is Not Good")



# sample input
# Enter size of array: 4
# Enter array elements: 1 3 3 2

# sample output
# True - Array is Good