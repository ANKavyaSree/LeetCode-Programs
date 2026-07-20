from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        elements = []
        for row in grid:
            elements.extend(row)

        total = m * n
        k %= total

        if k != 0:
            elements = elements[-k:] + elements[:-k]

        result = []
        for i in range(0, total, n):
            result.append(elements[i:i + n])

        return result
