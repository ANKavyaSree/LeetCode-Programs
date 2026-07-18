from math import gcd

n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter the elements: ").split()))

if len(nums) != n:
    print("Error: Number of elements does not match n.")
else:
    smallest = min(nums)
    largest = max(nums)

    result = gcd(smallest, largest)

    print("Greatest Common Divisor:", result)
