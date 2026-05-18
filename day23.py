from collections import defaultdict, deque

def minJumps(arr):
    n = len(arr)

    if n == 1:
        return 0

    # Store indices of same values
    graph = defaultdict(list)

    for i, value in enumerate(arr):
        graph[value].append(i)

    queue = deque([(0, 0)])  # (index, steps)
    visited = set([0])

    while queue:
        index, steps = queue.popleft()

        # Reached last index
        if index == n - 1:
            return steps

        # Adjacent indices
        neighbors = graph[arr[index]] + [index - 1, index + 1]

        for next_index in neighbors:
            if 0 <= next_index < n and next_index not in visited:
                visited.add(next_index)
                queue.append((next_index, steps + 1))

        # Clear processed value to avoid repeated traversal
        graph[arr[index]].clear()

    return -1


# User Input
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))

# Output
print("Minimum jumps required:", minJumps(arr))



# sample input
# Enter size of array: 10
# Enter array elements: 100 -23 -23 404 100 23 23 23 3 404

# sample output
# Minimum jumps required: 3