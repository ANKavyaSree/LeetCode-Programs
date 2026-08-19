class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        reserved = {}

        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()
            reserved[row].add(seat)

        answer = (n - len(reserved)) * 2

        for seats in reserved.values():
            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}

            if left.isdisjoint(seats) and right.isdisjoint(seats):
                answer += 2
            elif (left.isdisjoint(seats) or
                  middle.isdisjoint(seats) or
                  right.isdisjoint(seats)):
                answer += 1

        return answer


# User Input
n = int(input("Enter number of rows: "))
m = int(input("Enter number of reserved seats: "))

reservedSeats = []

print("Enter reserved seat pairs (row seat):")
for _ in range(m):
    row, seat = map(int, input().split())
    reservedSeats.append([row, seat])

solution = Solution()
result = solution.maxNumberOfFamilies(n, reservedSeats)

print("Maximum number of families:", result)
