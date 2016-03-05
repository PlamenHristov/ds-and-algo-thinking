from MyTake.src.chapter10.Common import *


def SelectionSort(A):
    for i in range(len(A)):
        current_smallest = i
        for k in range(i + 1, len(A)):
            if A[k] < A[current_smallest]:
                current_smallest = k
        swap(A, current_smallest, i)
