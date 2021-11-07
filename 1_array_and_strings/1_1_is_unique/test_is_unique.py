import unittest
from is_unique import is_unique

class TestIsUnique(unittest.TestCase):

    def test_should_be_unique(self) -> None:
        self.assertTrue(is_unique('abcdef'))

    def test_should_not_be_unique(self) -> None:
        self.assertFalse(is_unique('abccdef'))


if __name__ == '__main__':
    unittest.main()
