# day162.py
# LeetCode 856 - Score of Parentheses

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                value = stack.pop()

                if value == 0:
                    value = 1
                else:
                    value *= 2

                stack[-1] += value

        return stack[0]


# User input
s = input("Enter the balanced parentheses string: ")

solution = Solution()
result = solution.scoreOfParentheses(s)

print("Output:", result)
