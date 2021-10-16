from typing import List, Optional, Dict, Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        root = self.traverse(root, key)
        return root

    def traverse(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return

        if key < root.val:
            root.left = self.traverse(root.left, key)
        elif key > root.val:
            root.right = self.traverse(root.right, key)
        else:
            if root.left:
                root_right: TreeNode = root.right
                root = root.left
                temp: TreeNode = root
                while temp is not None:
                    if temp.right is None:
                        temp.right = root_right
                        break
                    temp = temp.right
            else:
                root = root.right
        return root