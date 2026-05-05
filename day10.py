# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head

    # Step 1: Find length
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Make it circular
    tail.next = head

    # Step 3: Find new head
    k = k % length
    steps_to_new_head = length - k

    new_tail = head
    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.next

    new_head = new_tail.next

    # Step 4: Break the circle
    new_tail.next = None

    return new_head


# -------- User Input --------
values = list(map(int, input("Enter linked list values: ").split()))
k = int(input("Enter k: "))

# Create linked list
head = None
tail = None
for val in values:
    node = ListNode(val)
    if not head:
        head = node
        tail = node
    else:
        tail.next = node
        tail = node

# Rotate
result = rotateRight(head, k)

# Print result
print("Rotated List:")
while result:
    print(result.val, end=" -> " if result.next else "")
    result = result.next


# Sample input
# Enter linked list values: 1 2 3 4 5
# Enter k: 2

# sample output
# Rotated List:
# 4 -> 5 -> 1 -> 2 -> 3