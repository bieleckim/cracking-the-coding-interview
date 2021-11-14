
import unittest
from remove_duplicates import Node, remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_should_remove_duplicates(self) -> None:
        node = Node(5)
        node.append(1)
        node.append(1)
        node.append(2)

        expected_node = Node(5)
        expected_node.append(1)
        expected_node.append(2)

        remove_duplicates(node)
        self.assertTrue(node.is_equal(expected_node))


if __name__ == '__main__':
    unittest.main()
