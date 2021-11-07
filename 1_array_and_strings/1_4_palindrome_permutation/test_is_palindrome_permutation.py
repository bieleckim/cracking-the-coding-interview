
import unittest
from is_palindrome_permutation import is_palindrome_permutation

class TestIsPalindromePermutation(unittest.TestCase):

    def test_should_be_palindrome_permutation(self) -> None:
        self.assertTrue(is_palindrome_permutation('a bcab'))

    def test_should_not_be_palindrome_permutation(self) -> None:
        self.assertFalse(is_palindrome_permutation('ttta aab'))


if __name__ == '__main__':
    unittest.main()
