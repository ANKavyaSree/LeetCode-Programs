from math import gcd


class Solution:
    def findKthSmallest(self, coins, k):
        n = len(coins)

        # Remove redundant coins.
        coins.sort()
        useful = []

        for c in coins:
            if not any(c % x == 0 for x in useful):
                useful.append(c)

        coins = useful
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        # Count distinct amounts <= x
        # divisible by at least one coin.
        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                current_lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        current_lcm = lcm(current_lcm, coins[i])

                        if current_lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                ways = x // current_lcm

                if bits % 2 == 1:
                    total += ways
                else:
                    total -= ways

            return total

        # Binary search for the kth smallest amount.
        low = 1
        high = min(coins) * k

        while low < high:
            mid = (low + high) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low


# Example:
# coins = [5, 2]
# k = 7
# print(Solution().findKthSmallest(coins, k))
# Output: 12
