from typing import List, Optional, Dict, Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order: List[int] = list()

        self.traverse(root, order)

        return order[k - 1]

    def traverse(self, root: Optional[TreeNode], order: List[int]):
        if root is None:
            return

        self.traverse(root.left, order)
        order.append(root.val)
        self.traverse(root.right, order)
