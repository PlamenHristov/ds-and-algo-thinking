from MyTake.src.chapter3.LinkedList import LinkedList
from collections import defaultdict


class CycleDetect(LinkedList):
    def induceCycle(self, end, start):
        current = self.head
        stop = False
        endnodeFound = False
        endnodePointer = None
        count = 0
        while current != None and not stop:
            count += 1
            if count == end:
                endnodeFound = True
                endnodePointer = current.getNext()

            else:
                if count == start:
                    stop = True
                else:
                    current = current.getNext()

        current.setNext(endnodePointer)

    def detectCycleHashTable(self):
        hashtable = defaultdict(bool)
        current = self.head
        while current:
            if hashtable[current]:
                print("Found a cycle at: " + str(current.data))
                return True
            hashtable[current] = True
            current = current.getNext()
        return False

    # def detectCycleBruteForce(self):
    # 	detective = self.head
    # 	current = self.head.next
    #
    # 	while current is not None:
    # 		if detective == current:
    # 			print("Cycle detected" + str(detective.data))
    # 			detective = current.getNext()
    # 		while current.hasNext():
    # 			if current == detective

    def detectCycle(self):
        fastPtr = self.head
        slowPtr = self.head

        while fastPtr and slowPtr:
            fastPtr = fastPtr.getNext()
            if fastPtr == slowPtr:
                return True
            if fastPtr is None:
                return
            fastPtr = fastPtr.getNext
            if fastPtr == slowPtr:
                return True

            slowPtr = slowPtr.getNext()

    def detectCycleStart(self):
        if None == self.head or None == self.head.next:
            return None

        slow = self.head.next
        fast = slow.next
        while slow != fast:
            slow = slow.next
            try:
                fast = fast.next.next
            except AttributeError:
                return None
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow.getData()  # beginning of loop


if __name__ == "__main__":
    linkedlst = CycleDetect()
    linkedlst.insertAtBeg(1)
    linkedlst.insertAtBeg(2)
    linkedlst.insertAtEnd(3)
    linkedlst.insertBeforeItem(4, 3)
    linkedlst.insertAfterItem(5, 1)
    linkedlst.insertAtEnd(6)
    linkedlst.insertAtEnd(8)
    linkedlst.insertAtEnd(7)
    print("Head Node" + str(linkedlst.head.data))

    linkedlst.printList()
    print("Detecting cycle with a Hash Table: " + str(linkedlst.detectCycleHashTable()))

    linkedlst.induceCycle(2, 8)
    print("Detecting cycle with a Hash Table: " )
    print(linkedlst.detectCycleHashTable())
    print(linkedlst.detectCycle())
    print(linkedlst.detectCycleStart())
