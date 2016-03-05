from MyTake.src.chapter10.Common import *


def BubbleSort(A):
    for i in range(len(A)):
        for k in range(len(A) - 1, i, -1):
            if A[k] < A[k - 1]:
                swap(A, k, k - 1)

def BubbleSortImproved(A):
    for i in range(len(A)):
        sorted = True
        for k in range(len(A) - 1, i, -1):
            if A[k] < A[k - 1]:
                sorted = False
                swap(A, k, k - 1)
        if sorted:
            return




if __name__ == '__main__':
    sorted_a = [127, 220, 246, 277, 321, 454, 534, 565, 933]
    unsorted_a = [534, 246, 933, 127, 277, 321, 454, 565, 220]
    with Timer() as fast:
        for _ in range(100000):
            BubbleSortImproved(sorted_a)

    with Timer() as slow:
        for _ in range(100000):
            BubbleSortImproved(unsorted_a)
    print(sorted_a)
    print(unsorted_a)
    print(fast.interval)
    print(slow.interval)
