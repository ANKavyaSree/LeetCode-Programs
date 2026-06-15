class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next

    return head


def delete_middle(head):
    if not head or not head.next:
        return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next

    return head


def print_linked_list(head):
    result = []

    while head:
        result.append(str(head.val))
        head = head.next

    print("Modified Linked List:", " -> ".join(result))


# User Input
n = int(input("Enter number of nodes: "))

print("Enter node values:")
arr = list(map(int, input().split()))

head = create_linked_list(arr)

head = delete_middle(head)

if head:
    print_linked_list(head)
else:
    print("Linked List is empty")


# sample input
# Enter number of nodes: 7
# Enter node values:
# 1 3 4 7 1 2 6

# sample output
# Modified Linked List: 1 -> 3 -> 4 -> 1 -> 2 -> 6