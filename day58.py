from collections import Counter

def max_number_of_balloons(text):
    freq = Counter(text)

    return min(
        freq['b'],
        freq['a'],
        freq['l'] // 2,
        freq['o'] // 2,
        freq['n']
    )

# User Input
text = input("Enter the text string: ")

result = max_number_of_balloons(text)

print("Maximum number of times 'balloon' can be formed:", result)


# sample input
# Enter the text string: loonbalxballpoon

# sample output
# Maximum number of times 'balloon' can be formed: 2