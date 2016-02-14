from MyTake.src.chapter3.LinkedList import LinkedList


class FromEndList(LinkedList):
    def nthNodeFromEndWithLength(self, n):
        movesFromHead = self.length - n - 1
        current = self.head

        if n < 0:
            return None
        if movesFromHead < 0:
            return None
        if movesFromHead == 0 and current:
            return current.getData()
        else:
            while current and movesFromHead:
                movesFromHead -= 1
                current = current.getNext()

        return current.getData()

    def nthNodeFromEnd(self, n):
        if 0 > n:
            return None

        temp = self.head
        count = 0
        while count < n and temp:
            temp = temp.next
            count += 1
        if count < n or temp is None:
            return None

        nth = self.head

        while temp.next:
            temp = temp.next
            nth = nth.next

        return nth


def main():
    l_list = FromEndList()
    l_list.insert("Jacob")
    l_list.insert("Cid")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    l_list.insert("Rasmus")
    l_list.printList()

    print(l_list.nthNodeFromEnd(0))


if __name__ == '__main__':
    main()
