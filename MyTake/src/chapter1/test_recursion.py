import unittest
import recursion


class TestRecursion(unittest.TestCase):

    def test_TowersOfHanoi(self):
        recursion.Recursion.TowersOfHanoi(numberOfDisks=4)
        self.assertTrue(True)

    def test_isArraySorted(self):
        sorted = [1,2,3,6,7,8,10]
        not_sorted = [3,5,7,8,1,9,10]
        self.assertTrue(recursion.Recursion.isArraySorted(sorted))
        self.assertFalse(recursion.Recursion.isArraySorted(not_sorted))

if __name__ == '__main__':
    unittest.main()