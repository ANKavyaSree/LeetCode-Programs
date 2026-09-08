class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        return n - 999


# User input
n = int(input("Enter n: "))

solution = Solution()
result = solution.countCommas(n)

print("Total number of commas:", result)
