# Binary Search Tree
# dealing with integers as node values

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class binaryTree(object):
    def __init__(self):
        self.rootNode = None

    def getRoot(self):
        return self.rootNode

    def addNode(self, newVal): # In-order tree
        if self.rootNode == None:
            self.rootNode = TreeNode(newVal)
        else:
            self._addNode(newVal,self.rootNode)
    def _addNode(self,newVal,node):
        if newVal<= node.val:
            if node.left == None:
                node.left = TreeNode(newVal)
            else:
                self._addNode(newVal,node.left)
        else:
            if node.right == None:
                node.right = TreeNode(newVal)
            else:
                self._addNode(newVal,node.right)

    def  maxDep(self):
        if (self.left == None) & (self.right == None):
            return 1
        else:
            return max(maxDep(self.left),maxDep(self.right)) + 1

    def printTree(self,order="in.order"):
        if self.rootNode!= None:
            self._printTree(self.rootNode,order)


    def _printTree(self,node,order):
        if ((order!="in.order") & (order !="pre.order")
        & (order!="post.order")):
            print("False order input!")
            return None
        if node!=None:
            if order == "post.order":
            # left child -> rigit child -> root
                self._printTree(node.left,order)
                self._printTree(node.right,order)
                print str(node.val) + " "
            elif order == "pre.order":
                print str(node.val) + " "
                self._printTree(node.left,order)
                self._printTree(node.right,order)
            # root-> left child-> right child
            else:# default "in.order"
                self._printTree(node.left,order)
                print str(node.val) + " "
                self._printTree(node.right,order)
    def findPath(self,val):
        if self.rootNode!=None:
            _find(val,self.rootNode)
#    def _findPath(self,val,node):
#        if

tree= binaryTree()
tree.rootNode == None
tree.addNode(5)
#tree.printTree()
tree.addNode(3)
#tree.printTree()
tree.addNode(7)
#tree.printTree()
tree.addNode(2)
#tree.printTree()
tree.addNode(4)
#tree.printTree()
tree.addNode(6)
#tree.printTree()
tree.addNode(8)
#tree.printTree()
tree.addNode(9)
#tree.printTree()
tree.addNode(1)
#tree.printTree()
tree.printTree("pre.order")
#tree.printTree("post.order")
