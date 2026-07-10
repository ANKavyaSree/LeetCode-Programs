import bisect
import json
import sys

class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        # Step 1: Extract unique sorted values
        arr = sorted(list(set(nums)))
        m = len(arr)
        
        # Map element values to their corresponding index in the unique sorted list
        val_to_idx = {v: i for i, v in enumerate(arr)}
        
        # 18 levels cover up to 2^17 (131,072) nodes, sufficient for N <= 10^5
        LOG_N = 18
        
        # max_reach[p][i]: index in 'arr' reachable in 2^p steps moving right from index i
        # min_reach[p][i]: index in 'arr' reachable in 2^p steps moving left from index i
        max_reach = [[i for i in range(m)] for _ in range(LOG_N)]
        min_reach = [[i for i in range(m)] for _ in range(LOG_N)]
        
        # Step 2: Initialize base steps (2^0 = 1 step capability)
        for i in range(m):
            # Furthest index to the right within maxDiff
            r_val = arr[i] + maxDiff
            r_idx = bisect.bisect_right(arr, r_val) - 1
            max_reach[0][i] = r_idx
            
            # Furthest index to the left within maxDiff
            l_val = arr[i] - maxDiff
            l_idx = bisect.bisect_left(arr, l_val)
            min_reach[0][i] = l_idx
            
        # Step 3: Compute binary lifting tables
        for p in range(1, LOG_N):
            for i in range(m):
                max_reach[p][i] = max_reach[p-1][max_reach[p-1][i]]
                min_reach[p][i] = min_reach[p-1][min_reach[p-1][i]]
                
        # Step 4: Evaluate queries efficiently
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            vu, vv = nums[u], nums[v]
            if abs(vu - vv) <= maxDiff:
                ans.append(1)
                continue
                
            iu, iv = val_to_idx[vu], val_to_idx[vv]
            
            if iu < iv:
                # Target value is to the right
                if max_reach[LOG_N - 1][iu] < iv:
                    ans.append(-1)
                    continue
                
                steps = 0
                curr = iu
                for p in range(LOG_N - 1, -1, -1):
                    if max_reach[p][curr] < iv:
                        steps += (1 << p)
                        curr = max_reach[p][curr]
                ans.append(steps + 1)
                
            else:
                # Target value is to the left
                if min_reach[LOG_N - 1][iu] > iv:
                    ans.append(-1)
                    continue
                
                steps = 0
                curr = iu
                for p in range(LOG_N - 1, -1, -1):
                    if min_reach[p][curr] > iv:
                        steps += (1 << p)
                        curr = min_reach[p][curr]
                ans.append(steps + 1)
                
        return ans

# --- Interactive Local Driver Code ---
if __name__ == "__main__":
    print("--- LeetCode 3534 Test Sandbox ---")
    print("Provide inputs to run custom tests or press Enter directly to run built-in samples.\n")
    
    try:
        # Prompting for user inputs
        user_n = input("Enter n (or press Enter for samples): ").strip()
        if user_n:
            n = int(user_n)
            nums = json.loads(input("Enter nums array (e.g., [1,8,3,4,2]): "))
            maxDiff = int(input("Enter maxDiff integer: "))
            queries = json.loads(input("Enter queries array (e.g., [[0,3],[2,4]]): "))
            
            sol = Solution()
            output = sol.pathExistenceQueries(n, nums, maxDiff, queries)
            print(f"\n[Execution Result] Output: {output}")
            sys.exit(0)
    except Exception as e:
        print(f"Parsing failed ({e}). Proceeding to evaluate built-in samples standard outputs instead...\n")

    # Built-in Samples Execution
    sol = Solution()
    
    # Sample Test 1
    n1, nums1, maxDiff1, queries1 = 5, [1, 8, 3, 4, 2], 3, [[0, 3], [2, 4]]
    print("Sample 1 Input:")
    print(f"n = {n1}, nums = {nums1}, maxDiff = {maxDiff1}, queries = {queries1}")
    print(f"Expected Output: [1, 1]")
    print(f"Actual Output:   {sol.pathExistenceQueries(n1, nums1, maxDiff1, queries1)}\n")
    
    # Sample Test 2 (Your TLE Edge Case)
    n2, nums2, maxDiff2, queries2 = 3, [13, 17, 16], 8, [[1, 2]]
    print("Sample 2 Input (The TLE Edge-case Breakpoint):")
    print(f"n = {n2}, nums = {nums2}, maxDiff = {maxDiff2}, queries = {queries2}")
    print(f"Expected Output: [1]")
    print(f"Actual Output:   {sol.pathExistenceQueries(n2, nums2, maxDiff2, queries2)}\n")
    
    # Sample Test 3
    n3, nums3, maxDiff3, queries3 = 5, [5, 3, 1, 9, 10], 2, [[0, 1], [0, 2], [2, 3], [4, 3]]
    print("Sample 3 Input:")
    print(f"n = {n3}, nums = {nums3}, maxDiff = {maxDiff3}, queries = {queries3}")
    print(f"Expected Output: [1, 2, -1, 1]")
    print(f"Actual Output:   {sol.pathExistenceQueries(n3, nums3, maxDiff3, queries3)}\n")

# sample input
# Enter n (or press Enter for samples): 5
# Enter nums array (e.g., [1,8,3,4,2]): [1,8,3,4,2]
# Enter maxDiff integer: 3
# Enter queries array (e.g., [[0,3],[2,4]]): [[0,3],[2,4]] 

# sample output
# Output: [1, 1]