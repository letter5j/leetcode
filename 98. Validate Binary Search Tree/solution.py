from typing import List, Optional, Dict, Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root, float('-inf'), float('inf'))

    def traverse(self, root: Optional[TreeNode], min_value: int, max_value: int) -> bool:
        if root is None:
            return True
        if root.val <= min_value or root.val >= max_value:
            return False
        return self.traverse(root.left, min_value, root.val) and self.traverse(root.right, root.val, max_value)
