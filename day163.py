# Day 163 - LeetCode 921: Minimum Add to Make Parentheses Valid

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        additions = 0

        for ch in s:
            if ch == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    additions += 1

        return additions + balance


# User Input
s = input("Enter parentheses string: ")

solution = Solution()
result = solution.minAddToMakeValid(s)

print("Minimum additions required:", result)
