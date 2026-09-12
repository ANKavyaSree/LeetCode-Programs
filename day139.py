from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Sort by right endpoint
        arr = sorted(
            (r, l, w, i)
            for i, (l, r, w) in enumerate(intervals)
        )

        ends = [x[0] for x in arr]

        # dp[k][i] = (maximum score, tuple of selected indices)
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(1, n + 1):
                # Option 1: don't take current interval
                best_score, best_indices = dp[k][i - 1]

                r, l, w, idx = arr[i - 1]

                # Previous interval must end strictly before l
                p = bisect_left(ends, l)

                prev_score, prev_indices = dp[k - 1][p]

                # Option 2: take current interval
                new_score = prev_score + w
                new_indices = tuple(sorted(prev_indices + (idx,)))

                if new_score > best_score:
                    best_score = new_score
                    best_indices = new_indices
                elif new_score == best_score and new_indices < best_indices:
                    best_indices = new_indices

                dp[k][i] = (best_score, best_indices)

        return list(dp[4][n][1])


# User input
n = int(input("Enter number of intervals: "))

intervals = []
print("Enter each interval as: left right weight")

for _ in range(n):
    l, r, w = map(int, input().split())
    intervals.append([l, r, w])

solution = Solution()
result = solution.maximumWeight(intervals)

print("Selected indices:", result)
