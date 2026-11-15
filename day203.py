MOD = 10**9 + 7

def count_odd_sum_subarrays(arr):
    even = 1
    odd = 0
    prefix = 0
    ans = 0

    for num in arr:
        prefix += num

        if prefix % 2 == 0:
            ans += odd
            even += 1
        else:
            ans += even
            odd += 1

    return ans % MOD


# User input
n = int(input())
arr = list(map(int, input().split()))

print(count_odd_sum_subarrays(arr))
