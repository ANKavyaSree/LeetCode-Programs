from collections import deque, defaultdict
import math

# Function to check prime number
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


# Function to find minimum jumps
def min_jumps(nums):

    n = len(nums)

    # Map prime -> indices divisible by that prime
    prime_map = defaultdict(list)

    for i in range(n):

        for p in range(2, nums[i] + 1):

            if is_prime(p) and nums[i] % p == 0:
                prime_map[p].append(i)

    queue = deque([0])
    visited = [False] * n
    visited[0] = True

    jumps = 0

    while queue:

        for _ in range(len(queue)):

            index = queue.popleft()

            # Reached last index
            if index == n - 1:
                return jumps

            # Move left
            if index - 1 >= 0 and not visited[index - 1]:
                visited[index - 1] = True
                queue.append(index - 1)

            # Move right
            if index + 1 < n and not visited[index + 1]:
                visited[index + 1] = True
                queue.append(index + 1)

            # Prime teleportation
            if is_prime(nums[index]):

                prime = nums[index]

                if prime in prime_map:

                    for next_index in prime_map[prime]:

                        if not visited[next_index]:
                            visited[next_index] = True
                            queue.append(next_index)

                    # Remove to avoid repeated processing
                    del prime_map[prime]

        jumps += 1

    return -1


# User Input
n = int(input("Enter size of array: "))

nums = list(map(int, input("Enter array elements: ").split()))

result = min_jumps(nums)

print("Minimum jumps required:", result)


# Sample input
# Enter size of array: 4
# Enter array elements: 1 2 4 6

# sample output:
# Minimum jumps required: 2