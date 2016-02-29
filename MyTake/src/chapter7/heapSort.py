def heapSort(A):
    # convert A to heap
    length = len(A) - 1
    leastParent = length // 2
    for i in range(leastParent, -1, -1):
        percolateDown(A, i, length)
        # flatten heap into sorted array
    for i in range(length, 0, -1):
        if A[0] > A[i]:
            swap(A, 0, i)
            percolateDown(A, 0, i - 1)

def percolateDown(A, first, last):
    largest = first*2 + 1
    while largest <= last:
        if (largest < last) and (A[largest] < A[largest + 1 ]):
            largest += 1

        if A[largest] > A[first]:
            swap(A, largest, first)
            first = largest
            largest = 2*first + 1
        else:
            return

def swap(A, x,y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(heapSort(A))
print(A)