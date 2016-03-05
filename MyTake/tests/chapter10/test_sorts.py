import unittest
from MyTake.src.chapter10.BubbleSort import *
from MyTake.src.chapter10.SelectionSort import *
from MyTake.src.chapter10.Common import *


class TestSort(unittest.TestCase):
    def test_BubbleSort(self):
        A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
        sorted_a = sorted(A)
        print(A)
        BubbleSort(A)
        self.assertEqual(A, sorted_a)

    def test_BubbleSortImproved(self):
        sorted_a = [127, 220, 246, 277, 321, 454, 534, 565, 933]
        unsorted_a = [534, 246, 933, 127, 277, 321, 454, 565, 220]

        with Timer() as fast:
            for _ in range(1000):
                BubbleSortImproved(sorted_a)
        with Timer() as slow:
            for _ in range(1000):
                BubbleSortImproved(unsorted_a)

        self.assertTrue(fast.interval < slow.interval)
        self.assertEqual(sorted_a, unsorted_a)

    def test_SelectionSort(self):
        A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
        sorted_a = sorted(A)
        print(A)
        SelectionSort(A)
        self.assertEqual(A, sorted_a)

def main():
    unittest.main()


if __name__ == '__main__':
    main()
