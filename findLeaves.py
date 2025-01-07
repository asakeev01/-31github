from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        self.curr = []
        def find_leaves(node):
            if not node.left and not node.right:
                self.curr.append(node.val)
                node = None
                return True
            l = find_leaves(node.left) if node.left else False
            r = find_leaves(node.right) if node.right else False
            if l:
                node.left = None
            if r:
                node.right = None
        while root:
            if not root.left and not root.right:
                self.curr.append(root.val)
                self.ans.append(self.curr)
                break
            else:
                find_leaves(root)
                self.ans.append(self.curr)
                self.curr = []
        return self.ans