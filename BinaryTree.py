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

    def insert(self,node):
        if self.__root==None:
            self.__root=node
        else:
            self.__insert(node,self.__root)

    def __insert(self,node,c_node):
        if node.getVal()<c_node.getVal():
            if c_node.getLeft()==None:
                c_node.setLeft(node)
                return
            else:
                self.__insert(node,c_node.getLeft())
        elif node.getVal()>c_node.getVal():
            if c_node.getRight() == None:
                c_node.setRight(node)
                return
            else:
                self.__insert(node, c_node.getRight())
        else:
            return

    def isRoot(self, node):
        return self.__root == node

    def printValues(self,node):
        if node==None:
            return
        self.printValues(node.getLeft())
        print(node.getVal())
        self.printValues(node.getRight())

if __name__=="__main__":
    values=[12,5,4,3,6,17,19,18,21]
    nodes=[]
    for value in values:
        nodes.append(Node(value))

    binaryTree=BinaryTree()

    for node in nodes:
        binaryTree.insert(node)

    binaryTree.printValues(nodes[0])