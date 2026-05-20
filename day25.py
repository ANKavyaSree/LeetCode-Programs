def findThePrefixCommonArray(A, B):
    seen = set()
    common = 0
    result = []

    for i in range(len(A)):

        # If already seen in other array
        if A[i] in seen:
            common += 1
        else:
            seen.add(A[i])

        if B[i] in seen:
            common += 1
        else:
            seen.add(B[i])

        result.append(common)

    return result


# User Input
n = int(input("Enter size of arrays: "))

A = list(map(int, input("Enter elements of array A: ").split()))
B = list(map(int, input("Enter elements of array B: ").split()))

# Output
print("Prefix Common Array:", findThePrefixCommonArray(A, B))

# sample input
# Enter size of arrays: 4
# Enter elements of array A: 1 3 2 4
# Enter elements of array B: 3 1 2 4


# sample output
# Prefix Common Array: [0, 2, 3, 4]
