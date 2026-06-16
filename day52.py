def process_string(s):
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

    return ''.join(result)


# User Input
s = input("Enter the string: ")

answer = process_string(s)

print("Final Result:", answer)


# sample input
# Enter the string: a#b%*

# sample output
# Final Result: ba