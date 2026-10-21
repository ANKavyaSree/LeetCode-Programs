# Day 178 - LeetCode 3863: Minimum Operations to Sort a String

class Solution:
    def minOperations(self, s: str) -> int:
        if all(s[i] <= s[i + 1] for i in range(len(s) - 1)):
            return 0

        if len(s) == 2:
            return -1

        min_p, max_p = min(s[1:-1]), max(s[1:-1])

        if s[0] <= s[-1] and (min_p >= s[0] or max_p <= s[-1]):
            return 1

        return 3 if s[-1] < min_p and s[0] > max_p else 2


if __name__ == "__main__":
    s = input("Enter a string: ").strip()
    solution = Solution()
    print("Minimum operations:", solution.minOperations(s))
