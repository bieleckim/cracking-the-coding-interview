
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

def delete_middle(node: Node):
    current = node
    previous_middle = None

    while current:
        current = current.next
        if current:
            current = current.next
            if current:
                previous_middle = previous_middle.next if previous_middle else node
    
    if previous_middle:
        previous_middle.next = previous_middle.next.next
