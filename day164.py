# Day 164 - LeetCode 301: Remove Invalid Parentheses

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string):
            balance = 0
            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        level = {s}

        while True:
            valid = []
            for string in level:
                if is_valid(string):
                    valid.append(string)

            if valid:
                return valid

            next_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] in '()':
                        next_level.add(string[:i] + string[i + 1:])
            level = next_level


# User Input
s = input("Enter the string: ")

solution = Solution()
result = solution.removeInvalidParentheses(s)

print("Valid strings after minimum removals:")
for string in result:
    print(string)
