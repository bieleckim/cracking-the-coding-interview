
import unittest
from is_one_away import is_one_away

class TestIsOneAway(unittest.TestCase):

    def test_should_be_one_away_added(self) -> None:
        self.assertTrue(is_one_away('abc', 'abdc'))
        self.assertTrue(is_one_away('abc', 'abcd'))
    
    def test_should_be_one_away_removed(self) -> None:
        self.assertTrue(is_one_away('abc', 'ab'))
        self.assertTrue(is_one_away('abc', 'ac'))
    
    def test_should_be_one_away_replaced(self) -> None:
        self.assertTrue(is_one_away('abc', 'abe'))
        self.assertTrue(is_one_away('abc', 'ebc'))

    def test_should_not_be_one_away(self) -> None:
        self.assertFalse(is_one_away('abc', 'abcde'))
        self.assertFalse(is_one_away('abc', 'bcd'))


if __name__ == '__main__':
    unittest.main()
