from typing import List, Optional, Dict, Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        root = self.traverse(root, val)
        return root

    def traverse(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            root: TreeNode = TreeNode()
            root.val = key
            return root

        if key < root.val:
            root.left = self.traverse(root.left, key)
        else:
            root.right = self.traverse(root.right, key)

        return root