
import unittest
from compress import compress

class TestCompress(unittest.TestCase):

    def test_compress(self) -> None:
        self.assertEqual(compress('aaa'), 'a3')
        self.assertEqual(compress('aaabb'), 'a3b2')
        self.assertEqual(compress('aaabbZGGGG'), 'a3b2Z1G4')

    def test_should_not_compress(self) -> None:
        self.assertEqual(compress('a'), 'a')
        self.assertEqual(compress('abc'), 'abc')
        self.assertEqual(compress('aabccde'), 'aabccde')


if __name__ == '__main__':
    unittest.main()
