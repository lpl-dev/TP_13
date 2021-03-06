class Node:
    def __init__(self,val):
        self.__val=val
        self.__left=None
        self.__right=None

    def __str__(self):
        return str(self.__val)


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
        self._root=None

    def getRoot(self):
        return self._root

    def insert(self,node):
        if self._root==None:
            self._root=node
        else:
            self.__insert(node, self._root)

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
        return self._root == node

    def size(self,node):
        if node==None:
            return 0
        return 1+self.size(node.getLeft())+self.size(node.getRight())

    def printValues(self,node):
        if node==None:
            return
        self.printValues(node.getLeft())
        print(node)
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
            print(node)
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

    def prefixe(self,node):
        if node == None:
            return
        print(node)
        self.prefixe(node.getLeft())
        self.prefixe(node.getRight())

    def infixe(self,node):
        if node == None:
            return
        self.infixe(node.getLeft())
        print(node)
        self.infixe(node.getRight())
        # = printValues

    def postfixe(self,node):
        if node == None:
            return
        self.postfixe(node.getLeft())
        self.postfixe(node.getRight())
        print(node)

    def widetrack(self,node):
        self.__widetrack(node,self.size(node),[],0)

    def __widetrack(self, node, treesize, floors_list=[], floor_nbr=0):
        if node==None:
            if len(floors_list)==treesize:
                floors_list_sorted=sorted(floors_list,key=lambda f:f['floor_nbr'])
                treesize=len(floors_list_sorted)
                for i in range(treesize):
                    if i<treesize-1 and  floors_list_sorted[i]['floor_nbr']==floors_list_sorted[i+1]['floor_nbr']:
                        print(floors_list_sorted[i]['value'],end=' ')
                    else:
                        print(floors_list_sorted[i]['value'])
            return
        self.__widetrack(node.getLeft(), treesize, floors_list, floor_nbr + 1)
        floors_list.append({'value':node.getVal(),'floor_nbr':floor_nbr})
        self.__widetrack(node.getRight(), treesize, floors_list, floor_nbr + 1)

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def contains(self,node,val):
        return self.belongs(node,val)

    def findMin(self,node):
        if node.getLeft()==None:
            return node
        return self.findMin(node.getLeft())

    def findMax(self, node):
        if node.getRight() == None:
            return node
        return self.findMax(node.getRight())

    def equivalentBST(self,node1,node2):
        return self.getTreeValues(node1)==self.getTreeValues(node2)

    def getTreeValues(self,node):
        return self.__getTreeValues(node,self.size(node),[])

    def __getTreeValues(self,node,treesize,values=[]):
        if node == None:
            if len(values) == treesize:
                return values
            return
        values.append(node.getVal())
        self.__getTreeValues(node.getLeft(), treesize, values)
        return self.__getTreeValues(node.getRight(), treesize, values)

    def delete(self,node,val):
        parent=self.getParentOfNodeValue(node,val)
        if parent != None:
            left=parent.getLeft()
            right=parent.getRight()
            node_v=left if (left!=None and left.getVal()==val) else right
            if node_v.getLeft()==None and node_v.getRight()==None:
                # noeud avec val = feuille
                new_child=None
            elif node_v.getLeft()==None or node_v.getRight()==None:
                left_c = node_v.getLeft()
                right_c= node_v.getRight()
                child=left_c if left_c!=None else right_c
            else:
                new_child=self.findMax(node_v.getLeft())

                new_child.setLeft(node_v.getLeft())
                new_child.setRight(node_v.getRight())

                new_child_parent=self.getParentOfNodeValue(node,new_child.getVal())
                if new_child_parent.getLeft()==new_child:
                    new_child_parent.setLeft(None)
                else:
                    new_child_parent.setRight(None)
            if parent.getLeft() == node_v:
                parent.setLeft(new_child)
            else:
                parent.setRight(new_child)
        else:
            # noeud avec val = root
            self._root = self.findMax(node.getLeft())

            self._root.setLeft(node.getLeft())
            self._root.setRight(node.getRight())

            new_root_previous_parent = self.getParentOfNodeValue(node, self._root.getVal())
            if new_root_previous_parent.getLeft() == self._root:
                new_root_previous_parent.setLeft(None)
            else:
                new_root_previous_parent.setRight(None)

    def getParentOfNodeValue(self,node,val):
        ancestors=self.__getParentOfNodeValue(node,val,[])
        return None if node.getVal()==val else ancestors[0]

    def __getParentOfNodeValue(self,node,val,ancestors=[]):
        if node == None:
            return False
        if node.getVal() == val:
            return True
        if self.__getParentOfNodeValue(node.getLeft(),val,ancestors) or self.__getParentOfNodeValue(node.getRight(),val,ancestors):
            ancestors.append(node)
        return ancestors

    def isBST(self,node):
        left=node.getLeft()
        right=node.getRight()
        val=node.getVal()
        if left!=None and right!=None:
            return self.isBST(node.getLeft()) and self.isBST(node.getRight())
        elif left!=None:
            return left.getVal()<val
        elif right!=None:
            return right.getVal()>val
        else:
            return True

if __name__=="__main__":
    print("""
    -----------
    Binary Tree
    -----------\n\n
    """)
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
    print("Affichage des antécédents de 21 :")
    binaryTree.ancestors(nodes[0],21)
    print('-' * 10)
    print("Affichage des descendants de 5 :")
    binaryTree.descendants(nodes[0],5)
    print('-' * 10)
    print("Affichage suivant un parcours prefixe :")
    binaryTree.prefixe(nodes[0])
    print('-' * 10)
    print("Affichage suivant un parcours infixe :")
    binaryTree.infixe(nodes[0])
    print('-' * 10)
    print("Affichage suivant un parcours postfixe :")
    binaryTree.postfixe(nodes[0])
    print('-' * 10)
    print("Affichage suivant un parcours largeur :")
    binaryTree.widetrack(nodes[0])

    print("""\n\n
    ------------------
    Binary Search Tree
    ------------------\n\n
    """)
    values=[4,2,0,1,3,20,12,7,6,15,13,14]
    nodes_s=[]
    for value in values:
        nodes_s.append(Node(value))
    binarySearchTree=BinarySearchTree()

    for node in nodes_s:
        binarySearchTree.insert(node)

    print("Affichage suivant un parcours infixe :")
    binarySearchTree.infixe(nodes_s[0])

    print('-' * 10)
    print(f"12 une valeur de l'arbre ? {binarySearchTree.contains(nodes_s[0], 12)}")
    print(f"4 une valeur de l'arbre ? {binarySearchTree.contains(nodes_s[0], 4)}")
    print(f"17 une valeur de l'arbre ? {binarySearchTree.contains(nodes_s[0], 17)}")
    print(f"23 une valeur de l'arbre ? {binarySearchTree.contains(nodes_s[0], 23)}")

    print('-' * 10)
    print(f"Valeur minimale de l'arbre ? {binarySearchTree.findMin(nodes_s[0])}")
    print(f"Valeur maximale de l'arbre ? {binarySearchTree.findMax(nodes_s[0])}")

    print('-' * 10)
    print(f"Arbres équivalents ? {binarySearchTree.equivalentBST(nodes_s[0],nodes_s[0])}")
    print(f"Arbres équivalents ? {binarySearchTree.equivalentBST(nodes_s[1], nodes_s[2])}")

    print('-' * 10)
    print("Affichage suivant un parcours largeur avant suppression du 2:")
    binarySearchTree.widetrack(binarySearchTree.getRoot())
    binarySearchTree.delete(nodes_s[0], 4)
    print("Affichage suivant un parcours largeur après suppression du 2:")
    binarySearchTree.widetrack(binarySearchTree.getRoot())

    print('-' * 10)
    print(f"L'arbre est un ABR ? {binarySearchTree.isBST(nodes_s[0])}")