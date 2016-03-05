import unittest
from MyTake.src.chapter5.linkedQueue import *


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.que = Queue()
        self.que.enQueue("first")
        self.que.enQueue("second")
        self.que.enQueue("third")
        self.que.enQueue("fourth")

    def test_queueFrontRear(self):
        self.assertEqual(self.que.queueRear(), "first")
        self.assertEqual(self.que.queueFront(), "fourth")
        self.que.enQueue("fifth")
        self.assertEqual(self.que.queueRear(), "first")
        self.assertEqual(self.que.queueFront(), "fifth")
        self.assertEqual(self.que.getSize(), 5)

    def test_deQueue(self):
        self.assertEqual(self.que.deQueue(), "first")
        self.assertEqual(self.que.deQueue(), "second")
        self.assertEqual(self.que.getSize(), 2)
        self.que.enQueue("fifith")
        self.assertEqual(self.que.deQueue(), "third")

    def test_deQueueException(self):
        for _ in range(4):
            self.que.deQueue()
        with self.assertRaises(IndexError):
            self.que.deQueue()

    def test_emptyQueue(self):
        emptyQueue = Queue()
        with self.assertRaises(IndexError):
            emptyQueue.queueFront()


def main():
    unittest.main()


if __name__ == '__main__':
    main()
