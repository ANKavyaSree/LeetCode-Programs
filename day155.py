# day155.py
# 1614. Maximum Nesting Depth of the Parentheses

s = input("Enter the parentheses expression: ")

depth = 0
max_depth = 0

for ch in s:
    if ch == '(':
        depth += 1
        max_depth = max(max_depth, depth)
    elif ch == ')':
        depth -= 1

print("Maximum nesting depth:", max_depth)
