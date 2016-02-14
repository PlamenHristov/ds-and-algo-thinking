class Node:
    # Constructor to initialize data
    # If data is not given by user,its taken as None
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

        # method for setting the data field of the node

    def setData(self, data):
        self.data = data

    # method for getting the data field of the node
    def getData(self):
        return self.data

    # method for setting the next field of the node
    def setNext(self, next):
        self.next = next

    # method for getting the next field of the node
    def getNext(self):
        return self.next

    # returns true if the node points to another node
    def hasNext(self):
        return self.next is not None

    # method for setting the next field of the node
    def setPrev(self, prev):
        self.prev = prev

    # method for getting the next field of the node
    def getPrev(self):
        return self.prev

    # returns true if the node points to another node
    def hasPrev(self):
        return self.prev is not None

    # __str__ returns string equivalent of Object
    def __str__(self):
        return "Node[Data = %s]" % (self.data,)


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = Node(data, None, current)
            self.tail = current.next

    def delete(self, data):
        current = self.head
        if current.data == data:
            self.head = current.next
            self.head.prev = None
            return True

        if current is None:
            return False

        if self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            return True

        while current:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                return True
            current = current.next

        return False

    def insertAtBeginning(self, data):
        newNode = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.setNext(self.head)
            newNode.setPrev(None)
            self.head.setPrev(newNode)
            self.head = newNode

    def getNode(self, index):
        current = self.head
        count = 0
        if index < 0:
            return None

        if current is None:
            return None

        while count < index and current:
            count += 1
            current = current.getNext()

        return current

    def insertAtGivenPosition(self, index, data):
        newNode = Node(data)
        if self.head == None or index == 0:
            self.insertAtBeginning(data)
        elif index > 0:
            temp = self.getNode(index)
            if temp == None or temp.getNext() == None:
                self.insert(data)
            else:
                newNode.setNext(temp.getNext())
                newNode.setPrev(temp)
                temp.getNext().setPrev(newNode)
                temp.setNext(newNode)

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True

            current = current.next
        return False

    def fwdPrint(self):
        current = self.head
        dataList = []
        if current is None:
            print("The list is empty")
            return False
        else:
            while current:
                dataList.append(current.data)
                current = current.next

        print(dataList)
        return True

    def revPrint(self):
        current = self.tail
        dataList = []
        if current is None:
            print("The list is empty")
            return False
        else:
            while current:
                dataList.append(current.data)
                current = current.prev

        print(dataList)
        return True


if __name__ == '__main__':
    # Initializing list
    l = DoubleLinkedList()

    # Inserting Values
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(4)

    print("The head of the list " + str(l.head.data))
    print("The head of the list " + str(l.tail.data))

    # Forward Print
    l.fwdPrint()

    # Reverse Print
    l.revPrint()

    # Try to find 3 in the list
    if (l.find(3)):
        print("Found")
    else:
        print("Not found")

    # Delete 3 from the list
    l.delete(3)

    # Forward Print
    l.fwdPrint()

    # Reverse Print
    l.revPrint()

    # Now if we find 3, we will not get it in the list
    if (l.find(3)):
        print("Found")
    else:
        print("Not found")
