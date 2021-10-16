from typing import List, Optional, Dict, Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum: int = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tree = self.traverse(root)
        return tree

    def traverse(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return

        tree = TreeNode()

        tree.right = self.traverse(root.right)
        self.sum = self.sum + root.val
        tree.val = self.sum
        tree.left = self.traverse(root.left)

        return tree
