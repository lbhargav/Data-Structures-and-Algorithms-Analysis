'''
insert( root, x )       --> Insert x
builtTree(root, data)  --> return binary tree with data
delete( root, x )       --> Remove x
boolean find( root, x )  --> Return true if x is present
find_min(root)  --> Return smallest item
find_max(root)  --> Return largest item
boolean isEmpty( )     --> Return true if empty; else false
makeEmpty( )      --> Remove all items
printTree(root)      --> Print tree in sorted order
'''
#####################################################################
'''
 # Implements an unbalanced binary search tree.
 # @author Bhargav Lenka
'''
#####################################################################
import random
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def build_tree(self, root, data):
        if data is None:
            return -1
        for i in data:
            tree  = self.insert(root, i)
        return tree

    def insert(self, root,  x):
        if x is None:
            return -1
        newNode = Node(x)
        if root:
            if newNode.val <= root.val:
                if root.left is None:
                    root.left = newNode
                else:
                    self.insert(root.left, x)
            else:
                if root.right is None:
                    root.right = newNode
                else:
                    self.insert(root.right, x)
        else:
            root = newNode

    def find(self,root, x):
        if root:
            if root.val == x:
                print("\n", "Has Node with value: {}".format(x))
                return True
            else:
                if x <= root.val:
                    self.find(root.left, x)
                else:
                    self.find(root.right, x)

    def find_min(self, root):
        if root is None:
            return root
        elif root.left is None:
            return root
        return self.find_min(root.left)

    def find_max(self, root):
        if not root is None:
            while not root.right is None:
                root = root.right
        return root

    def delete(self, root, x):
        if root is None:
            return  root
        if x < root.val:
            root.left = self.delete(root.left, x)
        elif x > root.val:
            root.right = self.delete(root.right, x)
        elif not root.left is None and not root.right is None:
            root.val = self.find_min(root.right).val
            root.right = self.delete(root.right, root.val)
        else:
            root = root.left if not root.left is None else root.right
        return  root

    def print_tree(self, root):
        """
        Print tree content inorder
        """
        if root.left:
            root.left.print_tree(root.left)
        print(root.val, end = " ")
        if root.right:
            root.right.print_tree(root.right)

def main():
    binaryTree = Node(8)
    root = Node(8)
    data = [random.randint(0, 100) for i in range(20)]
    binaryTree.build_tree(root, data)
    binaryTree.print_tree(root)
    binaryTree.find(root, 59)
    binaryTree.delete(root, 59)
    binaryTree.print_tree(root)
    print(binaryTree.pathSum(root, 12))

if __name__ == '__main__':
    main()
