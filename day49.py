def weighted_word_mapping(words, weights):
    result = []

    for word in words:
        total_weight = 0

        for ch in word:
            total_weight += weights[ord(ch) - ord('a')]

        mod_value = total_weight % 26

        # Reverse alphabetical mapping:
        # 0 -> z, 1 -> y, ..., 25 -> a
        mapped_char = chr(ord('z') - mod_value)

        result.append(mapped_char)

    return "".join(result)


# User Input
n = int(input("Enter number of words: "))

words = []
print("Enter words:")
for _ in range(n):
    words.append(input().strip())

print("Enter 26 weights separated by spaces:")
weights = list(map(int, input().split()))

answer = weighted_word_mapping(words, weights)

print("Mapped String:", answer)


# sample input
# Enter number of words: 3
# Enter words:
# abcd
# def
# xyz
# Enter 26 weights separated by spaces:
# 5 3 12 14 1 2 3 2 10 6 6 9 7 8 7 10 8 9 6 9 9 8 3 7 7 2


# sample output
# Mapped String: rij