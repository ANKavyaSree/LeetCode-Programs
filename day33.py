# Day 33 - Longest Common Suffix Queries
# User Input Version

def longest_common_suffix(word1, word2):
    i = len(word1) - 1
    j = len(word2) - 1
    count = 0

    while i >= 0 and j >= 0 and word1[i] == word2[j]:
        count += 1
        i -= 1
        j -= 1

    return count


n = int(input("Enter number of words in wordsContainer: "))
wordsContainer = []

print("Enter words for wordsContainer:")
for _ in range(n):
    wordsContainer.append(input())

m = int(input("\nEnter number of words in wordsQuery: "))
wordsQuery = []

print("Enter words for wordsQuery:")
for _ in range(m):
    wordsQuery.append(input())

result = []

for query in wordsQuery:
    best_index = 0
    best_suffix = -1
    shortest_length = float('inf')

    for i in range(len(wordsContainer)):
        suffix_len = longest_common_suffix(wordsContainer[i], query)

        if suffix_len > best_suffix:
            best_suffix = suffix_len
            best_index = i
            shortest_length = len(wordsContainer[i])

        elif suffix_len == best_suffix:
            if len(wordsContainer[i]) < shortest_length:
                best_index = i
                shortest_length = len(wordsContainer[i])

    result.append(best_index)

print("\nResult:", result)



# sample input
# Enter number of words in wordsContainer: 3
# Enter words for wordsContainer:
# abcd
# bcd
# xbcd

# Enter number of words in wordsQuery: 3
# Enter words for wordsQuery:
# cd
# bcd
# xyz


# sample output
# Result: [1, 1, 1]
