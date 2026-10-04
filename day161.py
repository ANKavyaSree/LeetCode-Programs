# day161.py
# LeetCode 678 - Valid Parenthesis String

class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                low -= 1
                high -= 1
            else:  # '*'
                low -= 1
                high += 1

            if high < 0:
                return False

            low = max(low, 0)

        return low == 0


# User input
s = input("Enter the string: ")

solution = Solution()
result = solution.checkValidString(s)

print("Output:", result)
