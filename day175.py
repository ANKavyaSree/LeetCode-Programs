MOD = 10**9 + 7

def numOfWays(nums):
    n = len(nums)

    # Precompute binomial coefficients C(i, j).
    comb = [[0] * n for _ in range(n)]
    for i in range(n):
        comb[i][0] = 1
        comb[i][i] = 1
        for j in range(1, i):
            comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

    def count_ways(arr):
        if len(arr) <= 2:
            return 1

        root = arr[0]
        left = [x for x in arr[1:] if x < root]
        right = [x for x in arr[1:] if x > root]

        interleavings = comb[len(left) + len(right)][len(left)]
        return (
            interleavings
            * count_ways(left) % MOD
            * count_ways(right) % MOD
        )

    # Exclude the original ordering.
    return (count_ways(nums) - 1) % MOD


# Input example: [2,1,3]
raw = input("Enter nums (e.g. [2,1,3]): ").strip()
nums = list(map(int, raw.strip("[]").split(",")))
print(numOfWays(nums))
