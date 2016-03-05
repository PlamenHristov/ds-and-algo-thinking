class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def InsertionSort(A):
    for i in range(1, len(A)):
        tmp = A[i]
        k = i
        while k > 0 and tmp < A[k - 1]:
            A[k] = A[k - 1]
            k -= 1
        A[k] = tmp

if __name__ == '__main__':
    A = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    InsertionSort(A)
    print(A)
