def find_subtree_sizes(parent, s):
    n = len(parent)

    # Build the original tree.
    children = [[] for _ in range(n)]
    for node in range(1, n):
        children[parent[node]].append(node)

    # Find the nearest ancestor with the same character.
    nearest = [-1] * 26
    new_parent = parent[:]

    def dfs_update(node):
        char_index = ord(s[node]) - ord('a')
        previous = nearest[char_index]
        nearest[char_index] = node

        for child in children[node]:
            dfs_update(child)

        if previous != -1:
            new_parent[node] = previous

        nearest[char_index] = previous

    dfs_update(0)

    # Build the modified tree.
    new_children = [[] for _ in range(n)]
    for node in range(1, n):
        new_children[new_parent[node]].append(node)

    # Calculate subtree sizes in the modified tree.
    answer = [0] * n

    def dfs_size(node):
        size = 1
        for child in new_children[node]:
            size += dfs_size(child)
        answer[node] = size
        return size

    dfs_size(0)
    return answer


# Read input:
# First line: n
# Second line: n space-separated parent values
# Third line: string s
n = int(input().strip())
parent = list(map(int, input().split()))
s = input().strip()

result = find_subtree_sizes(parent, s)
print(*result)
