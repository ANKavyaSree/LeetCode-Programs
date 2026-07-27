n = int(input("Enter the number of elements: "))
nums = list(map(int, input("Enter the elements: ").split()))

first = second = 0

for num in nums:
    if num > first:
        second = first
        first = num
    elif num > second:
        second = num

result = (first - 1) * (second - 1)

print("Maximum product:", result)
