from unittest import TestCase
from MyTake.src.chapter2.backtracking import Backtracking


class TestBacktracking(TestCase):
    def test_appendAtBeginningFront(self):
        print(Backtracking.bitStrings(4))
