from collections import deque


def min_moves(classroom, energy):
    m = len(classroom)
    n = len(classroom[0])

    start_r = start_c = -1
    litter = {}

    for r in range(m):
        for c in range(n):
            if classroom[r][c] == 'S':
                start_r, start_c = r, c
            elif classroom[r][c] == 'L':
                litter[(r, c)] = len(litter)

    total_litter = len(litter)

    if total_litter == 0:
        return 0

    target_mask = (1 << total_litter) - 1

    queue = deque([(start_r, start_c, energy, 0)])
    visited = {(start_r, start_c, energy, 0)}

    moves = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        for _ in range(len(queue)):
            r, c, e, mask = queue.popleft()

            if mask == target_mask:
                return moves

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if classroom[nr][nc] == 'X':
                    continue
                if e == 0:
                    continue

                new_energy = e - 1
                new_mask = mask

                if (nr, nc) in litter:
                    new_mask |= 1 << litter[(nr, nc)]

                if classroom[nr][nc] == 'R':
                    new_energy = energy

                state = (nr, nc, new_energy, new_mask)

                if state not in visited:
                    visited.add(state)
                    queue.append(state)

        moves += 1

    return -1


# User input
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

classroom = []
print("Enter classroom rows:")
for _ in range(m):
    classroom.append(input().strip())

energy = int(input("Enter energy: "))

print(min_moves(classroom, energy))
