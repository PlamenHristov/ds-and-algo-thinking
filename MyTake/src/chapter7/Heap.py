import heapq


class Heap(object):
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def parent(self, index):
        return index // 2

    def leftChild(self, index):
        maxIndex = self.size
        childIndex = 2 * index
        if index > maxIndex or childIndex > maxIndex:
            return maxIndex
        else:
            return childIndex

    def rightChild(self, index):
        maxIndex = self.size
        childIndex = (2 * index + 1)
        if index > self.size or childIndex > maxIndex:
            return maxIndex
        else:
            return childIndex

    def printHeap(self):
        print(str(self.heapList))


class MinHeap(Heap):
    def __int__(self):
        super(MinHeap, self).__int__()

    def getMinimum(self):
        if self.size == 0:
            return -1
        else:
            return self.heapList[1]

    def minChild(self, i):
        if self.heapList[self.leftChild(i)] < self.heapList[self.rightChild(i)]:
            return self.leftChild(i)
        else:
            return self.rightChild(i)

    def percolateDown(self, i):
        while (i * 2) <= self.size:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def percolateUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def deleteMin(self):
        minIndex = 1
        retval = self.heapList[minIndex]
        self.heapList[minIndex] = self.heapList[self.size]
        self.size -= 1
        self.heapList.pop()
        self.percolateDown(minIndex)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percolateDown(i)
            i = i - 1


class MaxHeap(Heap):
    def __int__(self):
        super(MaxHeap, self).__int__()

    def getMaximum(self):
        if self.size == 0:
            return -1
        else:
            return self.heapList[1]

    def maxChild(self, i):
        if self.heapList[self.leftChild(i)] > self.heapList[self.rightChild(i)]:
            return self.leftChild(i)
        else:
            return self.rightChild(i)

    def percolateDown(self, i):
        while (i * 2) <= self.size:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def percolateUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.size = self.size + 1
        self.percolateUp(self.size - 1)

    def deleteMax(self):
        maxIndex = 1
        retval = self.heapList[maxIndex]
        self.heapList[maxIndex] = self.heapList[self.size]
        self.size -= 1
        self.heapList.pop()
        self.percolateDown(maxIndex)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percolateDown(i)
            i = i - 1


def main():
    A = [11, 16, 14, 17, 13, 12, 15, 14, 20]
    min = [0, 11, 13, 12, 14, 16, 14, 15, 17, 20]
    max = [0, 20, 17, 15, 16, 13, 12, 14, 14, 11]
    minHeap = MinHeap()
    minHeap.buildHeap(A)
    minHeap.printHeap()

    maxHeap = MaxHeap()
    maxHeap.buildHeap(A)
    maxHeap.printHeap()


if __name__ == '__main__':
    main()
