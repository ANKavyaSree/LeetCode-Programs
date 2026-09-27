# day154.py
# LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses

def reverse_parentheses(s):
    stack = []

    for ch in s:
        if ch == ')':
            temp = []

            while stack[-1] != '(':
                temp.append(stack.pop())

            stack.pop()  # Remove '('
            stack.extend(temp)
        else:
            stack.append(ch)

    return ''.join(stack)


# User Input
s = input("Enter the string: ")

# Output
print("Result:", reverse_parentheses(s))
