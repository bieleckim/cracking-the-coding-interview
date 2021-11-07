
import unittest
from urlify import urlify

class TestUrlify(unittest.TestCase):

    def test_urlify(self) -> None:
        self.assertEqual(urlify('aa a  ', 4), 'aa%20a')

if __name__ == '__main__':
    unittest.main()
