class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head

    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next

    return head


def pair_sum(head):
    values = []

    current = head
    while current:
        values.append(current.val)
        current = current.next

    left = 0
    right = len(values) - 1
    max_sum = 0

    while left < right:
        max_sum = max(max_sum, values[left] + values[right])
        left += 1
        right -= 1

    return max_sum


# User Input
n = int(input("Enter even number of nodes: "))

print("Enter node values:")
arr = list(map(int, input().split()))

head = create_linked_list(arr)

result = pair_sum(head)

print("Maximum Twin Sum:", result)


# sample input
# Enter even number of nodes: 4
# Enter node values:
# 5 4 2 1

# sample output
# Maximum Twin Sum: 6