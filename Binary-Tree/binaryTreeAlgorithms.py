#####################################################################
'''
 # Implements an unbalanced binary search tree algorithms.
 # @author Bhargav Lenka
'''
#####################################################################
from binaryTree import *

class BinaryTreeAlgo(Node):
    def height(self, root):
        if root:
            return 1 + max(self.height(root.left), self.height(root.right))
        else:
            return -1

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack = [root, ]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children[::-1])
        return result

    def print_path(self, root, subpath =  "", path = []):
        if not root:
            return []
        else:
            if not root.left and not root.right:
                path.append(subpath + str(root.val))
            if root.left:
                self.print_path(root.left, subpath + str(root.val) + "-->", path)
            if root.right:
                self.print_path(root.right, subpath + str(root.val) + "-->", path)
            return path

    def dfs_path(self, root):
        if root is None:
            return []
        stack = [(root,"")]
        path = []
        while stack:
            node, children = stack.pop()
            if not node.left and not node.right:
                path.append(children + str(node.val))
            if node.right:
                stack.append((node.right, children + str(node.val) + "-->"))
            if node.left:
                stack.append((node.left, children + str(node.val) + "-->"))
        return path

    def findMode(self, root, dict = {}):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            dict[root.val] = dict.get(root.val, 0) + 1
            self.findMode(root.left, dict)
            self.findMode(root.right, dict)
        else:
            return
        maxFreq = max(dict.values())
        result = [k for k, v in dict.items() if maxFreq == v]
        return result

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.secondMin = float('inf')
        firstMin = root.val

        def dfs(node):
            if node:
                if firstMin < node.val < self.secondMin:
                    self.secondMin = node.val
                elif node.val == firstMin:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return self.secondMin if self.secondMin < float('inf') else -1

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        count = 0
        stack = [(root, sum)]

        while stack:
            node, s = stack.pop()
            if s == 0:
                count += 1
                if not node.left is None:
                    stack.append((node.left, sum))
                if not node.right is None:
                    stack.append((node.right, sum))
            if not node.left is None:
                stack.append((node.left, sum - node.val))
            if not node.right is None:
                stack.append((node.right, sum - node.val))
        return count

    def pathSum_root_leaf(self, root, sum):
        if root is None:
            return sum == 0
        if sum == 0 and root.left is None and root.right is None:
                return True
        return self.pathSum_root_leaf(root.left, sum - root.val) or self.pathSum_root_leaf(root.right, sum - root.val)


        #########------------dfs-----------############
        stack = [(root, sum - root.val)]
        while stack:
            node, currSum = stack.pop()
            if not node.left and not node.right and currSum == 0:
                return True
            if node.left:
                stack.append((node.left, currSum - node.left.val))
            if node.right:
                stack.append((node.right, currSum - node.right.val))
        return False

    def path_sum_counts(self, root, s):
        self.count = 0
        def helper(node, sum):
            if not node:
                return 0
            if node.val == sum:
                self.count += 1
            if node.left:
                helper(node.left, s - node.val)
            if node.right:
                node.right(node.right, s - node.val)
        if not root:
            return 0
        helper(root, sum)
        if root.left:
            self.pathSumCounts(root.left, sum)
        if root.right:
            self.pathSumCounts(root.right, sum)
        return self.count

        '''#########------------dfs-----------############

        if not root:
            return 0

        def helper(node, s):
            if not root:
                return 0
            stack = [(node, s)]
            while stack:
                node, tempSum = stack.pop()
                if node:
                    if tempSum == node.val:
                        self.count += 1
                    stack.append(node.left, tempSum - node.val)
                    stack.append(node.right, tempSum - node.val)
            return self.count

        stack = [root]
        count = 0
        while tree:
            node = stack.pop()
            if node:
                count += helper(node, sum)
                stack.append(node.right)
                stack.append(node.left)
        return count'''

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root:
            lHeight = self.height(root.left)
            rHeight = self.height(root.right)
            if abs(rHeight - lHeight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False

        def isSubtree(self, s, t):
            """
            :type s: TreeNode
            :type t: TreeNode
            :rtype: bool
            """
            if s is None:
                return False
            if t is None:
                return True
            if self.isSame(s, t) == 1:
                return True
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

        def isSame(self, root1, root2):
            if root1 is None and root2 is None:
                return 1
            if not root1 is None and not root2 is None:
                if root1.val == root2.val and self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right):
                    return 1
            else:
                return 0

def main():
    from random import randint
    binaryTree = Node(8)
    root = Node(8)
    data = [randint(0, 100) for i in range(20)]
    binaryTree.build_tree(root, data)
    binaryTreeAlgo = BinaryTreeAlgo(8)
    path = binaryTreeAlgo.print_path(root)
    print("\n", path)

if __name__ == '__main__':
    main()