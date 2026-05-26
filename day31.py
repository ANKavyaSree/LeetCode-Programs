def numberOfSpecialChars(word):
    lowercase = set()
    uppercase = set()

    for ch in word:
        if ch.islower():
            lowercase.add(ch)
        else:
            uppercase.add(ch.lower())

    count = 0

    for ch in lowercase:
        if ch in uppercase:
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