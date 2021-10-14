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

        value = preorder.

        inorder_index = inorder.index(value)
        root.val = value

        if
        root.left = self.buildTree(preorder[1:inorder_index])

        root


        self.buildTree(preorder)

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return
        print(root.val)  # preorder
        self.traverse(root.left)
        print(root.val)  # inorder
        self.traverse(root.right)
