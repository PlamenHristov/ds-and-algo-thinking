import unittest
from MyTake.src.chapter2.backtracking import Backtracking


class TestBacktracking(unittest.TestCase):
    def test_appendAtBeginningFront(self):
        print(Backtracking.bitStrings(4))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
