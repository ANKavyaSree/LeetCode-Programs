from bisect import bisect_right


class Solution:
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        total_ones = s.count("1")

        # Run-length encode s.
        starts = []
        ends = []
        types = []

        i = 0
        while i < n:
            j = i
            while j + 1 < n and s[j + 1] == s[i]:
                j += 1

            starts.append(i)
            ends.append(j)
            types.append(s[i])
            i = j + 1

        run_count = len(starts)

        # Value for every 1-run:
        # length of the zero-run before it + length of the zero-run after it.
        values = [0] * run_count

        for i in range(1, run_count - 1):
            if types[i] == "1":
                left_zero = ends[i - 1] - starts[i - 1] + 1
                right_zero = ends[i + 1] - starts[i + 1] + 1
                values[i] = left_zero + right_zero

        # Sparse table for range maximum query on values.
        logs = [0] * (run_count + 1)
        for i in range(2, run_count + 1):
            logs[i] = logs[i // 2] + 1

        sparse = [values[:]]
        level = 1

        while (1 << level) <= run_count:
            length = 1 << level
            half = length // 2
            previous = sparse[-1]
            current = []

            for i in range(run_count - length + 1):
                current.append(max(previous[i], previous[i + half]))

            sparse.append(current)
            level += 1

        def range_max(left, right):
            if left > right:
                return 0

            length = right - left + 1
            power = logs[length]

            return max(
                sparse[power][left],
                sparse[power][right - (1 << power) + 1]
            )

        def candidate_gain(l, r):
            left_run = bisect_right(starts, l) - 1
            right_run = bisect_right(starts, r) - 1

            # Find the first possible 1-run surrounded by zeroes.
            if types[left_run] == "0":
                first = left_run + 1
            else:
                first = left_run + 2

            # Find the last possible 1-run surrounded by zeroes.
            if types[right_run] == "0":
                last = right_run - 1
            else:
                last = right_run - 2

            if first > last or first >= run_count or last < 0:
                return 0

            best = 0

            # First candidate may have a truncated left zero block.
            left_zero = ends[first - 1] - starts[first - 1] + 1
            if first - 1 == left_run:
                left_zero = ends[left_run] - l + 1

            # Last candidate may have a truncated right zero block.
            right_zero = ends[last + 1] - starts[last + 1] + 1
            if last + 1 == right_run:
                right_zero = r - starts[right_run] + 1

            if first == last:
                return left_zero + right_zero

            best = max(best, left_zero + (
                ends[first + 1] - starts[first + 1] + 1
            ))

            best = max(best, (
                ends[last - 1] - starts[last - 1] + 1
            ) + right_zero)

            # Candidates strictly between first and last use complete zero-runs.
            best = max(best, range_max(first + 1, last - 1))

            return best

        answer = []

        for l, r in queries:
            answer.append(total_ones + candidate_gain(l, r))

        return answer


# User input version
s = input("Enter the binary string: ")
q = int(input("Enter number of queries: "))

queries = []
print("Enter each query as: l r")

for _ in range(q):
    l, r = map(int, input().split())
    queries.append([l, r])

solution = Solution()
answer = solution.maxActiveSectionsAfterTrade(s, queries)

print("Answer:", answer)
