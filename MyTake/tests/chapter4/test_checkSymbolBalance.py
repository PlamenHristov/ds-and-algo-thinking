from unittest import TestCase
from MyTake.src.chapter4.checkSymbolBalance import checkSymbolBalance


class TestCheckSymbolBalance(TestCase):
    def test_checkSymbolBalance(self):
        not_balanced = '([)]'
        balanced = '{{([][])}()}'
        self.assertFalse(checkSymbolBalance(not_balanced))
        self.assertTrue(checkSymbolBalance(balanced))
