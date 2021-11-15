
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def append(self, value: int):
        node = Node(value)
        current = self
        while current.next:
            current = current.next
        current.next = node

    def is_equal(self, node: 'Node') -> bool:
        current = self
        other_current = node
        while current and other_current:
            if current.value != other_current.value:
                return False
            current = current.next
            other_current = other_current.next
        return True

def sum_lists(a: Node, b: Node) -> Node:
    sum = None
    carry = 0
    while a or b:
        s = a.value if a else 0
        s += b.value if b else 0
        s += carry
        push = 0
        if s >= 10:
            push = s - 10
            carry = 1
        else:
            push = s
            carry = 0

        if sum:
            sum.append(push)
        else:
            sum = Node(push)

        if a:
            a = a.next
        if b:
            b = b.next
    return sum
