from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.l = []
        def recursion(node):
            if node == None:
                return None
            left = recursion(node.left)
            if left != None:
                self.l.append(left.val)
            self.l.append(node.val)
            right = recursion(node.right)
            if right != None:
                self.l.append(right.val)
        recursion(root)
        return self.l[k-1]