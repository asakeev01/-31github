from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        answer = []
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            answer.append(node.val)
            if node.left != None:
                queue.appendleft(node.left)
            if node.right != None:
                queue.appendleft(node.right)
        return answer[::-1]