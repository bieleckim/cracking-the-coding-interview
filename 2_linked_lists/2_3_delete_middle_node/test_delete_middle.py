import unittest
from delete_middle import Node, delete_middle

class TestDeleteMiddle(unittest.TestCase):

    def test_should_delete_middle_node(self) -> None:
        node = Node('a')
        node.append('b')
        node.append('c')
        node.append('d')
        node.append('e')
        node.append('f')

        expected_node = Node('a')
        expected_node.append('b')
        expected_node.append('d')
        expected_node.append('e')
        expected_node.append('f')

        delete_middle(node)
        self.assertTrue(node.is_equal(expected_node))

    def test_should_not_delete(self) -> None:
        node = Node('a')
        node.append('b')

        expected_node = Node('a')
        expected_node.append('b')

        delete_middle(node)
        self.assertTrue(node.is_equal(expected_node))


if __name__ == '__main__':
    unittest.main()
