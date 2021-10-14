from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root: TreeNode = TreeNode()
        value = preorder[0]
        inorder_root_index = inorder.index(value)
        root.val = value
        root.left = self.buildTree(preorder[1:inorder_root_index + 1], inorder[:inorder_root_index])
        root.right = self.buildTree(preorder[inorder_root_index + 1:], inorder[inorder_root_index + 1:])
        return root

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return
        print(root.val)  # preorder
        self.traverse(root.left)
        print(root.val)  # inorder
        self.traverse(root.right)
