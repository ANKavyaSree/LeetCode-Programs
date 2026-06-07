class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def createBinaryTree(descriptions):
    nodes = {}
    children = set()

    for parent, child, isLeft in descriptions:

        if parent not in nodes:
            nodes[parent] = TreeNode(parent)

        if child not in nodes:
            nodes[child] = TreeNode(child)

        if isLeft == 1:
            nodes[parent].left = nodes[child]
        else:
            nodes[parent].right = nodes[child]

        children.add(child)

    root = None
    for value in nodes:
        if value not in children:
            root = nodes[value]
            break

    return root


def levelOrder(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result


# User Input
n = int(input("Enter number of descriptions: "))

descriptions = []

print("Enter parent child isLeft:")
for _ in range(n):
    parent, child, isLeft = map(int, input().split())
    descriptions.append([parent, child, isLeft])

root = createBinaryTree(descriptions)

print("Level Order Traversal:")
print(levelOrder(root))



# sample input
# Enter number of descriptions: 5

# Enter parent child isLeft:
# 20 15 1
# 20 17 0
# 50 20 1
# 50 80 0
# 80 19 1

# sample output
# Level Order Traversal:
# [50, 20, 80, 15, 17, 19]