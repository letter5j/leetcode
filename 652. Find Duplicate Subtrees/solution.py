from typing import List, Optional, Dict, Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        tree_stack: Dict[str, int] = dict()
        duplicate_tree: List[TreeNode] = list()

        root_tree = self.traverse(root, tree_stack, duplicate_tree)

        return duplicate_tree

    def traverse(self, root: Optional[TreeNode], tree_stack: Dict[str, int],
                 duplicate_tree: List[TreeNode]) -> str:
        if root is None:
            return ""

        left_subtree = self.traverse(root.left, tree_stack, duplicate_tree)
        right_subtree = self.traverse(root.right, tree_stack, duplicate_tree)

        subtree = str(root.val) + "L" + left_subtree + "R" + right_subtree

        if subtree in tree_stack:
            if tree_stack[subtree] == 1:
                duplicate_tree.append(root)
            tree_stack[subtree] = tree_stack[subtree] + 1

        else:
            tree_stack[subtree] = 1

        return subtree
