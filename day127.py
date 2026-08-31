class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nodes_between_critical_points(head):
    prev = head
    curr = head.next
    index = 1

    first = -1
    last = -1
    min_dist = float("inf")

    while curr.next:
        next_node = curr.next

        if ((curr.val > prev.val and curr.val > next_node.val) or
            (curr.val < prev.val and curr.val < next_node.val)):

            if first == -1:
                first = index
            else:
                min_dist = min(min_dist, index - last)

            last = index

        prev = curr
        curr = next_node
        index += 1

    if first == -1 or first == last:
        return [-1, -1]

    return [min_dist, last - first]


# User input
values = list(map(int, input("Enter linked list values separated by spaces: ").split()))

head = ListNode(values[0])
current = head

for value in values[1:]:
    current.next = ListNode(value)
    current = current.next

print(nodes_between_critical_points(head))
