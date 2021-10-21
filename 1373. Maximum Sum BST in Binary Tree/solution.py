from typing import List, Optional, Dict, Set, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeInfo:
    is_BST: bool
    sumary: int
    min_value: int
    max_value: int




class Solution:

    max_sum = 0

    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        sumary, valid = self.traverse(root)

        return sumary if sumary > 0 else 0

    def is_valid_tree(self, root: Optional[TreeNode]):

        if root is None:
            return True

        if root.left is not None and root.left.val >= root.val:
            return False
        if root.right is not None and root.right.val <= root.val:
            return False

        return True

    def traverse(self, root: Optional[TreeNode]) -> TreeInfo:

        if root is None:
            treeinfo = TreeInfo()
            treeinfo.is_BST = True
            treeinfo.sumary = 0
            treeinfo.max_value = 0
            treeinfo.min_value = 0
            return treeinfo

        left_treeinfo  = self.traverse(root.left)
        right_treeinfo  = self.traverse(root.right)

        if

