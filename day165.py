# Day 165 - LeetCode 1021: Remove Outermost Parentheses

def remove_outer_parentheses(s):
    result = []
    depth = 0

    for ch in s:
        if ch == '(':
            if depth > 0:
                result.append(ch)
            depth += 1
        else:
            depth -= 1
            if depth > 0:
                result.append(ch)

    return ''.join(result)


# User input
s = input("Enter a valid parentheses string: ")

print("Result:", remove_outer_parentheses(s))
