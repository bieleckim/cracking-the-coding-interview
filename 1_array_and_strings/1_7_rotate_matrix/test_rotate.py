
import unittest
from rotate import rotate

class TestRotate(unittest.TestCase):

    def test_should_rotate(self) -> None:
        image = [
            [0, 1, 1],
            [2, 3, 3],
            [4, 4, 1],
        ]

        rotated = [
            [4, 2, 0],
            [4, 3, 1],
            [1, 3, 1]
        ]

        self.assertEqual(rotate(image), rotated)


if __name__ == '__main__':
    unittest.main()
