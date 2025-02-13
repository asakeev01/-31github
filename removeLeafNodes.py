from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if node.left:
                if dfs(node.left) == False:
                    node.left = None
            if node.right:
                if dfs(node.right) == False:
                    node.right = None
            if not node.left and not node.right and node.val == target:
                return False
            elif not node.left and not node.right:
                return True

        if dfs(root) == False:
            return None
        else:
            return root