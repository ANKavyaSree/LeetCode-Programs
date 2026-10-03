# Day 160 - Longest Valid Parentheses
# LeetCode 32
# User Input Program

def longest_valid_parentheses(s):
    stack = [-1]
    max_length = 0

    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()

            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length


s = input("Enter parentheses string: ")
answer = longest_valid_parentheses(s)

print("Length of the longest valid parentheses substring:", answer)
