class Recursion(object):
    @staticmethod
    def TowersOfHanoi(numberOfDisks, startPeg=1, endPeg=3):
        if numberOfDisks:
            Recursion.TowersOfHanoi(numberOfDisks - 1, startPeg, 6 - startPeg - endPeg)
            print("Move disk {numberOfDisks} from peg {startPeg} to peg {endPeg}".format(numberOfDisks=numberOfDisks,
                                                                                         startPeg=startPeg,
                                                                                         endPeg=endPeg))
            Recursion.TowersOfHanoi(numberOfDisks - 1, 6 - startPeg - endPeg, endPeg)

    @staticmethod
    def isArraySorted(A):
        # Base Case
        if len(A) == 1:
            return True
        return A[0] <= A[1] and Recursion.isArraySorted(A[1:])


def main():
    Recursion.TowersOfHanoi(numberOfDisks=4)


if __name__ == '__main__':
    main()
