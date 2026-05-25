from collections import deque

def canReach(s, minJump, maxJump):
    n = len(s)
    queue = deque([0])
    farthest = 0
    visited = [False] * n
    visited[0] = True

    while queue:
        current = queue.popleft()

        start = max(current + minJump, farthest)
        end = min(current + maxJump + 1, n)

        for i in range(start, end):
            if s[i] == '0' and not visited[i]:
                if i == n - 1:
                    return True
                visited[i] = True
                queue.append(i)

        farthest = current + maxJump + 1

    return n == 1


# User Input
s = input("Enter binary string: ")
minJump = int(input("Enter minimum jump: "))
maxJump = int(input("Enter maximum jump: "))

result = canReach(s, minJump, maxJump)

print("Can reach last index:", result)



# sample input
# Enter binary string: 011010
# Enter minimum jump: 2
# Enter maximum jump: 3


# sample output
# Can reach last index: True