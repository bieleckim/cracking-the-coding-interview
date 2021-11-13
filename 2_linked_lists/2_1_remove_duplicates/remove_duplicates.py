
from typing import Dict, List

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

def remove_duplicates(node: Node):
    values: Dict[int, bool] = {}
    prev = None
    current = node
    while current.next:
        if current.value in values:
            prev.next = current.next
        else:
            values[current.value] = True
        prev = current
        current = current.next
    return node
