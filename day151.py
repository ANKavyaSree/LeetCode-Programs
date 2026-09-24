# Day151 - 3550. Smallest Index With Digit Sum Equal to Index

def smallest_index(nums):
    for i, num in enumerate(nums):
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum == i:
            return i
    return -1


# User input
nums = list(map(int, input("Enter the array elements: ").split()))

print("Output:", smallest_index(nums))
