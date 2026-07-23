n = int(input("Enter the number of elements: "))

nums = list(map(int, input("Enter the permutation elements: ").split()))

xor_values = set()

for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            value = nums[i] ^ nums[j] ^ nums[k]
            xor_values.add(value)

print("Number of unique XOR triplet values:", len(xor_values))
