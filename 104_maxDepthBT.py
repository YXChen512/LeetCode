# Define TreeNode and implement binary tree
# Recursively find the depth

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class binaryTree(object):
    

    def maxDep(self):
        if (self.left == None) & (self.right == None):
            return 1
        else:
            return max(maxDep(self.left),maxDep(self.right)) + 1

    def addNote(self, newNode):
        if newNode.val <= self.val:
            if self.left == None:
                self.left = newNode
            else:
                self.left.addNote(newNode)

#Test: construct a tree from input and calc depth

print("Input a list of integers for constructing Binary Tree (in brakets [] and separated by ,comma):\n")
values = input('>')
Length = len(values)
print("Length of the list")
