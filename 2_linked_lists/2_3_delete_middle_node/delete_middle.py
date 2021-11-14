
class Node:
    def __init__(self, value: str):
        self.value = value
        self.next = None

    def append(self, value: str):
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

def delete_middle(middle_node: Node):
    if middle_node and middle_node.next:
        middle_node.value = middle_node.next.value
        middle_node.next = middle_node.next.next

