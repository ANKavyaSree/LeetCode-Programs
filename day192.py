# Day 192 - Minimum Operations to Make K Subarrays Equal
# User input program

import bisect


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def kth(self, k):
        idx = 0
        bit = 1 << (self.n.bit_length() - 1)
        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.tree[nxt] < k:
                idx = nxt
                k -= self.tree[nxt]
            bit >>= 1
        return idx + 1


def min_operations(nums, x, k):
    n = len(nums)
    vals = sorted(set(nums))
    m = len(vals)

    bit_count = Fenwick(m)
    bit_sum = Fenwick(m)

    def update(v, delta):
        idx = bisect.bisect_left(vals, v) + 1
        bit_count.add(idx, delta)
        bit_sum.add(idx, delta * v)

    total = sum(nums[:x])
    for i in range(x):
        update(nums[i], 1)

    costs = []
    for i in range(n - x + 1):
        mid_idx = bit_count.kth((x + 1) // 2)
        median = vals[mid_idx - 1]
        count_left = bit_count.query(mid_idx)
        sum_left = bit_sum.query(mid_idx)

        cost = (
            median * count_left - sum_left
            + (total - sum_left)
            - median * (x - count_left)
        )
        costs.append(cost)

        if i < n - x:
            update(nums[i], -1)
            update(nums[i + x], 1)
            total += nums[i + x] - nums[i]

    # DP for selecting k non-overlapping windows.
    INF = float("inf")
    prev = [0] * (n + 1)

    for j in range(1, k + 1):
        curr = [INF] * (n + 1)
        for i in range(1, n + 1):
            curr[i] = curr[i - 1]
            if i >= x:
                curr[i] = min(curr[i], prev[i - x] + costs[i - x])
        prev = curr

    return prev[n]


nums = list(map(int, input("Enter array elements separated by spaces: ").split()))
x = int(input("Enter subarray size x: "))
k = int(input("Enter number of subarrays k: "))

print(min_operations(nums, x, k))
