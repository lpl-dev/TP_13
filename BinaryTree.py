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

    def size(self,node):
        if node==None:
            return 0
        return 1+self.size(node.getLeft())+self.size(node.getRight())

    def printValues(self,node):
        if node==None:
            return
        self.printValues(node.getLeft())
        print(node.getVal())
        self.printValues(node.getRight())

    def sumValues(self,node):
        if node==None:
            return 0
        return node.getVal()+self.sumValues(node.getLeft())+self.sumValues(node.getRight())

    def numberLeaves(self, node):
        if node==None:
            return 0
        elif node.getLeft()==None and node.getRight()==None:
            return 1
        return self.numberLeaves(node.getLeft())+self.numberLeaves(node.getRight())

    def numberInternalNodes(self,node):
        return self.size(node)-self.numberLeaves(node)

    def height(self, node):
        if node == None:
            return 0
        return max(1 + self.size(node.getLeft()), 1 + self.size(node.getRight()))-1

    def belongs(self,node,val):
        if node==None:
            return False
        if node.getVal()==val:
            return True
        return self.belongs(node.getLeft(),val) or self.belongs(node.getRight(),val)

    def ancestors(self,node,val):
        if self.belongs(node, val):
            self.__ancestors(node,val)

    def __ancestors(self,node,val):
        if node==None:
            return False

        if node.getVal()==val:
            return True

        if self.__ancestors(node.getLeft(),val) or self.__ancestors(node.getRight(),val):
            print(node.getVal())
            return True

    def descendants(self,node,val):
        if self.belongs(node,val):
            self.__descendants(node,val)

    def __descendants(self,node,val):
        if node==None:
            return
        if node.getVal()==val:
            self.printValues(node.getLeft())
            self.printValues(node.getRight())
            return

        self.descendants(node.getLeft(),val)
        self.descendants(node.getRight(),val)


if __name__=="__main__":
    values=[12,5,4,3,6,17,19,18,21]
    nodes=[]
    for value in values:
        nodes.append(Node(value))

    binaryTree=BinaryTree()

    for node in nodes:
        binaryTree.insert(node)


    print("Affichage de l'arbre :")
    binaryTree.printValues(nodes[0])
    print('-' * 10)
    print(f"Taille de l'arbre : {binaryTree.size(nodes[0])}")
    print(f"Somme des valeurs de l'arbre : {binaryTree.sumValues(nodes[0])}")
    print(f"Hauteur de l'arbre : {binaryTree.height(nodes[0])}")
    print(f"Nombre de feuilles : {binaryTree.numberLeaves(nodes[0])}")
    print(f"Nombre de noeuds internes : {binaryTree.numberInternalNodes(nodes[0])}")
    print('-'*10)
    print(f"12 une valeur de l'arbre ? {binaryTree.belongs(nodes[0],12)}")
    print(f"4 une valeur de l'arbre ? {binaryTree.belongs(nodes[0],4)}")
    print(f"17 une valeur de l'arbre ? {binaryTree.belongs(nodes[0],17)}")
    print(f"23 une valeur de l'arbre ? {binaryTree.belongs(nodes[0],23)}")
    print('-'*10)
    print("Affichage des antécédents de 3 :")
    binaryTree.ancestors(nodes[0],21)
    print('-' * 10)
    print("Affichage des descendants de 5 :")
    binaryTree.descendants(nodes[0],5)