from functools import cache
from itertools import accumulate


class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(left, right):
            if left >= right:
                return 0

            best = 0
            left_sum = 0
            right_sum = prefix[right + 1] - prefix[left]

            for mid in range(left, right):
                left_sum += stoneValue[mid]
                right_sum -= stoneValue[mid]

                if left_sum < right_sum:
                    if best >= 2 * left_sum:
                        continue

                    best = max(
                        best,
                        left_sum + dfs(left, mid)
                    )

                elif left_sum > right_sum:
                    if best >= 2 * right_sum:
                        break

                    best = max(
                        best,
                        right_sum + dfs(mid + 1, right)
                    )

                else:
                    best = max(
                        best,
                        left_sum + dfs(left, mid),
                        right_sum + dfs(mid + 1, right)
                    )

            return best

        return dfs(0, len(stoneValue) - 1)


# User Input
stoneValue = list(map(
    int,
    input("Enter stone values separated by spaces: ").split()
))

solution = Solution()
result = solution.stoneGameV(stoneValue)

print("Maximum score:", result)
