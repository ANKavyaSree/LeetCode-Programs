MOD = 10**9 + 7

n = int(input("Enter n: "))
l = int(input("Enter l: "))
r = int(input("Enter r: "))

m = r - l + 1

if m == 1:
    print("Number of ZigZag Arrays:", 0)
else:

    up_down = m * (m - 1) // 2
    down_up = up_down

    T = [
        [0, up_down],
        [down_up, 0]
    ]

    def mat_mul(A, B):
        size = len(A)
        res = [[0] * size for _ in range(size)]

        for i in range(size):
            for k in range(size):
                if A[i][k]:
                    for j in range(size):
                        res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
        return res

    def mat_pow(mat, power):
        size = len(mat)
        res = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

        while power:
            if power & 1:
                res = mat_mul(res, mat)
            mat = mat_mul(mat, mat)
            power >>= 1

        return res

    if n == 2:
        ans = (m * (m - 1)) % MOD
    else:
        base = [[up_down], [down_up]]

        M = mat_pow(T, n - 2)

        ans = 0
        for i in range(2):
            for j in range(2):
                ans = (ans + M[i][j] * base[j][0]) % MOD

    print("Number of ZigZag Arrays:", ans)

# sample input
# Enter n: 3
# Enter l: 1
# Enter r: 3

# sample output
# Number of ZigZag Arrays: 10