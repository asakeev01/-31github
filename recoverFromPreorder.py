from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes = []
        n = len(traversal)
        i = 0

        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1

            value = 0
            while i < n and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1

            nodes.append((depth, value))

        root = TreeNode(nodes[0][1])
        stack = [(0, root)]

        for depth, value in nodes[1:]:
            node = TreeNode(value)

            while stack and stack[-1][0] >= depth:
                stack.pop()

            parent = stack[-1][1]
            if not parent.left:
                parent.left = node
            else:
                parent.right = node

            stack.append((depth, node))

        return root