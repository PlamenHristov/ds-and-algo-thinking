import unittest
from MyTake.src.chapter10.MergeSort import *
from MyTake.src.chapter10.QuickSort import *
from MyTake.src.chapter10.Common import *


class TestSort(unittest.TestCase):
    def test_MergeSort(self):
        A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
        sorted_a = sorted(A)
        # print(A)
        mergeSort(A)
        self.assertEqual(A, sorted_a)

    def test_QuickSort(self):
        A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
        sorted_a = sorted(A)
        # print(A)
        mergeSort(A)
        self.assertEqual(A, sorted_a)
def main():
    unittest.main()


if __name__ == '__main__':
    main()