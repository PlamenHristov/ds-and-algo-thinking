class Backtracking(object):
    @staticmethod
    def appendAtBeginningFront(x, L):
        # print("Entered the bit string")
        # print(str(x) + " " + str(L))
        return [x + element for element in L]

    @staticmethod
    def bitStrings(n):
        if n == 0:
            # print("Entered the empty")
            return []
        if n == 1:
            # print("Entered one")
            return ["0", "1"]
        else:
            # print("Entered else")
            return (Backtracking.appendAtBeginningFront("0", Backtracking.bitStrings(n - 1))
                    + Backtracking.appendAtBeginningFront("1", Backtracking.bitStrings(n - 1)))

    @staticmethod
    def alternativeBitString(n):
        # if n == 0:
        #     return []
        if n <= 1:
            return ["0", "1"]
        else:
            return [digit + bitstring
                    for digit in Backtracking.alternativeBitString(1)
                    for bitstring in Backtracking.alternativeBitString(n - 1)]

    @staticmethod
    def rangeToList(k):
        result = []
        for i in range(0, k):
            result.append(str(i))
        return result

    @staticmethod
    def baseKStrings(n, k):
        if n == 0:
            return []
        if n == 1:
            return Backtracking.rangeToList(k)
        else:
            return [digit + bitstring
                    for digit in Backtracking.baseKStrings(1, k)
                    for bitstring in Backtracking.baseKStrings(n - 1, k)]

    @staticmethod
    def geteval(A, i, j, L, H):
        if (i < 0 or i >= L or j < 0 or j >= H):
            return 0
        else:
            return A[i][j]

    @staticmethod
    def findMaxBlock(A, r, c, L, H, size):
        global maxsize
        global cntarr

        if (r >= L or c >= H):
            return
        cntarr[r][c] = 1
        size += 1

        if (size > maxsize):
            maxsize = size

        # search in eight directions
        direction = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
        for i in range(7):
            newi = r + direction[i][0]
            newj = c + direction[i][1]
            val = Backtracking.geteval(A, newi, newj, L, H)
            if (val > 0 and (cntarr[newi][newj] == 0)):
                Backtracking.findMaxBlock(A, newi, newj, L, H, size)
        cntarr[r][c] = 0

    @staticmethod
    def getMaxOnes(A, rmax, colmax):
        global maxsize
        global size
        global cntarr
        for i in range(0, rmax):
            for j in range(0, colmax):
                if (A[i][j] == 1):
                    Backtracking.findMaxBlock(A, i, j, rmax, colmax, 0)
        return maxsize


def main():
    print(Backtracking.bitStrings(3))
    # print(Backtracking.alternativeBitString(3))
    # print(Backtracking.baseKStrings(2, 4))
    zarr = [
        [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 1, 1],
        [1, 0, 0, 1, 1],
        [0, 1, 0, 1, 1],
    ]
    rmax = 5
    colmax = 5
    maxsize = 0
    size = 0
    cntarr = rmax * [colmax * [0]]
    print("Number of maximum 1s are")
    print(Backtracking.getMaxOnes(zarr, rmax, colmax))


if __name__ == '__main__':
    main()
