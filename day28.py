def check(nums):
    count = 0
    n = len(nums)

    # Count places where order breaks
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1

    # Valid if at most one break exists
    return count <= 1


# User Input
n = int(input("Enter size of array: "))
nums = list(map(int, input("Enter array elements: ").split()))

# Output
if check(nums):
    print("True - Array is sorted and rotated")
else:
    print("False - Array is not sorted and rotated")



# sample input
# Enter size of array: 5
# Enter array elements: 3 4 5 1 2


# sample output
# True - Array is sorted and rotated