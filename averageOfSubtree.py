

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.counter = 0
        def rec(node):
            if node == None:
                return [0, 0]
            leftAnswer = rec(node.left)
            rightAnswer = rec(node.right)
            quantity = leftAnswer[1] + rightAnswer[1] + 1
            values = leftAnswer[0] + rightAnswer[0] + node.val
            if quantity == 0:
                return [node.val, 1]
            else:
                if values // quantity == node.val:
                    self.counter += 1
                return [values, quantity]
        rec(root)
        return self.counter