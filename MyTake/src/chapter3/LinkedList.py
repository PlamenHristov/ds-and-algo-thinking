class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next is not None

    # __str__ returns string equivalent of Object
    def __str__(self):
        return "Node[Data = %s]" % (self.data,)


class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    # method to add a node in the linked list
    def insert(self, data):
        if self.length == 0:
            self.insertAtBeg(data)
        else:
            self.insertAtBeg(data)

    def insertAtBeg(self, item):
        newNode = Node(item)
        newNode.setNext(self.head)
        self.head = newNode
        self.length += 1

    def insertAtEnd(self, item):
        current = self.head

        while current.getNext() is not None:
            current = current.getNext()

        node = Node(item)
        current.setNext(node)

        self.length += 1

    def insertBeforeItem(self, inItem, item):
        current = self.head
        previous = None
        found = False
        stop = False

        while current and not found and not stop:
            if current.getData() == item:
                found = True
                stop = True
            else:
                previous = current
                current = current.getNext()

        node = Node(inItem)
        previous.setNext(node)
        node.setNext(current)

    def insertAfterItem(self, inItem, item):
        current = self.head

        found = False
        stop = False

        while current and not found and not stop:
            if current.getData() == item:
                found = True
                stop = True
            else:
                #                previous = current
                current = current.getNext()
        successor = current.getNext()
        node = Node(inItem)
        current.setNext(node)
        node.setNext(successor)

    # method to delete the first node of the linked list
    def deleteBeg(self):
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.next
            self.length -= 1

    # method to delete the last node of the linked list
    def deleteLast(self):
        if self.length == 0:
            print("The list is empty")
        else:
            currentnode = self.head
            previousnode = self.head
            while currentnode.next:
                previousnode = currentnode
                currentnode = currentnode.next

            previousnode = None
            self.length -= 1

    # method to delete a node after the node having the given data
    def deleteValue(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        return True

    # particular position
    def deleteAtPos(self, pos):
        raise NotImplementedError

    # returns the length of the list
    def getLength(self):
        return self.length

    # returns the first element of the list
    def getFirst(self):
        if self.length == 0:
            print("The list is empty")
        else:
            return self.head.data

    # returns the last element of the list
    def getLast(self):
        if self.length == 0:
            print("The list is empty")
        else:
            currentnode = self.head

            while currentnode is not None:
                currentnode = currentnode.next

            return currentnode.data

    # returns node at any position
    def getAtPos(self, pos):
        count = 0
        currentnode = self.head

        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    return currentnode.data
                else:
                    currentnode = currentnode.next

    def search(self, data):
        if self.length == 0:
            print("The list is empty")
            return None

        current = self.head

        while current:
            if current.data == data:
                return current.data
            current = current.next

        return None

    # method to print the whole list
    def printList(self):
        listData = []
        currentNode = self.head
        while currentNode:
            listData.append(currentNode.data)
            currentNode = currentNode.next
        print(listData)


class BSTNode:
    def __init__(root, data=None):
        root.left = None
        root.right = None
        root.data = data


def insertNode(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)


def deleteNode(root, data):
    """ delete the node with the given data and return the root node of the tree """
    if root.data == data:
        # found the node we need to delete
        if root.right and root.left:
            # get the successor node and its parent
            [psucc, succ] = findMin(root.right, root)
            # splice out the successor
            # (we need the parent to do this)
            if psucc.left == succ:
                psucc.left = succ.right
            else:
                psucc.right = succ.right
            # reset the left and right children of the successor
            succ.left = root.left
            succ.right = root.right
            return succ
        else:
            # "easier" case
            if root.left:
                return root.left  # promote the left subtree
            else:
                return root.right  # promote the right subtree
    else:
        if root.data > data:  # data should be in the left subtree
            if root.left:
                root.left = deleteNode(root.left, data)
                # else the data is not in the tree
        else:  # data should be in the right subtree
            if root.right:
                root.right = deleteNode(root.right, data)
    return root


def findMin(root, parent):
    """ return the minimum node in the current tree and its parent """
    # we use an ugly trick: the parent node is passed in as an argument
    # so that eventually when the leftmost child is reached, the
    # call can return both the parent to the successor and the successor
    if root.left:
        return findMin(root.left, root)
    else:
        return [parent, root]


def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print
    root.data
    inOrderTraversal(root.right)


def preOrderTraversal(root):
    if not root:
        return
    print
    root.data
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)


def main():
    l_list = LinkedList()
    l_list.insert("Jacob")
    l_list.insert("Cid")
    l_list.insert("Pallymay")
    l_list.insert("Rasmus")
    l_list.insert("Rasmus")
    l_list.deleteValue("Rasmus")
    l_list.deleteValue("Cid")
    l_list.printList()
    print(l_list.head.data)
    print(l_list.head)


if __name__ == '__main__':
    main()
