def remove_covered_intervals(intervals):
    intervals.sort(key=lambda x: (x[0], -x[1]))

    count = 0
    max_end = 0

    for start, end in intervals:
        if end > max_end:
            count += 1
            max_end = end

    return count


n = int(input("Enter number of intervals: "))

intervals = []

print("Enter intervals (start end):")

for _ in range(n):
    l, r = map(int, input().split())
    intervals.append([l, r])

print("Remaining Intervals:", remove_covered_intervals(intervals))

# sample input
# Enter number of intervals: 3
# Enter intervals (start end):
# 1 4
# 3 6
# 2 8

# sample output
# Remaining Intervals: 2