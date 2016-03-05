import time

class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start

def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

