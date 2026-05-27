def numberOfSpecialChars(word):
    first_upper = {}
    last_lower = {}

    # Store first occurrence of uppercase letters
    for i, ch in enumerate(word):
        if ch.isupper():
            lower_char = ch.lower()
            if lower_char not in first_upper:
                first_upper[lower_char] = i

    # Store last occurrence of lowercase letters
    for i, ch in enumerate(word):
        if ch.islower():
            last_lower[ch] = i

    count = 0

    # Check special characters
    for ch in last_lower:
        if ch in first_upper and last_lower[ch] < first_upper[ch]:
            count += 1

    return count


# User Input
word = input("Enter a word: ")

result = numberOfSpecialChars(word)

print("Number of special characters:", result)


# sample input
# Enter a word: aaAbcBC


# sample output
# Number of special characters: 3
