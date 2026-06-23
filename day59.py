MOD = 10**9 + 7

n = int(input("Enter n: "))
l = int(input("Enter l: "))
r = int(input("Enter r: "))

m = r - l + 1

if n == 1:
    print("Number of ZigZag Arrays:", m % MOD)
else:
    up = [0] * m
    down = [0] * m

    for i in range(m):
        up[i] = i
        down[i] = m - 1 - i

    if n == 2:
        ans = (sum(up) + sum(down)) % MOD
        print("Number of ZigZag Arrays:", ans)
    else:
        for _ in range(3, n + 1):
            pref_down = [0] * (m + 1)
            pref_up = [0] * (m + 1)

            for i in range(m):
                pref_down[i + 1] = (pref_down[i] + down[i]) % MOD
                pref_up[i + 1] = (pref_up[i] + up[i]) % MOD

            total_up = pref_up[m]

            new_up = [0] * m
            new_down = [0] * m

            for i in range(m):
                new_up[i] = pref_down[i]
                new_down[i] = (total_up - pref_up[i + 1]) % MOD

            up, down = new_up, new_down

        ans = (sum(up) + sum(down)) % MOD
        print("Number of ZigZag Arrays:", ans)

# sample input
# Enter n: 3
# Enter l: 1
# Enter r: 3

# sample output
# Number of ZigZag Arrays: 10