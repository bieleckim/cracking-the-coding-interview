
from typing import Optional


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

class LinkedList:
    def __init__(self, head: Node):
        self.head = head
        self.tail = head.next

    def append(self, value: int):
        self.tail = Node(value)
        self.head.append(value)

def create_or_append(list: Optional[LinkedList], value: int) -> LinkedList:
    if list is None:
        list = LinkedList(Node(value))
    else:
        list.append(value)
    return list

def partition(node: Node, x: int) -> Node:
    left = None
    right = None
    current = node
    while current:
        if current.value < x:
            left = create_or_append(left, current.value)
        else:
            right = create_or_append(right, current.value)
        current = current.next
    
    left.tail.next = right.head
    return left.head
