# Day 194 - Count Zero Request Servers

from collections import defaultdict


def countServers(n, logs, x, queries):
    logs.sort(key=lambda a: a[1])
    indexed_queries = sorted((q, i) for i, q in enumerate(queries))

    result = [0] * len(queries)
    server_count = defaultdict(int)
    left = right = active = 0

    for q, idx in indexed_queries:
        # Add requests received at or before query time.
        while right < len(logs) and logs[right][1] <= q:
            server = logs[right][0]
            if server_count[server] == 0:
                active += 1
            server_count[server] += 1
            right += 1

        # Remove requests before the inclusive window [q-x, q].
        while left < right and logs[left][1] < q - x:
            server = logs[left][0]
            server_count[server] -= 1
            if server_count[server] == 0:
                active -= 1
            left += 1

        result[idx] = n - active

    return result


# User input
n = int(input("Enter the number of servers: "))

logs_count = int(input("Enter the number of logs: "))
logs = []
print("Enter each log as: server_id time")
for _ in range(logs_count):
    server_id, time = map(int, input().split())
    logs.append([server_id, time])

x = int(input("Enter x: "))
queries = list(map(int, input("Enter query times separated by spaces: ").split()))

print("Output:", countServers(n, logs, x, queries))
