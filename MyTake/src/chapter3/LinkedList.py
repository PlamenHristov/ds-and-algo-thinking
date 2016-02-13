class Node(object):
    def __init__(self):
        self.data = None
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
        return self.next != None


class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    # method to add a node in the linked list
    def addNode(self, node):
        pass

        # method to add a node at the beginning of the list with a data

    def addBeg(self, node):
        pass

    # method to add a node after the node having the data=data. The data of the new node is value2
    def addAfterValue(self, data, node):
        pass

    # method to add a node at a particular position
    def addAtPos(self, pos, node):
        pass

    # method to add a node at the end of a list
    def addLast(self, node):
        pass

    # method to delete the first node of the linked list
    def deleteBeg(self):
        pass

    # method to delete the last node of the linked list
    def deleteLast(self):
        pass

    # method to delete a node after the node having the given data
    def deleteValue(self, data):
        pass

    # method to delete a node at a particular position
    def deleteAtPos(self, pos):
        pass

    # returns the length of the list
    def getLength(self):
        pass

    # returns the first element of the list
    def getFirst(self):
        pass

    # returns the last element of the list
    def getLast(self):
        pass

    # returns node at any position
    def getAtPos(self, pos):
        pass

    # method to print the whole list
    def printList(self):
        pass


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


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
ll = LinkedList()
ll.addNode(node1)
ll.addNode(node2)
ll.addNode(node3)
ll.addNode(node4)
ll.addNode(node5)
ll.print_list()
