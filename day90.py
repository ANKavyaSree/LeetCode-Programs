MAX_XOR = 2048

n = int(input("Enter the number of elements: "))
nums = list(map(int, input("Enter the elements: ").split()))

present = [False] * MAX_XOR

for num in nums:
    present[num] = True

pair_xor = [False] * MAX_XOR

for a in range(MAX_XOR):
    if present[a]:
        for b in range(MAX_XOR):
            if present[b]:
                pair_xor[a ^ b] = True

result = [False] * MAX_XOR

for x in range(MAX_XOR):
    if pair_xor[x]:
        for num in nums:
            result[x ^ num] = True

print("Number of unique XOR triplet values:", sum(result))
