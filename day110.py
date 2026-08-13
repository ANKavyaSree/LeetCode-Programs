class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        arr = list(s)
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            prefix = a[2]
            suffix = b[3]
            maximum = max(a[4], b[4])

            if a[0] == b[0] and a[2] == a[5]:
                prefix = a[5] + b[2]

            if a[1] == b[1] and b[3] == b[5]:
                suffix = a[3] + b[5]

            if a[1] == b[0]:
                maximum = max(maximum, a[3] + b[2])

            return (a[0], b[1], prefix, suffix, maximum, a[5] + b[5])

        def build(node, left, right):
            if left == right:
                tree[node] = (arr[left], arr[left], 1, 1, 1, 1)
                return

            mid = (left + right) // 2
            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, left, right, index, char):
            if left == right:
                tree[node] = (char, char, 1, 1, 1, 1)
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, right, index, char)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        answer = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            answer.append(tree[1][4])

        return answer


# User input
s = input("Enter string: ")
queryCharacters = input("Enter query characters: ")
indices_input = input("Enter query indices: ").strip()

# Supports both [1,3,3] and 1 3 3
if indices_input.startswith("["):
    queryIndices = [int(x.strip()) for x in indices_input[1:-1].split(",") if x.strip()]
else:
    queryIndices = list(map(int, indices_input.split()))

solution = Solution()

result = solution.longestRepeating(
    s,
    queryCharacters,
    queryIndices
)

print("Output:", result)
