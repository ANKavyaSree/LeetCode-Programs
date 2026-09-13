class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ans = 0

        for dr in range(-n + 1, n):
            for dc in range(-n + 1, n):
                overlap = 0

                for r in range(n):
                    for c in range(n):
                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < n and 0 <= nc < n:
                            if img1[r][c] == 1 and img2[nr][nc] == 1:
                                overlap += 1

                ans = max(ans, overlap)

        return ans


# User input
n = int(input("Enter matrix size n: "))

print("Enter img1 rows:")
img1 = []
for _ in range(n):
    img1.append(list(map(int, input().split())))

print("Enter img2 rows:")
img2 = []
for _ in range(n):
    img2.append(list(map(int, input().split())))

solution = Solution()
result = solution.largestOverlap(img1, img2)

print("Maximum overlap:", result)
