from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        s = set(to_delete)
        answer = []
        def rec(node, isRoot):
            if not node:
                return None
            isDeleted = node.val in s
            if isRoot and not isDeleted:
                answer.append(node)
            node.left = rec(node.left, isDeleted)
            node.right = rec(node.right, isDeleted)
            return None if isDeleted else node
        rec(root, True)
        return answer