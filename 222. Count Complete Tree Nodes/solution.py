from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        return self.traverse(root)

    def traverse(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        root_left_count = self.traverse(root.left)
        root_right_count = self.traverse(root.right)

        return root_left_count + root_right_count + 1