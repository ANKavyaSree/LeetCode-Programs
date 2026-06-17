def kth_character(s, k):
    result = []

    for ch in s:
        if ch.islower():
            result.append(ch)

        elif ch == '*':
            if result:
                result.pop()

        elif ch == '#':
            result.extend(result)

        elif ch == '%':
            result.reverse()

    if 0 <= k < len(result):
        return result[k]

    return '.'

# User Input
s = input("Enter the string: ")
k = int(input("Enter k: "))

print("Output:", kth_character(s, k))


# sample input
# Enter the string: a#b%*
# Enter k: 1

# sample output
# Output: a