class Solution(object):
    def minInsertions(self, s):
        insertions = 0
        need = 0

        for ch in s:
            if ch == '(':
                if need % 2 == 1:
                    insertions += 1
                    need -= 1
                need += 2
            else:
                need -= 1

                if need < 0:
                    insertions += 1
                    need = 1

        return insertions + need


if __name__ == "__main__":
    s = input().strip()
    solution = Solution()
    print(solution.minInsertions(s))
