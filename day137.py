from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root):
        self.count = 0

        def dfs(node):
            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            if node.val == total_sum // total_count:
                self.count += 1

            return total_sum, total_count

        dfs(root)
        return self.count

def build_tree(values):
    if not values or values[0].lower() == "null":
        return None

    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i].lower() != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i].lower() != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1

    return root

# User input
data = input("Enter tree values (space-separated, use null for missing nodes): ")
root = build_tree(data.split())

solution = Solution()
print("Number of nodes equal to the average of their subtree:",
      solution.averageOfSubtree(root))
