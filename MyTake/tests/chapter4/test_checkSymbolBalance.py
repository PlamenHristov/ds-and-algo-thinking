import unittest
from MyTake.src.chapter4.checkSymbolBalance import checkSymbolBalance


class TestCheckSymbolBalance(unittest.TestCase):
    def test_checkSymbolBalance(self):
        not_balanced = '([)]'
        balanced = '{{([][])}()}'
        self.assertFalse(checkSymbolBalance(not_balanced))
        self.assertTrue(checkSymbolBalance(balanced))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
