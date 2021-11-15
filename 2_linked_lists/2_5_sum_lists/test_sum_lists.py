import unittest
from sum_lists import Node, sum_lists

class TestSumLists(unittest.TestCase):

    def test_should_sum_lists(self) -> None:
        a = Node(7)
        a.append(1)
        a.append(6)

        b = Node(5)
        b.append(9)
        b.append(2)

        sum = Node(2)
        sum.append(1)
        sum.append(9)

        self.assertTrue(sum_lists(a, b).is_equal(sum))


if __name__ == '__main__':
    unittest.main()
