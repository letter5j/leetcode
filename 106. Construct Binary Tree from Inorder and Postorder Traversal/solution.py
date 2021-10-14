from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Input: inorder = [9, 3, 15, 20, 7], postorder = [9, 15, 7, 20, 3]
        # Output: [3, 9, 20, null, null, 15, 7]
        if len(inorder) == 0:
            return None
        root: TreeNode = TreeNode()
        value = postorder[len(postorder) - 1]
        inorder_root_index = inorder.index(value)
        root.val = value
        root.left = self.buildTree(inorder[: inorder_root_index], postorder[: inorder_root_index])
        root.right = self.buildTree(inorder[inorder_root_index + 1:], postorder[inorder_root_index: len(postorder) - 1])
        return root

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return
        print(root.val)  # preorder
        self.traverse(root.left)
        print(root.val)  # inorder
        self.traverse(root.right)
