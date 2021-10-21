from typing import List, Optional, Dict, Set, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeInfo:
    is_BST: bool = False
    sumary: int = 0
    min_value: int = 0
    max_value: int = 0


class Solution:
    max_sum = 0

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.max_sum

    def traverse(self, root: Optional[TreeNode]) -> TreeInfo:

        if root is None:
            treeinfo = TreeInfo()
            treeinfo.is_BST = True
            treeinfo.sumary = 0
            treeinfo.max_value = float("-inf")
            treeinfo.min_value = float("inf")
            return treeinfo

        left_treeinfo = self.traverse(root.left)
        right_treeinfo = self.traverse(root.right)

        treeinfo = TreeInfo()
        if left_treeinfo.is_BST and right_treeinfo.is_BST and left_treeinfo.max_value < root.val < right_treeinfo.min_value:

            sumary = root.val + left_treeinfo.sumary + right_treeinfo.sumary

            self.max_sum = max(sumary, self.max_sum)

            treeinfo.is_BST = True
            treeinfo.sumary = sumary
            treeinfo.max_value = max(root.val, right_treeinfo.max_value)
            treeinfo.min_value = min(root.val, left_treeinfo.min_value)

        else:
            treeinfo.is_BST = False

        return treeinfo
