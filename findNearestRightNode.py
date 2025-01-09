from typing import Optional

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if u == root.val:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            nodes_in_level = len(queue)
            for i in range(nodes_in_level):
                node = queue.popleft()
                if node == u:
                    return queue[0] if i < nodes_in_level - 1 else None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return None