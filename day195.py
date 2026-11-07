import heapq

def assignTasks(servers, tasks):
    free = [(weight, i) for i, weight in enumerate(servers)]
    heapq.heapify(free)

    busy = []
    ans = []
    time = 0

    for i, task in enumerate(tasks):
        time = max(time, i)

        # Move all servers that have finished their tasks to the free heap.
        while busy and busy[0][0] <= time:
            free_time, weight, index = heapq.heappop(busy)
            heapq.heappush(free, (weight, index))

        # If no server is free, jump to the earliest finishing time.
        if not free:
            time = busy[0][0]

            while busy and busy[0][0] <= time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(free, (weight, index))

        weight, index = heapq.heappop(free)
        ans.append(index)

        heapq.heappush(busy, (time + task, weight, index))

    return ans


if __name__ == "__main__":
    servers = list(map(int, input("Enter server weights: ").split()))
    tasks = list(map(int, input("Enter task durations: ").split()))

    result = assignTasks(servers, tasks)
    print("Assigned servers:", *result)
