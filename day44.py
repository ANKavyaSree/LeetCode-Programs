def pivot_array(nums, pivot):
    less = []
    equal = []
    greater = []

    for num in nums:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)

    return less + equal + greater


# User Input
nums = list(map(int, input("Enter array elements: ").split()))
pivot = int(input("Enter pivot value: "))

result = pivot_array(nums, pivot)

print("Partitioned Array:", result)



# sample input
# Enter array elements: 9 12 5 10 14 3 10
# Enter pivot value: 10

# sample output
# Partitioned Array: [9, 5, 3, 10, 10, 12, 14]