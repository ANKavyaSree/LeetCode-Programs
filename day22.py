from collections import deque

def canReach(arr, start):
    n = len(arr)
    visited = [False] * n

    queue = deque([start])

    while queue:
        index = queue.popleft()

        # If value becomes 0
        if arr[index] == 0:
            return True

        if visited[index]:
            continue

        visited[index] = True

        # Forward jump
        forward = index + arr[index]

        # Backward jump
        backward = index - arr[index]

        if forward < n and not visited[forward]:
            queue.append(forward)

        if backward >= 0 and not visited[backward]:
            queue.append(backward)

    return False


# User Input
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
start = int(input("Enter starting index: "))

# Output
if canReach(arr, start):
    print("True - Can reach an index with value 0")
else:
    print("False - Cannot reach an index with value 0")


# sample input
# Enter size of array: 7
# Enter array elements: 4 2 3 0 3 1 2
# Enter starting index: 5

# sample output
# True - Can reach an index with value 0