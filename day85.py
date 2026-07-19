def smallest_subsequence(s):
    last = {}

    # Last occurrence of each character
    for i, ch in enumerate(s):
        last[ch] = i

    stack = []
    visited = set()

    for i, ch in enumerate(s):
        if ch in visited:
            continue

        while stack and ch < stack[-1] and last[stack[-1]] > i:
            visited.remove(stack.pop())

        stack.append(ch)
        visited.add(ch)

    return "".join(stack)


# User Input
s = input("Enter the string: ")

print("Smallest subsequence:", smallest_subsequence(s))


# sample input
# Enter the string: bcabc

# sample output
# Smallest subsequence: abc