n = int(input("Enter number of elements: "))

print("Enter array elements:")
arr = list(map(int, input().split()))

arr.sort()

arr[0] = 1

for i in range(1, n):
    arr[i] = min(arr[i], arr[i - 1] + 1)

print("Maximum element after rearranging and decreasing:", arr[-1])


# sample input
# Enter number of elements: 5
# Enter array elements:
# 2 2 1 2 1

# sample output
# Maximum element after rearranging and decreasing: 2