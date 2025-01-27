# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # If the current node is None (base case), return an empty list
        if not root:
            return []

        # Recursively get the inorder traversal of the left subtree
        left_tree = self.inorderTraversal(root.left)

        # Recursively get the inorder traversal of the right subtree
        right_tree = self.inorderTraversal(root.right)

        # Combine the results: left subtree values, current node value, and right subtree values
        return left_tree + [root.val] + right_tree