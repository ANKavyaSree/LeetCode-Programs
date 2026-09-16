def number_of_sets(n, k):
    MOD = 10**9 + 7

    # The answer is C(n + k - 1, 2k).
    # Compute the combination without using factorials.
    r = 2 * k
    total = n + k - 1

    r = min(r, total - r)

    result = 1
    for i in range(1, r + 1):
        result = result * (total - r + i) % MOD
        result = result * pow(i, MOD - 2, MOD) % MOD

    return result


# User input
n = int(input("Enter n: "))
k = int(input("Enter k: "))

print(number_of_sets(n, k))
