class Node:
    def __init__(self,val):
        self.__val=val
        self.__left=None
        self.__right=None

    def getVal(self):
        return self.__val

    def getLeft(self):
        return self.__left

    def getRight(self):
        return self.__right

    def setLeft(self,node):
        self.__left=node

    def setRight(self,node):
        self.__right=node


class BinaryTree:
    def __init__(self):
        self.__root=None

    def getRoot(self):
        return self.__root

    def setRoot(self, node):
        self.__root=node

    def printValues(self,node):
        if node==None:
            return
        self.printValues(node.getLeft())
        print(node.getVal())
        self.printValues(node.getRight())

if __name__=="__main__":
    node1=Node(12)
    node2=Node(5)
    node3=Node(17)
    node1.setLeft(node2)
    node1.setRight(node3)

    node4=Node(4)
    node5=Node(6)
    node2.setLeft(node4)
    node2.setRight(node5)

    node6=Node(3)
    node4.setLeft(node6)

    node7=Node(19)
    node3.setRight(node7)

    node8=Node(18)
    node9=Node(21)
    node7.setLeft(node8)
    node7.setRight(node9)

    binaryTree=BinaryTree()
    binaryTree.setRoot(node1)
    binaryTree.printValues(node1)