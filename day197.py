import heapq


class FenwickTree:
    def __init__(self, n):
        self.n = n
        # Fenwick tree representing n initially available servers.
        self.tree = [0] + [i & -i for i in range(1, n + 1)]

    def add(self, index, value):
        while index <= self.n:
            self.tree[index] += value
            index += index & -index

    def prefix_sum(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def find_kth(self, k):
        # Find the 1-based index of the k-th available server.
        index = 0
        bit = 1 << (self.n.bit_length() - 1)

        while bit:
            next_index = index + bit
            if next_index <= self.n and self.tree[next_index] < k:
                index = next_index
                k -= self.tree[next_index]
            bit >>= 1

        return index + 1


def busiest_servers(k, arrival, load):
    available = FenwickTree(k)
    busy = []
    count = [0] * k
    available_count = k

    for i in range(len(arrival)):
        # Return servers whose previous tasks have finished.
        while busy and busy[0][0] <= arrival[i]:
            end_time, server = heapq.heappop(busy)
            available.add(server + 1, 1)
            available_count += 1

        if available_count == 0:
            continue

        start_server = i % k

        # Count available servers with indices below start_server.
        before = available.prefix_sum(start_server)

        # Select the first available server at or after start_server.
        # If there is none, wrap around to the first available server.
        if before < available_count:
            rank = before + 1
        else:
            rank = 1

        server = available.find_kth(rank) - 1

        available.add(server + 1, -1)
        available_count -= 1
        count[server] += 1

        heapq.heappush(busy, (arrival[i] + load[i], server))

    max_count = max(count)
    return [i for i in range(k) if count[i] == max_count]


if __name__ == "__main__":
    # Input:
    # k
    # arrival times (space-separated)
    # load times (space-separated)

    k = int(input())
    arrival = list(map(int, input().split()))
    load = list(map(int, input().split()))

    print(busiest_servers(k, arrival, load))
