from collections import deque

n = int(input("Enter the number of methods: "))
k = int(input("Enter the suspicious method: "))
m = int(input("Enter the number of invocations: "))

invocations = []
print("Enter each invocation (caller callee):")
for _ in range(m):
    u, v = map(int, input().split())
    invocations.append([u, v])

graph = [[] for _ in range(n)]
for u, v in invocations:
    graph[u].append(v)

suspicious = [False] * n
q = deque([k])
suspicious[k] = True

while q:
    u = q.popleft()
    for v in graph[u]:
        if not suspicious[v]:
            suspicious[v] = True
            q.append(v)

for u, v in invocations:
    if not suspicious[u] and suspicious[v]:
        print("Remaining methods:", list(range(n)))
        break
else:
    print("Remaining methods:", [i for i in range(n) if not suspicious[i]])
