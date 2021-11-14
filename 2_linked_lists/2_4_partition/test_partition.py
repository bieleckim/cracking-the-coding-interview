import unittest
from partition import Node, partition

class TestPartition(unittest.TestCase):

    def test_should_partition(self) -> None:
        node = Node(3)
        node.append(5)
        node.append(8)
        node.append(5)
        node.append(10)
        node.append(2)
        node.append(1)

        expected_node = Node(3)
        expected_node.append(2)
        expected_node.append(1)
        expected_node.append(5)
        expected_node.append(8)
        expected_node.append(5)
        expected_node.append(10)

        partitioned = partition(node, 5)

        self.assertTrue(partitioned.is_equal(expected_node))


if __name__ == '__main__':
    unittest.main()
