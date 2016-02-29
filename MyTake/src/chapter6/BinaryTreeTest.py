class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insert(self, val):
        if (self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if (val < node.value):
            if (node.left != None):
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if (node.right != None):
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if (self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if (val == node.value):
            return node
        elif (val < node.value and node.left != None):
            self._find(val, node.left)
        elif (val > node.value and node.right != None):
            self._find(val, node.right)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if (self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if (node != None):
            self._printTree(node.left)
            print(str(node.value + ' '))
            self._printTree(node.right)

    def traverse(self):
        thislevel = [self.root]
        level = 0
        while thislevel:
            level += 1
            print("Level {}".format(level))
            thisLevelValues = [node.value for node in thislevel]
            print(thisLevelValues)
            nextlevel = list()
            i = 0
            for node in thislevel:

                if node.left:
                    print("From " + str(thisLevelValues[i]) + " going left -> " + str(node.left.value))
                    nextlevel.append(node.left)
                if node.right:
                    print("From " + str(thisLevelValues[i]) + " going right -> " + str(node.right.value))
                    nextlevel.append(node.right)
                i += 1
            thislevel = nextlevel


def main():
    root = Tree()
    root.insert(3)
    root.insert(10)
    root.insert(1)
    root.insert(6)
    root.insert(4)
    root.insert(7)
    root.insert(14)
    root.insert(13)
    root.insert(16)
    root.insert(20)
    root.insert(30)
    root.traverse()


if __name__ == '__main__':
    main()
