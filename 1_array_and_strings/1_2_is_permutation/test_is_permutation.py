
import unittest
from is_permutation import is_permutation

class TestIsPermutation(unittest.TestCase):

    def test_should_be_permutation(self) -> None:
        self.assertTrue(is_permutation('abba', 'abab'))

    def test_should_not_be_permutation(self) -> None:
        self.assertFalse(is_permutation('aaba', 'abab'))


if __name__ == '__main__':
    unittest.main()
