from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        def dfs(node, isGrandParentEven, isParentEven):
            if not node:
                return
            if isGrandParentEven:
                print(node.val)
                self.answer += node.val
            if node.val % 2 == 0:
                dfs(node.left, isParentEven, True)
                dfs(node.right, isParentEven, True)
            else:
                dfs(node.left, isParentEven, False)
                dfs(node.right, isParentEven, False)
        dfs(root, False, False)
        return self.answer