def maxDepthAfterSplit(seq):
    ans = []
    depth = 0

    for ch in seq:
        if ch == '(':
            depth += 1
            ans.append(depth % 2)
        else:
            ans.append(depth % 2)
            depth -= 1

    return ans


# User input
seq = input("Enter parentheses string: ").strip()

result = maxDepthAfterSplit(seq)
print(result)
